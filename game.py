from player import Player
from pokemon import Pokemon
import random
class Game:
    def __init__(self) -> None:
        self.player = Player()
        self.pokemon_list = [
            Pokemon("1", "Audino", 19, "It touches others with the feelers on its ears, using the sound of their heartbeats to tell how they are feeling. Its auditory sense is astounding. It has a radar-like ability to understand its surrounding through slight sounds.", 100), 
            Pokemon("2", "Bidoof", 25, "With nerves of steel, nothing can perturb it. It is more agile and active than it appears. It constantly gnaws on logs and rocks to whittle down its front teeth. It nests alongside water.", 100),
            Pokemon("3", "Bonsly", 30, "It looks as if it is always crying. It is actually adjusting its body's fluid levels by eliminating excess. It prefers arid environments. It leaks water from its eyes to adjust its body's fluid levels.", 100),
            Pokemon("4", "Combee", 34, "A Pokemon formed by three others. It busily carries sweet floral honey to Vespiquen. It collects and delivers honey to its colony. At night, they cluster to form a beehive and sleep.", 100),
            Pokemon("5", "Krabby", 32, "Its pincers are not only powerful weapons, they are used for balance when walking sideways. Its pincers are superb weapons. They sometimes break off during battle, but they grow back fast.", 100)
        ]
        self.opponent = Player(random.choice(self.pokemon_list))

    def welcome(self):
        print("Welcome to Pokemon Game!")

        #select Pokemon and call player menu
    def start_main_menu(self):
        #display a list of Pokemons
        for pokemon in self.pokemon_list:
            print(pokemon.id + " - " + pokemon.name + ": hp = " + str(pokemon.hp) + "; attack = " + str(pokemon.attack))
        selected_id = input("Please choose a number of the Pokemon: ")
        if int(selected_id) > len(self.pokemon_list):
            print("Select number from 1 to 5")
            self.start_main_menu()
        else:
            for pokemon in self.pokemon_list:
                #find the object by selected id
                if pokemon.id == selected_id:
                    #set pokemon for Player
                    self.player.set_pokemon(pokemon)
                    print("You've chosen... " + pokemon.name + "! Good Choice!")
                    break
            #start player menu
            self.start_player_menu()
            
       #player menu displays options after Pokemon was selected
    def start_player_menu(self):
        user_selection = input("1 - Read description about your pokemon, \n2 - Change Pokemon \n3 - Start Fight! \nYour choice:  ")
        if user_selection == "1":
            #show description
            self.player.describe_selected_pokemon()
            self.start_player_menu()
        elif user_selection == "2":
            #change pokemon
            self.start_main_menu()
        elif user_selection == "3":
            #start fight
            print("Your opponent Pokemon is " + self.opponent.selected_pokemon.name + "\n")
            self.battle_menu()
                
        #this is the last function that is called, all the actions about battle happens here until Game Over
    def battle_menu(self):
        #get hp
        pokemon_hp = self.player.get_pokemon_hp()
        opponent_hp = self.opponent.get_pokemon_hp()

        while pokemon_hp > 0 or opponent_hp > 0:
            print("Your turn..."  + "\n")
            print("1 - Attack, 2 - Heal (random number)")
            pokemon_action = input("Your choice: ")
            if pokemon_action == "1":
                #attack opponent
                opponent_hp = self.calculate_hp("1", self.player.selected_pokemon.name, self.opponent.selected_pokemon.name, opponent_hp, self.player.selected_pokemon.attack)
                if opponent_hp <= 0:
                    print("Game Over, You Won!")
                    break
            else:
                #heal pokemon
                pokemon_hp = self.calculate_hp("2", self.player.selected_pokemon.name, self.player.selected_pokemon.name, pokemon_hp, self.player.selected_pokemon.attack)
            print("Opponent turn..." + "\n")
            opponent_action = random.choice(["1", "2"])
            if opponent_action == "1":
                #attack pokemon
                pokemon_hp = self.calculate_hp("1", self.opponent.selected_pokemon.name, self.player.selected_pokemon.name, pokemon_hp, self.opponent.selected_pokemon.attack)
                if pokemon_hp <= 0:
                    print("Game Over, You lost.")
                    break
            else:
                #heal opponent
                opponent_hp = self.calculate_hp("2", self.opponent.selected_pokemon.name, self.opponent.selected_pokemon.name, opponent_hp, self.opponent.selected_pokemon.attack)
            
            
    def calculate_hp(self, action: str, pokemon_name: str, opponent_name: str, pokemon_hp: int, opponent_attack: int) -> int:
        if action == "1":
            #attack
            print(pokemon_name + " attacks!")
            pokemon_hp -= opponent_attack
            print("-" + str(opponent_attack) + " hp")
            print(opponent_name + " remaining hp is... " + str(pokemon_hp))
            print("")
        elif action == "2":
            #heal
            if pokemon_hp < 100 and pokemon_hp > 0:
                heal_num = random.choice([2, 5, 9, 13, 15])
                pokemon_hp += heal_num
                print("Healing applied")
                print("+" + str(heal_num) + " to " + pokemon_name + " hp")
                print(pokemon_name + " remaining hp is " + str(pokemon_hp))
                print("")
            else:
                print("Heal is not possible")
        else:
            print("Select 1 or 2")
        return pokemon_hp