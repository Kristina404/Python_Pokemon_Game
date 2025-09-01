from pokemon import Pokemon

class Player:
    """Defines a Player in the game, who can select and manage a Pokemon."""

    def __init__(self, selected_pokemon=None) -> None:
        self.selected_pokemon = selected_pokemon

    def set_pokemon(self, pokemon: Pokemon) -> None:
        """Sets the selected Pokemon for the Player."""
        self.selected_pokemon = pokemon  

    def describe_selected_pokemon(self) -> None:
        """Prints the details of the selected Pokemon."""
        print(f"Name: {self.selected_pokemon.name}")
        print(f"Description: {self.selected_pokemon.description}")
        print(f"Attack: {str(self.selected_pokemon.attack)}")
        print(f"HP: {str(self.selected_pokemon.hp)}")

    def get_pokemon_hp(self) -> int:
        """Returns the HP of the selected Pokemon."""
        return self.selected_pokemon.hp
