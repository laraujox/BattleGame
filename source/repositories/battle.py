import logging

from source.models.battle import Battle
from source.models.player import Player
from source.repositories.abstraction import AbstractRepository

logger = logging.getLogger("repositories.battle")


class BattleRepository(AbstractRepository):
    def add(self, battle: Battle) -> Battle:
        logger.info(
            f"Saving Battle between the two players #{battle.player1.name} "
            f"and #{battle.player2.name}"
        )
        self.session.add(battle)
        self.session.commit()
        return battle

    def update_results(self, battle: Battle, winner: Player, gold_stolen: int) -> None:
        # logger.info(f"Getting Battle with Id #{battle_id}.")
        battle.winner = winner
        battle.gold_stolen = gold_stolen

        self.session.commit()
