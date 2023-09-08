import string

class Poke:
    name : string
    attack :int
    defense : int
    speed : int
    attackList : list
    
    def __init__(self, name, attack, defense, speed, attackList : list) -> None:
        self.name = name
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.attackList = attackList
        
        
    def perform_attack (self) -> None :
        print("The pokemon is attacking somehow...")
    
    
def main ():
    x = Poke ("Charizard", 83, 70, 100, {"Wing attack", "Flamethrougher", "Slash"})
    print(x.attackList)
    x.perform_attack()
  
    
main()