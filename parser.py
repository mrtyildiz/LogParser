import json

file_name = "/var/log/messages"
file = open(file_name, "r")
data = []
order = ["moon", "Days", "clock", "host", "hsmd", "message", "HSMCommand","HSMCommand2"]

def LogginParse():
    dataJson = []
    for line in file.readlines():
        details = line.split(" ")
        details = [x.strip() for x in details]
        structure = {key:value for key, value in zip(order, details)}
        data.append(structure)
    for entry in data:
        HSM_Json = json.dumps(entry, indent = 4)
        y = json.loads(HSM_Json)
        dataJson.append(y)
    y = json.loads(HSM_Json)
    return dataJson
LogginParse()