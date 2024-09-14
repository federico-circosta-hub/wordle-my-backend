from flask import Blueprint, jsonify, request # type: ignore
from services.word_services import get_word, check_word
from flask_cors import CORS

bp = Blueprint('wordle_routes', __name__)
CORS(bp)

@bp.route("/")
def init():
    word = get_word()
    return jsonify(word["day"])

@bp.route("/check_word", methods=['POST'])
def api_check_word():
    get_word()
    word_attempt = request.json.get('word_attempt')
    if not word_attempt:
        return jsonify({"error": "Missing word_attempt in request body"}), 400
    result = check_word(word_attempt)
    return jsonify(result)
