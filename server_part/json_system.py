import json
import os

def readfile(filename: str):
    try:
        with open(f"packets/{filename}.json", "r", encoding="UTF-8") as file:
            template = json.load(file)
    except Exception as e:
        return None, e
    return template


def writefile(filename: str, type_of_message: str, con1: str, con2: str, con3: str):
    os.makedirs("packets2", exist_ok=True)
    filepath = f"packets2/{filename}.json"
    with open(filepath, "w", encoding="UTF-8") as file:
        if type_of_message == "message":
            to_json = {"type": type_of_message, "from": con1, "to": con2, "contains": con3}
            json.dump(to_json, file)
    return filepath

# writeFile("ex2", "message", "me", "Shamanchik", "nigga nigga nigga nigga")
# print(readFile("ex2"))
print(readfile("send"))