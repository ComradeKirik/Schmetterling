import json


def readfile(filename: str):
    try:
        with open(f"packets/{filename}.json", "r", encoding="UTF-8") as file:
            template = json.load(file)
    except Exception:
        return None
    finally:
        return template


def writefile(filename: str, type_of_message: str, con1: str, con2: str, con3: str):
    with open(f"packets/{filename}.json", "w+", encoding="UTF-8") as file:
        if type_of_message == "message":
            to_json = {"type": type_of_message, "from": con1, "to": con2, "contains": con3}
            file.write(json.dumps(to_json))

# writeFile("ex2", "message", "me", "Shamanchik", "nigga nigga nigga nigga")
# print(readFile("ex2"))
