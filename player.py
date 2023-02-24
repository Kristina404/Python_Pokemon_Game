class Player:
    def __init__(self, selected_pokemon=None) -> None:
        #object Pokemon
        self.selected_pokemon = selected_pokemon

        #This function displays all pokemons to the console and asks to choose one of them, returns Pokemon object
    def set_pokemon(self, pokemon: object) -> object:
        self.selected_pokemon = pokemon  
        return self.selected_pokemon

        #this function displays all Pokemon's atributes to the user
    def describe_selected_pokemon(self):
            print(f"Name: {self.selected_pokemon.name}")
            print(f"Description: {self.selected_pokemon.description}")
            print(f"Attack: {str(self.selected_pokemon.attack)}")
            print(f"HP: {str(self.selected_pokemon.hp)}")

    def get_pokemon_hp(self):
        return self.selected_pokemon.hp
