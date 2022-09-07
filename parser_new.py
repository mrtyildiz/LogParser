import json
from socket import AF_ECONET
from .definition import LogExplanation
file_name = "/var/log/messages"
file = open(file_name, "r")
data = []
dataJson = []
order = ["Date", "Clock", "Host", "HSMD", "Message", "HSMCommand", "Definition"]

def LogginParse():
    for line in file.readlines():
        details = line.split(" ")
        if details[4] != 'hsmd:':
            pass
        else:
            Array = []
            deta = [x.strip() for x in details]
            Datet = str(deta[1])+" "+str(deta[0])
            Array.append(Datet)
            Clock = str(deta[2])
            Array.append(Clock)
            Host = str(deta[3])
            Array.append(Host)
            HSMD = str(deta[4])
            Array.append(HSMD)
            Message = str(deta[5])
            Array.append(Message)
            if 5 <= len(deta):
                x = len(deta) - 5
                HSMCommand = ""
                for i in range(x):
                    HSMCommand = str(HSMCommand)+deta[5+i]+" "
            else:
                pass
            Array.append(HSMCommand)
            definition = LogExplanation(Message,HSMCommand)
            Array.append(definition)
            structure = {key:value for key, value in zip(order, Array)}
            data.append(structure)
    for entry in data:
        HSM_Json = json.dumps(entry, indent = 5)
        y = json.loads(HSM_Json)
        dataJson.append(y)
#        print(HSM_Json)
    dataJson.reverse()
    return(dataJson)
