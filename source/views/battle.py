import logging
from http import HTTPStatus

from flask import jsonify, request, Blueprint
from marshmallow import ValidationError

from source.error_handling.exceptions import (
    PlayerDoesNotExistException,
)
from source.error_handling.schemas import BattleCreationSchema
from source.services.battle import process_battle

logger = logging.getLogger("views.battle")

# battle_repository = PlayerRepository()
battle_creation_schema = BattleCreationSchema()

BATTLE_BLUEPRINT = Blueprint("battle", __name__, url_prefix="/battle")


@BATTLE_BLUEPRINT.route("/", methods=["POST"])
def create_battle():
    """
    POST /battle
    Create a new battle.

    Request body:
    {
        "attacker_name": "HotBarbecu3",
        "defender_name": "Vegan2",
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
        battle_data = battle_creation_schema.load(json_data)

        battle, round_log = process_battle(
            battle_data["attacker_name"], battle_data["defender_name"]
        )
        # battle_repository.add(Player(**battle_data))
        return jsonify(
            {
                "winner": battle.winner.name,
                "gold_stolen": battle.gold_stolen,
                "round_log": round_log,
            }
        )
    except ValidationError as err:
        # Handle fields validation
        return jsonify(err.messages), HTTPStatus.BAD_REQUEST.value
    except PlayerDoesNotExistException as err:
        # Handle custom validations
        return jsonify(err.to_dict()), err.status_code
