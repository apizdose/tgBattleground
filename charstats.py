import random
import json

try:
    with open("players.json","r",encoding="utf-8") as file:
        file.read
except:
    with open("players.json","w",encoding="utf-8") as file:
        json.dump({},file)




data={}

def save(data):
    with open("players.json","w",encoding="utf-8") as file:
        json.dump(data,file)


def join(group,name):
    if group not in data:
        return False
    if name in data[group]['players']:
        return False
    else:
        tmpdict={}
        hp=random.randint(85,120)
        mp=random.randint(3,5)
        tmpdict["hp"]=hp
        tmpdict["mp"]=mp
        data[group]['players'][name]=tmpdict
        save(data)
        return {"name":name,"hp":hp,"mp":mp}

def tab(group):
    location=data[group]['location']
    msg=f'Players table on {location}:\n\n'
    
    if group in data:
        for i in data[group]['players']:
            name=i
            hp=data[group]['players'][i]['hp']
            mp=data[group]['players'][i]['mp']
            msg+=f"@{name} {hp} \\ {mp}\n"
    else:
        msg="No players!"
    return msg

def players(group):
    location=data[group]['location']
    resp=[]
    
    if group in data:
        for i in data[group]['players']:
            name=i
            resp.append(i)
    else:
        return False
    return resp

def location():
    return 'баня'

def start(group):
    data[group]={}
    data[group]['location']=location()
    data[group]['players']={}
    save(data)

def stop(group):
    if group in data:
        del data[group]
    save()

def load():
    with open("players.json","r",encoding="utf-8") as file:
        global data
        data=json.loads(file.read())



