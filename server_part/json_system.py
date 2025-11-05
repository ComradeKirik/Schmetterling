import json

def readFile(filename: str):
    try:
        with open(f"packets/{filename}.json", "r", encoding="UTF-8") as file:
            template = json.load(file)
    except Exception as e:
        return None
    finally:
        return template

def writeFile(filename: str, type: str, con1: str, con2: str, con3: str):
    with open(f"packets/{filename}.json", "w+", encoding="UTF-8") as file:
        if type == "message":
            to_json = {"type": type, "from": con1, "to": con2, "contains": con3}
            file.write(json.dumps(to_json))

#writeFile("ex2", "message", "me", "Shamanchik", "nigga nigga nigga nigga")
#print(readFile("ex2"))