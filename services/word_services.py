from datetime import datetime, timedelta

start_date = datetime(2020, 1, 1)
total_words = 3480


word = {"value": "abaca", "day": (datetime.now() - timedelta(days=1)).date()}

def get_word():
    if word["day"] < datetime.now().date():
        word["value"] = calulate_word_of_the_day()
        word["day"] = datetime.now().date()
    print("get_word called, word: ", word["day"], word["value"] )
    return word

def calulate_word_of_the_day():
    index = map_day_to_number(total_days_since_start(start_date, datetime.now().date()), total_words)
    with open('shuffled_five_letter_words.txt', 'r') as file:
        words = file.readlines()
    return words[index].strip()

def check_word(word_attempt):
    print(word_attempt)
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

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_year_until(date):
    start_of_year = datetime(date.year, 1, 1)
    return (date - start_of_year).days + 1

def total_days_since_start(start_date, current_date):
    total_days = 0
    for year in range(start_date.year, current_date.year):
        total_days += 366 if is_leap_year(year) else 365
    total_days += days_in_year_until(current_date)
    return total_days

def map_day_to_number(total_days, max_number):
    return total_days  % max_number 