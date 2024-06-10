import logging

from source.error_handling.exceptions import PlayerDoesNotExistException
from source.models.player import Player
from source.repositories.abstraction import AbstractRepository

logger = logging.getLogger("repositories.player")


class PlayerRepository(AbstractRepository):
    def add(self, player: Player) -> None:
        logger.info(f"Saving Player with name #{player.name}.")
        self.session.add(player)
        self.session.commit()

    @staticmethod
    def get_by_name(player_name: str) -> Player:
        logger.info(f"Getting Player with name #{player_name}.")
        player = Player.query.filter_by(name=player_name).first()
        if player:
            return player
        # raise PlayerDoesNotExistException(player_name)

    @staticmethod
    def get(player_id: int) -> Player:
        logger.info(f"Getting Player with Id #{player_id}.")
        player = Player.query.get(player_id)
        if player:
            return player
        raise PlayerDoesNotExistException(player_id)

    def update_gold(self, player: Player, gold: int, deduce: bool = False) -> None:
        logger.info(f"Updating gold for Player with Id #{player.id}.")
        if deduce:
            player.gold -= gold
        else:
            player.gold += gold

        self.session.commit()
