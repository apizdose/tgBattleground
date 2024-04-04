import os
import json

path = r'./queques/' 
if not os.path.exists(path):
    os.makedirs(path)

def start(group):
    with open(f"{path}{group}_queue.list","w") as file:
        json.dump([],file)


def join(group,username):
    data=get(group)
    if username in data:
        return False
    else:
        data.append(username)
        load(group,data)
        return True
    




def get(group):
    with open(f"{path}{group}_queue.list") as file:
        txt=file.read()
        data=json.loads(txt)
        return data


def load(group,data):
    with open(f"{path}{group}_queue.list","w") as file:
        json.dump(data,file)


def roll(group):
    data=get(group)
    username=data.pop(0)
    data.append(username)
    load(group,data)
    return data[0]
    

#-4192689530


