import json


def pull_db():
    with open("./db/notes.json", "r", encoding="utf8") as file:
        return json.load(file)


def push_db(data):
    with open("./db/notes.json", "w", encoding="utf8") as file:
        json.dump(data, file, ensure_ascii=False)
