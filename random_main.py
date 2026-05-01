from fastapi import FastAPI
import json
import random

app = FastAPI()

rand = []
name_file_load = "action.json"
try:
    with open(name_file_load, "r") as file:
        rand = json.load(file)
except FileNotFoundError:
    print("File not found, starting with empty list")
    rand = []
except:
    print("error, starting with empty list")
    rand = []

def save_file():
    with open(name_file_load, "w") as file:
        json.dump(rand,file)

last_random = ""

@app.get("/")
def get_random_action():
    if not rand:
        return {"message": "no action"}
    if len(rand) == 1:
        return {"message": rand[0]}
    global last_random
    random_action = ""
    while True:
        random_action = random.choice(rand)
        if random_action != last_random:
            last_random = random_action
            return {"message": random_action}
    

@app.post("/add/{text}")
def add_action(text: str):
    text = text.strip()
    if not text:
        return {"error": "write the action"}
    if text in rand:
        return {"error": "there is already such an action"}
    rand.append(text)
    save_file()
    return {"added": text}

@app.get("/all")
def get_all():
    if not rand:
        return {"message": "no action"}
    all_action = {}
    for i in range(len(rand)):
        all_action[i+1] = rand[i]
    return {"actions" : all_action}

@app.delete("/del/{index}", summary = "index начинается с 1")
def delete_action(index: int):
    if not rand:
        return {"message": "no action"}
    if index < 1 or index > len(rand):
        return {"error": "invalid index"}
    deleted = rand.pop(index - 1)
    save_file()
    return {"message": deleted}