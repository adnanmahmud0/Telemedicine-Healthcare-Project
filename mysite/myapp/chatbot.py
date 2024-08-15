# chatbot_app/chatbot_app.py

import re
import json
import os


def load_keywords_from_file(filename):
    with open(filename, 'r') as file:
        keywords_f = json.load(file)
        # print(keywords)
    return keywords_f


def match_keyword(user_input, keywords_f):
    for keyword_category in keywords_f.values():
        for keyword in keyword_category['keywords']:
            pattern = r'\b' + re.escape(keyword) + r'\b'
            if re.search(pattern, user_input, re.IGNORECASE):
                return keyword_category['response']
    return "Sorry! Give me more information."


file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'keywords.json')
keywords = load_keywords_from_file(file_path)


def get_chatbot_response(user_input):
    print(user_input)
    reply = match_keyword(user_input, keywords)
    print(reply)
    return reply


# test_input = "Hello"
# response = match_keyword(test_input, keywords)
# print(response)
