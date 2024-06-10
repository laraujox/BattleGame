import logging
from typing import List

from source.models.round import Round
from source.repositories.abstraction import AbstractRepository

logger = logging.getLogger("repositories.round")


class RoundRepository(AbstractRepository):
    def add(self, round_obj: Round) -> None:
        logger.info(f"Saving Round for battle with id #{round_obj.battle_id}")
        self.session.add(round_obj)
        self.session.commit()

    def bulk_add(self, round_list: List[Round]) -> None:
        logger.info(f"Saving Round list for battle with id #{round_list[0].battle_id}")
        self.session.bulk_save_objects(round_list)
        self.session.commit()
