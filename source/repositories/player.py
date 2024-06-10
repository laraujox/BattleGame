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

    def get(self, player_id: int) -> Player:
        logger.info(f"Getting Player with Id #{player_id}.")
        player = Player.query.get(player_id)
        if player:
            return player
        raise PlayerDoesNotExistException(player_id)
