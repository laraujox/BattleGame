import abc
from extensions import db


class AbstractRepository(abc.ABC):
    def __init__(self, session=db.session):
        self.session = session

    @abc.abstractmethod
    def add(self, *args, **kwargs):
        """add data on the database"""
        raise NotImplementedError  # pragma: no cover
