import random

Fissure_accuracy = random.randint(1, 10)

if Fissure_accuracy in (1, 3, 5):
    print("One hit K.O")

else:
    print("but it failed")

Present_accuracy = random.uniform(0.0, 1.0)
present_chance_to_heal = random.uniform(1.0,2.0)

if Present_accuracy >= 0.3625:
    print("good luck")
elif present_chance_to_heal >= (1.5) :
    print("healed the opponent")
else:
    print("but it failed")
