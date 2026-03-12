import random

randomBr = random.randint(1,20)
pogodak = int(input("Pogodi broj "))

while pogodak != randomBr:
    if pogodak>randomBr:
        print("Broj je manji")        
    else:
        print("Broj je veci")

    pogodak = int(input("Pogodi broj: "))

print("Bravo pogodili ste broj")

