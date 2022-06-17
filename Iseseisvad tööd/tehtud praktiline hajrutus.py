import random

class Uksus:
    def __init__(self, health):
        self.health = health

    def hit(target, target1):
        if target.health > 0:
            target.health -= 20
            if target1 == uksus1:
                target1 = "Üksus1"
            if target1 == uksus2:
                target1 = "Üksus2"
            print(target1, "ründas")
            print(target.health, "alles")
        if target.health == 0:
            print(target1, "võitis")


uksus1 = Uksus(100)
uksus2 = Uksus(100)

while uksus1.health > 0 and uksus2.health > 0:
    ran = random.randint(0, 10)

    if ran >= 5:
        Uksus.hit(uksus1, uksus2)
    else:
        Uksus.hit(uksus2, uksus1)