from http import HTTPStatus
from typing import Union


class MainException(Exception):
    def __init__(self, message: str, status_code: int, extra: dict):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.extra = extra

    def to_dict(self):
        return {
            "message": self.message,
            "status_code": self.status_code,
            "extra": self.extra,
        }


class PlayerDoesNotExistException(MainException):
    def __init__(self, player: Union[int, str]):
        message = f"Player #{player} does not exist."
        status_code = HTTPStatus.NOT_FOUND.value
        extra = {"player": player}
        super().__init__(message, status_code, extra)
