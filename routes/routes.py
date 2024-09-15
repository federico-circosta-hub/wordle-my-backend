from flask import Blueprint, jsonify, request
from services.word_services import get_word, check_word

bp = Blueprint('wordle_routes', __name__)

@bp.route("/")
def init():
    word = get_word()
    return jsonify(word["day"])

@bp.route("/check_word", methods=("GET",'POST', "OPTIONS"))
def check_word():
    print("here from check_word()")
    if request.method == 'OPTIONS':
        response = jsonify({"message": "CORS preflight response"})
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response, 200
    word_attempt = request.json.get('word_attempt')
    if not word_attempt:
        return jsonify({"error": "Missing word_attempt in request body"}), 400

    result = check_word(word_attempt)
    return jsonify(result)
