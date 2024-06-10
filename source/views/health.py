from flask import Blueprint, jsonify

API_BLUEPRINT = Blueprint("api", __name__, url_prefix="/")


@API_BLUEPRINT.route("/")
def health():
    """
    GET /
    Simple health endpoint.

    Example:
    curl -X GET http://127.0.0.1:5000/

    Response:
    {
        "message": "The app is running fine! :)"
    }
    """
    return jsonify({"message": "The app is running fine! :)"})
