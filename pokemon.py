class Pokemon:
    """A class representing a Pokemon with its attributes."""
    def __init__(self, id: str, name: str, attack: int, description: str, hp: int) -> None:
        self.id = id
        self.name = name
        self.attack = attack
        self.description = description
        self.hp = hp
