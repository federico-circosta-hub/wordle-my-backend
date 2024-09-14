from flask import Blueprint, jsonify, request
from services.word_services import get_word, check_word

bp = Blueprint('wordle_routes', __name__)

@bp.route("/")
def init():
    word = get_word()
    return jsonify(word["day"])

@bp.route("/check_word", methods=['POST'])
def api_check_word():
    word_attempt = request.json.get('word_attempt')
    if not word_attempt:
        return jsonify({"error": "Missing word_attempt in request body"}), 400

    result = check_word(word_attempt)
    return jsonify(result)
