import random
from datetime import datetime, timedelta

word = {"value": "abaca", "day": (datetime.now() - timedelta(days=1)).date()}

def get_word():
    if word["day"] < datetime.now().date():
        word["value"] = get_random_word()
        word["day"] = datetime.now().date()
    print("get_word called, word: ", word["day"], word["value"] )
    return word

def get_random_word():
    with open('five_letter_words.txt', 'r') as file:
        words = file.readlines()
    return random.choice(words).strip()

def check_word(word_attempt):
    word_characters_occorrence_map = {
        char: word["value"].count(char) for char in word["value"]
    }
    result = []
    for i in range(5):
        result.append({
            "right_position": word_attempt[i] == word["value"][i],
        })
        if result[i]["right_position"]:
            word_characters_occorrence_map[word_attempt[i]] -= 1
    for i, element in enumerate(result):
        element["is_present"] = element["right_position"] or (word_attempt[i] in word['value'] and word_characters_occorrence_map[word_attempt[i]] > 0)
        if word_attempt[i] in word_characters_occorrence_map and word_characters_occorrence_map[word_attempt[i]] > 0:
            word_characters_occorrence_map[word_attempt[i]] -= 1
    return result
