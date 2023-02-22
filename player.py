class Player:
    def __init__(self, selected_pokemon=None) -> None:
        #object Pokemon
        self.selected_pokemon = selected_pokemon

        #This function displays all pokemons to the console and asks to choose one of them, returns Pokemon object
    def pick_pokemon(self, pokemons_list: list) -> object:
        print("Here you can see our pokemons:")
        #display a list of Pokemons
        for pokemon in pokemons_list:
            print(pokemon.id + " - " + pokemon.name + ": hp = " + str(pokemon.hp) + "; attack = " + str(pokemon.attack))
        selected_id = input("Please choose a number of the Pokemon: ")
        if int(selected_id) > 5:
            print("Select number from 1 to 5")
            self.pick_pokemon(pokemons_list)
        else:   
            for pokemon in pokemons_list:
                #find the object by selected id
                if pokemon.id == selected_id:
                    self.selected_pokemon = pokemon
                    print("You've chosen... " + self.selected_pokemon.name + "! Good Choice!")    
        return self.selected_pokemon

        #this function displays all Pokemon's atributes to the user
    def describe_selected_pokemon(self):
            print("Name: " + self.selected_pokemon.name)
            print("Description: " + self.selected_pokemon.description)
            print("Attack: " + str(self.selected_pokemon.attack))
            print("HP: " +  str(self.selected_pokemon.hp))

    def get_pokemon_hp(self):
        return self.selected_pokemon.hp
