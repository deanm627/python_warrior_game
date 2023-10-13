import random

class Warrior:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    
    def status(self):
        print(f"{self.name}'s health: {self.health}")
    
    def attackedBy(self, other):
        self.health -= other.power
        print(f"{self.name} lost {other.power} points\n\n")
    
    def alive(self, other):
        if self.health > 0:
            return True
        else:
            print(f"{other.name} wins!\n\n")
            print("-------THE END-------\n\n")
            return False

class Zombie:
    def __init__(self, name, power):
        self.name = name
        self.power = power

def main():
    print("\n-------WELCOME TO THE WARRIOR R-P-S GAME!-------\n\n")
    hero_name = input("What is your hero name? ")
    villain_name = input("What is your villain name? ")
    hero = Warrior(hero_name, 20, 5)
    villain = Warrior(villain_name, 20, 3)
    zombie = Zombie("Zombie", 2)

    rps = ["Rock", "Paper", "Scissors"]

    def rps_game_villain(user_choice):
        user_choice -= 1
        villain_choice = random.randint(0, len(rps)-1)
        print(f"\n\n{hero.name}: {rps[user_choice]} | {villain.name}: {rps[villain_choice]}")
        if user_choice == villain_choice:
            print("Tie! Try again\n\n")
            return
        elif user_choice == 0 and villain_choice == 1:
            print(f"{villain.name} wins. {rps[villain_choice]} covers {rps[user_choice]}")
            hero.attackedBy(villain)
        elif user_choice == 0 and villain_choice == 2:
            print(f"{hero.name} wins. {rps[user_choice]} smashes {rps[villain_choice]}")
            villain.attackedBy(hero)
        elif user_choice == 1 and villain_choice == 0:
            print(f"{hero.name} wins. {rps[user_choice]} covers {rps[villain_choice]}")
            villain.attackedBy(hero)
        elif user_choice == 1 and villain_choice == 2:
            print(f"{villain.name} wins. {rps[villain_choice]} cut {rps[user_choice]}")
            hero.attackedBy(villain)
        elif user_choice == 2 and villain_choice == 0:
            print(f"{villain.name} wins. {rps[villain_choice]} smashes {rps[user_choice]}")
            hero.attackedBy(villain)
        elif user_choice == 2 and villain_choice == 1:
            print(f"{hero.name} wins. {rps[user_choice]} cut {rps[villain_choice]}")
            villain.attackedBy(hero)

    def rps_game_zombie(user_choice):
        print(f"Zombie round! Zombies have {zombie.power} power, but they can't die...")
        user_choice -= 1
        zombie_choice = random.randint(0, len(rps)-1)
        print(f"\n\n{hero.name}: {rps[user_choice]} | {zombie.name}: {rps[zombie_choice]}")
        if user_choice == zombie_choice:
            print("Tie! Try again\n\n")
            return
        elif user_choice == 0 and zombie_choice == 1:
            print(f"{zombie.name} wins. {rps[zombie_choice]} covers {rps[user_choice]}")
            hero.attackedBy(zombie)
        elif user_choice == 0 and zombie_choice == 2:
            print(f"{hero.name} wins. {rps[user_choice]} smashes {rps[zombie_choice]}")
            print("Zombies can't die!\n\n")
        elif user_choice == 1 and zombie_choice == 0:
            print(f"{hero.name} wins. {rps[user_choice]} covers {rps[zombie_choice]}")
            print("Zombies can't die!\n\n")
        elif user_choice == 1 and zombie_choice == 2:
            print(f"{zombie.name} wins. {rps[zombie_choice]} cut {rps[user_choice]}")
            hero.attackedBy(zombie)
        elif user_choice == 2 and zombie_choice == 0:
            print(f"{zombie.name} wins. {rps[zombie_choice]} smashes {rps[user_choice]}")
            hero.attackedBy(zombie)
        elif user_choice == 2 and zombie_choice == 1:
            print(f"{hero.name} wins. {rps[user_choice]} cut {rps[zombie_choice]}")
            print("Zombies can't die!\n\n")

    while hero.alive(villain) and villain.alive(hero):
        hero.status()
        villain.status()
        villain_or_zombie = random.randint(0, 3)
        user_choice = input("Pick one: 1 - Rock, 2 - Paper, 3 - Scissors\nType 1, 2, or 3: ")
        if user_choice == '1' or user_choice == '2' or user_choice == '3':
            if villain_or_zombie == 3:
                rps_game_zombie(int(user_choice))
            else: 
                rps_game_villain(int(user_choice))
        else:
            print("-------ERROR: Invalid input, try again-------\n\n")

main()