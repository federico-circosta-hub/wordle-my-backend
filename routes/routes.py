from flask import Blueprint, jsonify, request
from services.word_services import get_word, check_word, encrypt_string, is_valid_word
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY").encode('utf-8')

bp = Blueprint("wordle-my", __name__)

@bp.route("/")
def init():
    word = get_word()
    return jsonify(word["day"])

@bp.route("/check_word", methods=("GET","POST"))
def api_check_word():
    word_attempt = request.json.get('word_attempt')
    if not word_attempt:
        return jsonify({"error": "Missing word_attempt in request body"}), 400
    if not is_valid_word(word_attempt):
        return jsonify({"error": "invalid word"}), 422
    result = check_word(word_attempt)
    return jsonify(result)

@bp.route('/encrypted_word', methods=['GET'])
def encrypt():
    word = get_word()
    encrypted_data = encrypt_string(word["value"], SECRET_KEY)
    return jsonify(encrypted_data), 200