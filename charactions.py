import random
import charstats

def attack(group,username,target):
    dmg = random.randint(5,15)
    if charstats.data[group]["players"][username]['hp'] > 0:
        charstats.data[group]["players"][target]['hp'] -=dmg
        charstats.save(charstats.data)
        return dmg
    else:
        return False
    
def restore(group,username,target):
    heal = random.randint(3,10)
    if charstats.data[group]["players"][username]['mp'] > 0:
        charstats.data[group]["players"][target]['hp'] += heal
        charstats.data[group]["players"][username]['mp'] -= 1
        return heal
    else:
        return False



    