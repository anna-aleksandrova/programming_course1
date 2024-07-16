from classes import *

expecting_answer = ">>> "

def _name():
    """For player to input a name.

    Returns:
        name (str): A name of a player.
    """
    print("\nEnter a name of the player:")
    name = input(expecting_answer)
    return name

def _board_size():
    """For player to input a size of the board.

    Returns:
        board_size (int): A size of the board.
    """
    print("Enter the size of the board.")
    while True:
        board_size = input(expecting_answer)
        if board_size.isnumeric() and int(board_size) > 1:
            board_size = int(board_size)
            break
        else:
            print("Incorrect size. Try again")
    return board_size

def _board_choice():
    """For player to choose whether to enter or generate the board.

    Returns:
        board_choice (int): 0 for entering, 1 for generating.
    """
    print("Choose the mode for creating your board: 0 for entering, 1 for generating.")
    while True:
        board_choice = input(expecting_answer)
        if board_choice.isnumeric() and int(board_choice) in {0, 1}:
            board_choice = int(board_choice)
            break
        else:
            print("You entered incorrect mode. Try again.")
    return board_choice

def _ships_config():
    """For player to input ships' configuration if they chose generating the board.

    Returns:
        ships (dict): ships (dict): (key, value) = (size, amount): <amount> ships of <size> must be placed.
        ships_amount (int): A total amount of ships.
    """
    ships = {}
    ships_amount = 0
    print("Enter ships' configuration.")
    while True:
        size = int(input("Size: "))
        amount = int(input("Amount: "))
        ships_amount += amount
        ships[size] = amount
        print("Continue entering? (1 for yes, 0 for no).")
        next = input(expecting_answer)
        if int(next) == 0:
            break
        else:
            continue
    return ships, ships_amount

def _mines_config():
    """For player to input mines' configuration if they chose generating the board.

    Returns:
        mines (dict): (key, value) = (size, amount): <amount> mines of <size> must be placed.
        mines_amount (int): A total amount of mines.
    """
    mines = {}
    mines_amount = 0
    print("Enter mines' configuration.")
    while True:
        size = int(input("Size: "))
        amount = int(input("Amount: "))
        mines_amount += amount
        mines[size] = amount
        print("Continue entering? (1 for yes, 0 for no).")
        next = input(expecting_answer)
        if int(next) == 0:
            break
        else:
            continue
    return mines, mines_amount

def preparation():
    """
    Returns:
        player (Player) : A player in the game.
    """
    name = _name()
    board_size = _board_size()
    board_choice = _board_choice()
    ships = _ships_config()
    mines = _mines_config()
    player = Player(name, board_size, board_choice, ships, mines)
    return player

def attack(player, enemy):
    """Implements attack.

    Args:
        player (Player): They attack.
        enemy (Player): They are under attack.
    """
    print(f"\n---------------{player.name}-------------")

    print(f"{player.name}, your turn.")
    print("It's your board:")
    player.map.show_for_user(player)
    print("It's your enemy's board:")
    enemy.map.show_for_enemy(player)

    print("Enter the position to attack.")
    position = input(expecting_answer)
    res, obj = player.attack(enemy, position)
    player.consequences(enemy, position, res, obj)

    print("It's your board:")
    player.map.show_for_user(player)
    print("It's your enemy's board:")
    enemy.map.show_for_enemy(player)


if __name__ == '__main__':

    print("------------BATTLESHIP GAME----------")
    print("------------STAGE 0: PREPARATION----------")
    print("Choose the mode:\n1. Playing against bot. (enter 0)\n2. Playing against another player. (enter 1)")
    while True:
        mode = input(expecting_answer)
        if int(mode) in {0, 1}:
            mode = int(mode)
            break
        else:
            print("You entered incorrect mode. Try again.")


    if mode == 0:
        raise NotImplementedError("Bot hasn't been implemented.")
    else:
        player1 = preparation()
        print(f"\nPlayer {player1.name}, it's your board: ")
        player1.map.show_for_user(player1)
        player2 = preparation()
        print(f"\nPlayer {player2.name}, it's your board: ")
        player2.map.show_for_user(player2)

    while True:
        i = 1
        print(f"\n------------STAGE {i}: THE GAME----------")
        i += 1

        attack(player1, player2)

        if player2.ships_amount == 0:
            print("------------THE GAME HAS ENDED----------")
            print(f"{player1.name}, congrats, you won!")
            break
        else:
            pass

        attack(player2, player1)

        if player1.ships_amount == 0:
            print("\n------------THE GAME HAS ENDED----------")
            print(f"{player2.name}, congrats, you won!")
            break
        else:
            pass
