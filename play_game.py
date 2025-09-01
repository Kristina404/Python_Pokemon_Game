from game import Game

def main():
    """Entry point for the game application."""
    game = Game()
    game.welcome()
    game.start_main_menu()


if __name__ == "__main__":
    main()
