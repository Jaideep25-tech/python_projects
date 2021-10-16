import math
import random

# In the Warrior class, we will define the counstructor method to create our warrior, as well as define methods to calculate their attacks. Since it's a fight simulator, the attacks and blocks will have random values.
class Warrior:
    # Here, we define the method to create our warrior.
    def __init__(self, name = "", health = 0, max_attk = 0, max_block = 0):
        self.name = name
        self.health = health
        self.max_attk = max_attk
        self.max_block = max_block
    # This method declares the attack power of the warrior.
    def attack(self):
        attk = self.max_attk * (random.random() + 0.5)
        return attk
    # This method defines the block power of the warrior.
    def block(self):
        block = self.max_block * random.random()
        return block
    
    
# Now we will define the Battle class, that will handle the battle simulation. We don't have to declare a initiator method for this class.
class Battle:

    # What this method does is it continues to loop over and over again until one of our warrior dies and the other one is declared victorious.
    def battle_arena(self, warrior1, warrior2):
        while True:
            if self.attack_result(warrior1, warrior2) == "Game Over":
                print("GAME OVER")
                break
            if self.attack_result(warrior2, warrior1) == "Game Over":
                print("GAME OVER")
                break

    # Now, we will define the attack_result method. This method will simulate all the attacks, blocks and health drops of our warriors.
    # We will use static method for this method. A @staticmethod is a method that knows nothing about the class or instance it was called on. It just gets the arguments that were passed on to it.
    @staticmethod
    def attack_result(warriorA, warriorB):
        warriorA_attk = warriorA.attack()
        warriorB_block = warriorB.block()
        damage_dealt = math.ceil(warriorA_attk - warriorB_block)
        warriorB.health = warriorB.health - damage_dealt
        print("{} dealt {} damage on {}".format(warriorA.name, damage_dealt, warriorB.name))
        print("{}'s health drops to {}\n".format(warriorB.name, warriorB.health))


        if warriorB.health <=0:
            winner = warriorA.name
            print("Fatality! {} is dead and {} emerged as VICTORIOUS!".format(warriorB.name, warriorA.name))
            if bet_on == warriorA.name:
                print("\nYou won the bet! Congratulations!")
            else:
                print("\nYou lost the bet. Better luck next time.")
            return "Game Over"
        else:
            return "Fight Continues"

    # We will define a method that allows us to bet on either of the two warriors.
    @staticmethod
    def betting(warrior1, warrior2):
        x = input("Whom do you wanna place your bet on? Enter 1 for Superman, 2 for Batman : ")
        print()
        x = int(x.strip())
        global bet_on
        if x == 1:
            bet_on = warrior1.name
        else:
            bet_on = warrior2.name


# Now, lets define the main function.
def main():
    # We will create two warrior objects.
    superman = Warrior("Superman", 100, 20, 10)
    batman = Warrior("Batman", 100, 20, 10)

    # We will create a battle object.
    battle_start = Battle()
    battle_start.betting(superman, batman)
    # The code-block below will initiate the arena method, that will simulate the fight.
    battle_start.battle_arena(superman,batman)

main()
