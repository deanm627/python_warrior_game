import random

def main():
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
                print("-------THE END-------")
                return False

    hero_name = input("What is your hero name? ")
    villain_name = input("What is your villain name? ")
    hero = Warrior(hero_name, 20, 5)
    villain = Warrior(villain_name, 20, 3)

    rps = ["Rock", "Paper", "Scissors"]

    def rps_game(user_choice):
        user_choice -= 1
        villain_choice = random.randint(0, len(rps)-1)
        print(f"\n{hero.name}: {rps[user_choice]} | {villain.name}: {rps[villain_choice]}")
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

    while hero.alive(villain) and villain.alive(hero):
        hero.status()
        villain.status()
        user_choice = input("Pick one: 1 - Rock, 2 - Paper, 3 - Scissors\nType 1, 2, or 3: ")
        if user_choice == '1' or user_choice == '2' or user_choice == '3':
            rps_game(int(user_choice))
        else:
            print("---ERROR: Invalid input, try again---\n\n")

main()