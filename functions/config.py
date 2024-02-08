import json

with open('configuration/config.json', 'r') as file:
    config = json.load(file)

key = config["key"]
secret = config["secret"]
username = config["username"]
password = config["password"]
delay = config["delay"]
debug = config["debug"]
webhook = config["webhook"]