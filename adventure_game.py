# Text-based adventure game where the player searches for a legendary treasure.

# ---------------------------
# Helper function: ask again
# ---------------------------
# This function keeps asking the player for a valid choice until one is entered.
def get_choice(prompt, valid_choices):
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_choices:
            return choice
        print(f"Invalid choice. Please choose: {', '.join(valid_choices)}")


# ---------------------------
# Ending function
# ---------------------------
# This function displays the final outcome of the game.
def end_game(result, player_name):
    if result == "win":
        print(f"\nCongratulations, {player_name}! You found the legendary treasure and completed your quest!")
    elif result == "lose":
        print(f"\nGame over, {player_name}. Your adventure has come to an end.")


# ---------------------------
# Forest path
# ---------------------------
# This function handles the story events that happen if the player enters the forest.
def forest_path(player_name):
    print("\nYou step into the dark forest. The trees tower above you, and strange sounds echo around you.")
    print("Soon you discover a rushing river and a tall tree with a clear view of the land.")

    choice = get_choice(
        "Do you want to 'follow' the river or 'climb' the tree? ",
        ["follow", "climb"]
    )

    if choice == "climb":
        print("\nYou climb the tree and spot an ancient stone temple hidden beyond the forest.")
        print("When you arrive at the temple, you find a locked treasure chamber.")

        second_choice = get_choice(
            "Do you 'solve' the temple puzzle or try to 'force' the door open? ",
            ["solve", "force"]
        )

        if second_choice == "solve":
            print("\nYou solve the puzzle, and the stone door slowly opens.")
            end_game("win", player_name)
            return "win"
        else:
            print("\nA trap is triggered, and the chamber collapses around you.")
            end_game("lose", player_name)
            return "lose"

    else:
        print("\nYou follow the river downstream and discover an ancient stone bridge covered in moss.")
        print("Across the bridge you can see the ruins of an old village.")

        second_choice = get_choice(
            "Do you 'cross' the bridge or 'search' the riverbank for clues? ",
            ["cross", "search"]
        )

        if second_choice == "cross":
            print("\nYou cross the bridge and explore the ruins. Hidden beneath a crumbled wall")
            print("you find a tunnel that leads directly to the legendary treasure chamber!")
            end_game("win", player_name)
            return "win"
        else:
            print("\nYou search the riverbank and find faded carvings pointing deeper into the forest.")

            third_choice = get_choice(
                "Do you 'follow' the carvings deeper into the forest or 'turn back' to the bridge? ",
                ["follow", "turn back"]
            )

            if third_choice == "follow":
                print("\nThe carvings lead you to a hidden grove where the treasure is buried under a great oak tree!")
                end_game("win", player_name)
                return "win"
            else:
                print("\nYou head back to the bridge, but the path has vanished in the darkness.")
                print("Night falls, and the treasure remains far out of reach.")
                end_game("lose", player_name)
                return "lose"


# ---------------------------
# Cave path
# ---------------------------
# This function handles the story events that happen if the player enters the cave.
def cave_path(player_name):
    print("\nYou enter the mysterious cave. The air is cold, and the passage ahead is nearly pitch black.")

    choice = get_choice(
        "Do you 'light' a torch or walk 'dark' into the cave? ",
        ["light", "dark"]
    )

    if choice == "light":
        print("\nThe torch reveals a hidden map carved into the wall.")
        print("The map leads you to an underground chamber with a sleeping guardian.")

        second_choice = get_choice(
            "Do you try to 'sneak' past the guardian or 'attack' it? ",
            ["sneak", "attack"]
        )

        if second_choice == "sneak":
            print("\nYou move quietly past the guardian and find a golden chest behind the chamber.")
            end_game("win", player_name)
            return "win"
        else:
            print("\nThe guardian awakens and defeats you before you can escape.")
            end_game("lose", player_name)
            return "lose"

    else:
        print("\nWithout light, you stumble into a deep pit hidden in the darkness.")
        end_game("lose", player_name)
        return "lose"


# ---------------------------
# Start game
# ---------------------------
# This function introduces the adventure, asks for the player's name,
# and lets the player choose the first path.
def start_game():
    print("Welcome to the Adventure Game!")
    print("Your quest is to find a legendary treasure hidden in an ancient land.")

    player_name = input("What is your name, explorer? ").strip()
    if not player_name:
        player_name = "Explorer"

    print(f"\nWelcome, {player_name}!")
    print("You stand at the edge of a forgotten land.")
    print("In front of you is a dark forest, and beside it is a mysterious cave.")

    first_choice = get_choice(
        "Do you enter the 'forest' or the 'cave'? ",
        ["forest", "cave"]
    )

    if first_choice == "forest":
        return forest_path(player_name)
    else:
        return cave_path(player_name)


# ---------------------------
# Main game loop
# ---------------------------
# This loop starts the game and allows the player to restart after winning or losing.
def main():
    print("Setup check: adventure_game.py is running correctly.\n")

    while True:
        start_game()
        restart = get_choice(
            "\nWould you like to play again? Type 'yes' or 'no': ",
            ["yes", "no"]
        )
        if restart == "no":
            print("\nThanks for playing. Goodbye!")
            break
        print("\nRestarting your adventure...\n")


# ---------------------------
# Program entry point
# ---------------------------
# This ensures the game starts only when the file is run directly.
if __name__ == "__main__":
    main()
