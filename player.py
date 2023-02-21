class Player:
    def __init__(self, selected_pokemon=None) -> None:
        self.selected_pokemon = selected_pokemon

        #This function shows all pokemons names and asks to choose one of them 
    def pick_pokemon(self, pokemons_list):
        print("Here you can see our pokemons:")
        for pokemon in pokemons_list:
            print(pokemon.id + " - " + pokemon.name)
        selected_id = input("Please choose the number of your pokemon: ")
        for pokemon in pokemons_list:
            if pokemon.id == selected_id:
                self.selected_pokemon = pokemon
                print("You've chosen... " + self.selected_pokemon.name + "! Good Choice!")
        # else:
        #     print("Please select a valid name or number of Pokemon")
            # self.pick_pokemon(pokemons_list)    
        return self.selected_pokemon

    def describe_selected_pokemon(self):
        #check if pokemon was chosen before calling this function
        if self.selected_pokemon.name != None:
            print("Name: " + self.selected_pokemon.name)
            print("Description: " + self.selected_pokemon.description)
            print("Attack: " + str(self.selected_pokemon.attack))
            print("HP: " +  str(self.selected_pokemon.hp))
        else:
            print("You haven't chosen a pokemon yet")

    def get_pokemon_hp(self):
        return self.selected_pokemon.hp
