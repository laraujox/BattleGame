import logging
import random

from source.error_handling.exceptions import PlayerDoesNotExistException
from source.models import Player
from source.models.battle import Battle
from source.models.round import Round
from source.repositories.battle import BattleRepository
from source.repositories.player import PlayerRepository
from source.repositories.round import RoundRepository

logger = logging.getLogger("services.battle")

player_repository = PlayerRepository()
round_repository = RoundRepository()
battle_repository = BattleRepository()


def calculate_stolen_gold(loser: Player) -> int:
    return random.randint(int(0.1 * loser.gold), int(0.2 * loser.gold))


def calculate_damage(attacker: Player):
    hp_ratio = attacker.hit_points / 100
    if hp_ratio <= 0.5:
        return 0.5 * attacker.attack_value
    return hp_ratio * attacker.attack_value


def attack_missed(defender: Player):
    return random.randint(1, 100) <= defender.luck_value


def process_battle(attacker_name: str, defender_name: str):
    attacker = player_repository.get_by_name(attacker_name)
    defender = player_repository.get_by_name(defender_name)
    if not attacker:
        raise PlayerDoesNotExistException(attacker_name)
    if not defender:
        raise PlayerDoesNotExistException(defender_name)

    battle = battle_repository.add(Battle(player1=attacker, player2=defender))

    rounds_log = []
    while attacker.hit_points > 0 and defender.hit_points > 0:
        # Attacker's turn
        if not attack_missed(defender):
            damage = calculate_damage(attacker)
            defender.hit_points -= damage
            rounds_log.append(
                Round(
                    battle_id=battle.id,
                    log=f"{attacker.name} attacked {defender.name} for {damage} damage",
                )
            )
        else:
            rounds_log.append(
                Round(
                    battle_id=battle.id,
                    log=f"{attacker.name} attacked {defender.name} but missed",
                )
            )

        if defender.hit_points <= 0:
            break

        # Defender's turn
        if not attack_missed(attacker):
            damage = calculate_damage(defender)
            attacker.hit_points -= damage
            rounds_log.append(
                Round(
                    battle_id=battle.id,
                    log=f"{defender.name} attacked {attacker.name} for {damage} damage",
                )
            )
        else:
            rounds_log.append(
                Round(
                    battle_id=battle.id,
                    log=f"{defender.name} attacked {attacker.name} but missed",
                )
            )

        if attacker.hit_points <= 0:
            break

    winner, loser = (
        (attacker, defender) if defender.hit_points <= 0 else (defender, attacker)
    )
    gold_stolen = calculate_stolen_gold(loser)
    rounds_log.append(
        Round(
            battle_id=battle.id,
            log=f"{winner.name} won the battle and stole {gold_stolen} gold from {loser.name}",
        )
    )

    player_repository.update_gold(winner, gold_stolen)
    player_repository.update_gold(loser, gold_stolen, deduce=True)
    battle_repository.update_results(battle, winner, gold_stolen)
    round_repository.bulk_add(rounds_log)
    return battle, [round_object.log for round_object in rounds_log]
