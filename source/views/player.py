import logging
from http import HTTPStatus

from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from source.error_handling.exceptions import (
    PlayerDoesNotExistException,
)
from source.error_handling.schemas import PlayerCreationSchema
from source.models import Player
from source.repositories.player import PlayerRepository

logger = logging.getLogger("views.player")
PLAYER_BLUEPRINT = Blueprint("player", __name__, url_prefix="/player")

player_repository = PlayerRepository()
player_creation_schema = PlayerCreationSchema()


@PLAYER_BLUEPRINT.route("/", methods=["POST"])
def create_player():
    """
    POST /player
    Create a new player.

    Request body:
    {
        ...
    }

    Response:
    {
        "message": "Player created successfully!"
    }
    """
    try:
        json_data = request.get_json()
        logger.info(f"Received Player creation request with payload {json_data}")

        # Validate request body fields
        player_data = player_creation_schema.load(json_data)

        player_repository.add(Player(**player_data))
        return jsonify({"message": "Player created successfully!"})
    except ValidationError as err:
        # Handle fields validation
        return jsonify(err.messages), HTTPStatus.BAD_REQUEST.value
    except PlayerDoesNotExistException as err:
        # Handle custom validations
        return jsonify(err.to_dict()), err.status_code
