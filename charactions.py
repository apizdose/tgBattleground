import random

characters={}

def charGen(name):
    tmpdict={}
    hp=str(random.randint(85,120))
    mp=str(random.randint(3,5))
    tmpdict["hp"]=hp
    tmpdict["mp"]=mp
    characters[name]=tmpdict

def dmgGen():
    while True:
        dmg = random.randint(5,15)
        yield dmg

def healGen():
    while True:
        heal = random.randint(1,5)
        yield heal

def dmg():
    return next(dmgGen())

def heal():
    return next(healGen())

def hit(username,dmg):
    hp=characters[username]['hp']
    updhp=int(hp)-dmg
    characters[username]['hp']=str(updhp)
    
def restore(username,heal):
    hp=characters[username]['hp']
    mp=characters[username]['mp']
    if int(mp) > 0:
        updhp=int(hp)+heal
        updmp=int(mp)-1
        characters[username]['hp']=str(updhp)
        characters[username]['mp']=str(updmp)
    else:
        pass



     


        
    