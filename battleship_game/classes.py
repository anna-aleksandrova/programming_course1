"""The module contains classes for the implementation of the
battleship game.

"""


from copy import deepcopy
import random

class Object:

    _id_counter = 1

    def __init__(self, position):
        """Initializes an <object> which is supposed to be placed on the board.

        Args:
            position (str or tuple): An upper-left square of the <object> body.
        """
        self.id = Object._id_counter
        Object._id_counter += 1
        self.position = Map.decode(position)
    
    def get_body(self):
        pass

    def get_area(self):
        pass
    

class Ship(Object):
    """An object which represents a ship.

    Attributes:
        id (int): An identifier of an object of class <Ship>.
        position (tuple): (i, j) for i-coordinate and j-coordinate of the upper-left square,
                            occupied by an <object>.
        orientation (int): 0 for horizontal orientation, 1 for vertical orientation. 
        size (int): Size of an object of class <Ship>.
        health (int): Defines how much area of a <Ship> is shot if there is any of this kind.
        shot (set): Contains shot points from the body.
    """

    def __init__(self, position, orientation, size):
        """Expected orientation: 0 for 'h' or 1 for 'v'.
        """
        Object.__init__(self, position)
        self.orientation = orientation
        self.size = size
        self.health = self.size
        self.shot = set()

    def get_body(self):
        """
        Returns:
            body (set): Contains tuples with points(squares), occupied by a <Ship>,
                            in the given coordinate system.
        """
        body = set()
        if self.orientation == 0:
            for j in range(self.size):
                body.add((self.position[0], self.position[1] + j))
        elif self.orientation == 1:
            for i in range(self.size):
                body.add((self.position[0] + i, self.position[1]))
        else:
            pass
        return body
    
    def get_area(self):
        """
        Returns:
            area (set): Contains tuples with points(squares), occupied by a <Ship>, and the points, which 
                            are located at the distance of 1 square (vertically, horizontally, diagonally)
                            in the given coordinate system.
        """
        area = self.get_body()
        aux = set()
        for point in area:
            i, j = point
            for delta_i, delta_j in [[-1, 0], [1, 0], [0, -1], [0, 1],
                                     [-1, 1], [-1, -1], [1, 1], [1, -1]]:
                next_i, next_j = i + delta_i, j + delta_j
                aux.add((next_i, next_j))
        return area | aux
    
    def is_destroyed(self):
        """
        Returns:
            message (int): 0 if capacity of <self.injured> is not equal to <self.size>.
                            1 if capacity of <self.injured> is equal to <self.size>.
        """
        if len(self.shot) != self.size:
            return 0
        else:
            return 1
    
    @classmethod
    def generate(cls, size):
        """Generates a <Ship> on the random position with the given <size>.

        Args:
            size (int): Size of <res_object>.

        Returns:
            res_object (cls): An object of class <cls>.
        """
        return cls((random.randrange(Map.size), random.randrange(Map.size)), random.randrange(2), size)
    
    def __repr__(self):
        return f"Ship(position={self.position}, orientation={self.orientation}, size={self.size})"

 
class Mine(Object):
    """An object which represents a mine.

    Attributes:
        position (tuple): (i, j) for i-coordinate and j-coordinate of the upper-left square,
                            occupied by an object of class <Mine>. 
        orientation (int): 0 for horizontal, 1 for vertical.
        size (int): Size of an object of class <Ship>.
        health (int): To avoid errors in method <consequqnces> of class <Player>.
        shot (set): Contains shot points from the body.
        id (int): An identifier of an object of class <Mine>.
    """

    def __init__(self, position, orientation, size):
        """As far as <size> might vary, orientation is included.
        """
        Object.__init__(self, position)
        self.orientation = orientation
        self.size = size
        self.shot = set()
        self.health = size

    def __repr__(self):
        return f"Mine(position={self.position}, orientation={self.orientation}, size={self.size})"
    
    @classmethod
    def generate(cls, size):
        """Generates a <Mine> at the random position with given characteristics
            of <size>.

        Args:
            orientation(int): 0 for horizontal, 1 for vertical.
            size (int): Size of the object of class <cls>.

        Returns:
            object (cls): An object of class <cls>.
        """
        return cls((random.randrange(Map.size), random.randrange(Map.size)), random.randrange(2), size)
    

    def get_body(self):
        """
        Returns:
            body (set): Contains tuples with points(squares), occupied by a <Mine>,
                            in the given coordinate system.
        """
        body = set()
        if self.orientation == 0:
            for j in range(self.size):
                body.add((self.position[0], self.position[1] + j))
        elif self.orientation == 1:
            for i in range(self.size):
                body.add((self.position[0] + i, self.position[1]))
        else:
            pass
        return body
    
    def get_area(self):
        """
        Returns:
            area (set): Contains tuples with points(squares), occupied by a <Mine>, and the points, which 
                            are located at the distance of 1 square (vertically, horizontally, diagonally)
                            in the given coordinate system.
        """
        area = self.get_body()
        aux = set()
        for point in area:
            i, j = point
            for delta_i, delta_j in [[-1, 0], [1, 0], [0, -1], [0, 1],
                                     [-1, 1], [-1, -1], [1, 1], [1, -1]]:
                next_i, next_j = i + delta_i, j + delta_j
                aux.add((next_i, next_j))
        return area | aux

class Map:
    """Initializes a map for the game.

    Attributes:
        size (int): Positive integer as size of an object of class <Map>.
        map (list): A matrix (list of lists) which represents the map with ships, mines, etc.
                        The objects are represeted as natural numbers (identifiers).
        objects (dict): Contains all objects which are placed on the board at any given moment;
                            (key, value) = (<object>'s identifier, <object>)
        occupied (set): Contains the points (as tuples (i, j)) which are occupied by objects. No other objects
                            can be placed here.
        prohibited (set): Contains the points (as tuples (i, j)) which are occupied by objects and the points near them
                            at the distance of 1 square in all possible ways. Only mines might be placed here.
                            A mine (object of class <Mine>) can be placed on the point from <prohibited> if and only if
                            it's not in <self.occupied>.
        around (set): Contains the points which are around destroyed ships.
    """
    
    size = None
    j_coordinates = None
    i_coordinates = None

    def __init__(self, size):
        self.size = size
        if Map.size is None:
            Map.size = size
            Map.j_coordinates, Map.i_coordinates = Map.coordinate_system()
        else:
            if size == Map.size:
                pass
            else:
                raise ValueError("In battleship game maps must have equal dimensions.")
        self.map = [[" " for _ in range(self.size)] for _ in range(self.size)]
        self.objects = {}
        self.occupied = set()
        self.prohibited = set()
        self.around = set()

    @classmethod
    def coordinate_system(cls):
        """Defines universal coordinate system, which will be applied to the
        map. Doesn't depend on the size of the board.

        Returns:
            first_to_j (dict): (<key>, <value>) = (j in the old system, j in the new system)
            second_to_i (dict): (<key>, <value>) = (i in the old system, i in the new system)
        """
        if cls.size <= 26:
            first_to_j = {chr(97 + i): i for i in range(cls.size)}
        else:
            first_to_j = {i + 1: i for i in range(cls.size)}
        second_to_i = {i + 1: i for i in range(cls.size)}
        return first_to_j, second_to_i
    
    
    @classmethod
    def check_tuple(cls, pivot_map, tpl):
        """Checks if there is a point on the map which can be defined by <tpl>.

        Args:
            pivot_map (Map): A current map of the game.
            tpl (tuple): A tuple to check.

        Returns:
            val (int): 1 if <tpl> defines a point on <self.map>.

        Raises:
            ValueError: if <tpl> doesn't define a point on <self.map>.
        """
        if len(tpl) != 2:
            raise ValueError(f"Tuple {tpl} can't define a point on a board: incorrect length")
        elif not (isinstance(tpl[0], int) and isinstance(tpl[1], int)):
            raise ValueError(f"Tuple {tpl} can't define a point on a board: it contains objects of incorrect type")
        elif not (0 <= tpl[0] <= pivot_map.size - 1 and 0 <= tpl[1] <= pivot_map.size - 1):
            raise ValueError(f"Tuple {tpl} can't define a point on a board: it contains incorrect values")
        else:
            return 1
        
    @classmethod
    def _check_point(cls, pivot_map, tpl):
        """Checks if there is a point on the map which can be defined by <tpl>.
            Returns a value, raises nothing.

            Args:
                pivot_map (Map): A current map of the game.
                tpl (tuple): A tuple to check.

            Returns:
                val (int): 1 if <tpl> defines a point on <self.map>, 0 otherwise.
        """
        if isinstance(pivot_map, Map):
            size = pivot_map.size
        elif isinstance(pivot_map, list):
            size = len(pivot_map)
        else:
            raise ValueError(f"Unsupported type is given as an argument: {type(pivot_map)}")
        if (len(tpl) != 2 or
             not (isinstance(tpl[0], int) and isinstance(tpl[1], int)) or
             not (0 <= tpl[0] <= size - 1 and 0 <= tpl[1] <= size - 1)):
                return 0
        else:
            return 1
        
    @classmethod
    def decode(cls, arg):
        """Decodes an arg with coordinates of an object (type: <Ship>, or <Mine>;
        something else is also possible in case of module development).

        Args:
            arg (str or tuple): An arg with coordinates of an object.
                                    Expected format: 1) str: "a_1" (<latin-script letter>_<number>) if size
                                    of the board <= 26, "1_1" (<number>_<number>) otherwise;
                                                     2) tuple: (i, j), where i is the first coordinate of the square,
                                                                j is the second coordinate of the square.
        Returns:
            i (int): The first coordinate of the square, encoded in <arg>.
            j (int): The second coordinate of the square, encoded in <arg>.

        Raises:
            ValueError: 1. If the arg (str) isn't in the format of <latin-script letter>_<number>
                            or <number>_<number>.
                        2. If the arg (tuple) is not of format (i, j)
        """
        if isinstance(arg, tuple):
            return arg[0], arg[1]          
        elif isinstance(arg, str):
            decode_first_symbol, decode_second_symbol = cls.coordinate_system()
            arg = arg.split("_")
            if cls.size <= 26:
                pass
            else:
                arg[0] = int(arg[0])
            if not (arg[0] in decode_first_symbol.keys() and int(arg[1]) in decode_second_symbol.keys()):
                raise ValueError("Wrong format of square or such a square does not exist. Try again.")
            else:
                i = decode_second_symbol[int(arg[1])]
                j = decode_first_symbol[arg[0]]
                return i, j
        else:
            return ValueError(f"Can't decode from object of type {arg}")
    
    def add_ship(self, ship):
        """Places a <ship> on the board, if it's possible, thus modifies <self.map>, <self.objects>,
            <self.occupied>, <self.prohibited>.

        Args:
            ship (Ship): An object which might be placed on the <self.map>.

        Raises:
            ValueError: 1. There is at least one point <(i, j)> in ship.get_body() which
                            is not defined on the board.
                        2. There is at least one point <(i, j)> in ship.get_body() which
                            can't be placed on the board.
        """
        for point in ship.get_body():
            if point in self.occupied:
                raise ValueError(f"An object of {type(ship)} can't be placed on the map: attempt to place on the occupied square.")
            elif point in self.prohibited:
                raise ValueError(f"An object of {type(ship)} can't be placed on the map: attempt to place on the prohibited square.")
            elif not Map._check_point(self.map, point):
                raise ValueError(f"An object contains the point {point} which is not defined on the board.")
            else:
                pass
        for point in ship.get_body():
            i, j = point
            self.map[i][j] = ship.id
        self.objects[ship.id] = ship
        self.occupied = self.occupied | ship.get_body()
        for point in ship.get_area():
            if Map._check_point(self, point):
                self.prohibited.add(point)
            else:
                pass

    def add_mine(self, mine):
        """Places a <mine> on the board, if it's possible, thus modifies <self.map>, <self.objects>,
            <self.occupied>, <self.prohibited>.

        Args:
            mine (Mine): An object which might be placed on the <self.map>.

        Raises:
            ValueError: 1. There is at least one point <(i, j)> in mine.get_body() which
                            is not defined on the board.
                        2. There is at least one point <(i, j)> in mine.get_body() which
                            can't be placed on the board.
        """
        for point in mine.get_body():
            if point in self.occupied:
                raise ValueError(f"An object of {type(mine)} can't be placed on the map: attempt to place on the occupied square.")
            elif not Map._check_point(self.map, point):
                raise ValueError(f"An object contains the point {point} which is not defined on the board.")
            else:
                pass
        for point in mine.get_body():
            i, j = point
            self.map[i][j] = mine.id
        self.objects[mine.id] = mine
        self.occupied = self.occupied | mine.get_body()
        for point in mine.get_area():
            if Map._check_point(self, point):
                self.prohibited.add(point)
            else:
                pass
    
    def _show(self):
        """Displays a <self.map> as a game map. Contains identifiers of <objects>.
        """
        j = [chr(97+i) for i in range(self.size)]
        print("")
        print(" "*27, *j)
        for k in range(len(self.map)):
            print(" "*25, f"{k+1}", *self.map[k])

    def show_for_user(self, user):
        """Displays a <self.map> as a game map for the user (object of <Player>). Marks ships 
            as "X", mines as "O", shot squares as "S", destroyed objects as "*". If they pointed 
            at a mine on the enemy's board, the appropriate squares will be marked as "*" if 
            they were empty, caught ships will be shot or destroyed (depends on the power of mine),
            caught mines of <self> (user) will be revealed.
        
        Args:
            user (Player): Their board will be displayed.
        """
        for_user_map = deepcopy(self.map)
        for i in range(len(for_user_map)):
            for j in range(len(for_user_map)):
                if (i, j) in user.shot_mines or (i, j) in user.shot_mines_around:
                    for_user_map[i][j] = "*"
                elif (i, j) in self.around:
                    for_user_map[i][j] = "#"
                elif for_user_map[i][j] not in self.objects.keys():
                    pass
                elif isinstance(self.objects[for_user_map[i][j]], Ship):
                    ship = self.objects[for_user_map[i][j]]
                    if ship.is_destroyed():
                        for_user_map[i][j] = "*"
                    elif (i, j) in ship.shot:
                        for_user_map[i][j] = "S"
                    else:
                        for_user_map[i][j] = "X"
                elif isinstance(self.objects[for_user_map[i][j]], Mine):
                    mine = self.objects[for_user_map[i][j]]
                    if mine.shot == set():
                        for_user_map[i][j] = "O"
                    else:
                        for_user_map[i][j] = "*"
                else:
                    pass
        j = [chr(97+i) for i in range(len(for_user_map))]
        print("")
        print(" "*27, *j)
        for k in range(len(for_user_map)):
            print(" "*25, f"{k+1}", *for_user_map[k])
    
    def show_for_enemy(self, enemy):
        """Displays a <self.map> for the enemy (object of class <Player>). Marks everything
            as "~" at the start of the game. 
            
        If the enemy shots a <Ship>, then the appropriate square is marked as <S> (for shot). 
        If the enemy destroys a <Ship>, then the appropriate squares are marked as <*>. 
        If the enemy shots a <Mine>, then the appropriate square is marked as <M> (for mine).
        If the enemy misses, then the appropriate square is marked as <#>.
        """
        for_enemy_map = deepcopy(self.map)
        for i in range(len(for_enemy_map)):
            for j in range(len(for_enemy_map)):
                if (i, j) not in enemy.checked_squares or (i, j) in enemy.shot_mines_around:
                    for_enemy_map[i][j] = "~"
                else:
                    if for_enemy_map[i][j] == " ":
                        for_enemy_map[i][j] = "#"
                    elif for_enemy_map[i][j] in self.objects.keys():
                        if isinstance(self.objects[for_enemy_map[i][j]], Ship) and self.objects[for_enemy_map[i][j]].health != 0:
                            for_enemy_map[i][j] = "S"
                        elif isinstance(self.objects[for_enemy_map[i][j]], Ship) and self.objects[for_enemy_map[i][j]].health == 0:
                            for_enemy_map[i][j] = "*"
                        elif isinstance(self.objects[for_enemy_map[i][j]], Mine):
                            for_enemy_map[i][j] = "M"
                        else:
                            raise NotImplementedError("Maybe some new objects were declared in the game rules.")
                    else:
                        raise NotImplementedError("Maybe some new objects were declared in the game rules.")
        j = [chr(97+i) for i in range(len(for_enemy_map))]
        print("")
        print("                      ", *j)
        for k in range(len(for_enemy_map)):
            print("                    ", f"{k+1}", *for_enemy_map[k])

    @classmethod
    def generate(cls, board_size, ships, mines, max_tries = 100):
        """Generates an object of class <cls> which contains
            objects from <ships> and <mines>.
        
        Args:
            board_size (int): A size of the generated object.
            ships (dict): (key, value) = (size, amount): <amount> ships of <size> must be placed.
            mines (dict): (key, value) = (size, amount): <amount> mines of <size> must be placed.
        
        Returns:
            res_map (cls): A map of class <cls>.
        """
        res_map = cls(board_size)
        for size, amount in ships.items():
            for i in range(amount):
                for _ in range(max_tries):
                    ship = Ship.generate(size)
                    try:
                        res_map.add_ship(ship)
                        break
                    except ValueError or NotImplementedError:
                        Object._id_counter -= 1
                        continue
                else:
                    return ValueError("Map generation failed.")
        for size, amount in mines.items():
            for i in range(amount):
                for _ in range(max_tries):
                    mine = Mine.generate(size)
                    try:
                        res_map.add_mine(mine)
                        break
                    except ValueError or NotImplementedError:
                            Object._id_counter -= 1
                            continue
                else:
                    return ValueError("Map generation failed.")
        return res_map

    @classmethod
    def input_ships(cls, pivot_map, ships, ships_amount, user):
        """For placing ships on the <pivot_map>.

        Args:
            pivot_map (Map): A map to place the <ships> on.
            user (Player): On their board ships will be placed.
            ships (dict): (key, value) = (size, amount): <amount> ships of <size> must be placed.
            ships_amount (int): Total amount of all ships, which were entered by the <user>.
        """
        while ships_amount:
            print("You have got such ships to enter: ")
            for size, amount in ships.items():
                if amount == 0:
                    pass
                elif amount == 1:
                    print(f"{amount} ship of size {size}")
                else:
                    print(f"{amount} ships of size {size}")
            while True:
                size = input("Enter the size: ")
                if not size.isnumeric() or int(size) not in ships.keys() or ships[int(size)] == 0:
                    print("Incorrect size. Try again.")
                else:
                    size = int(size)
                    break
            while True:
                orientation = input("Enter the orientation (0 for horizontal, 1 for vertical): ")
                if not orientation.isnumeric() or int(orientation) not in {0, 1}:
                    print("Incorrect orientation. Try again.")
                else:
                    orientation = int(orientation)
                    break
            while True:
                position = input("Enter the upper-left square which will be occupied by a ship (expected format: e_7): ")
                if pivot_map.size > 26:
                    j, i = map(int, position.split("_"))
                else:
                    j, i = position.split("_")
                    i = int(i)
                if not (j in Map.j_coordinates.keys() and i in Map.i_coordinates.keys()):
                    print("Incorrect position. Try again.")
                else:
                    break
            ship = Ship(position, orientation, size)
            try:
                pivot_map.add_ship(ship)
                ships[size] -= 1
                ships_amount -= 1
                pivot_map.show_for_user(user)
            except ValueError:
                Object._id_counter -= 1
                print(f"Adding of {ship} failed. Try again.")

    @classmethod
    def input_mines(cls, pivot_map, mines, mines_amount, user):
        """For placing ships on the <pivot_map>.

        Args:
            pivot_map (Map): A map to place the <ships> on.
            user (Player): On their board mines will be placed.
            mines (dict): (key, value) = (size, amount): <amount> mines of <size> must be placed.
            mines_amount (int): Total amount of all mines, which were entered by <user>.
        """
        while mines_amount:
            print("You have got such mines to enter: ")
            for size, amount in mines.items():
                if amount == 0:
                    pass
                elif amount == 1:
                    print(f"{amount} mine of size {size}")
                else:
                    print(f"{amount} mines of size {size}")
            while True:
                size = input("Enter the size: ")
                if not size.isnumeric() or int(size) not in mines.keys() or mines[int(size)] == 0:
                    print("Incorrect size. Try again.")
                else:
                    size = int(size)
                    break
            while True:
                orientation = input("Enter the orientation (0 for horizontal, 1 for vertical): ")
                if not orientation.isnumeric() or int(orientation) not in {0, 1}:
                    print("Incorrect orientation. Try again.")
                else:
                    orientation = int(orientation)
                    break
            while True:
                position = input("Enter the upper-left square which will be occupied by a mine (expected format: e_7): ")
                if pivot_map.size > 26:
                    j, i = map(int, position.split("_"))
                else:
                    j, i = position.split("_")
                    i = int(i)
                if not (j in Map.j_coordinates.keys() and i in Map.i_coordinates.keys()):
                    print("Incorrect position. Try again.")
                else:
                    break
            mine = Mine(position, orientation, size)
            try:
                pivot_map.add_mine(mine)
                mines[size] -= 1
                mines_amount -= 1
                pivot_map.show_for_user(user)
            except ValueError:
                Object._id_counter -= 1
                print(f"Adding of {mine} failed. Try again.")
                
    @classmethod
    def user_input(cls, board_size, ships, ships_amount, mines, mines_amount, user):
        """For inputting a map (or an object of inheritant of <Map>) by a player.

        Args:
            size (int): The size of the map.

        Returns:
            res_map (cls): an object of class <cls>.
        """
        res_map = Map(board_size)
        Map.input_ships(res_map, ships, ships_amount, user)
        Map.input_mines(res_map, mines, mines_amount, user)
        return res_map


class Player:
    """Initializes an object which represents a player.

    Attributes:
        name (str): A name of a player.
        board_size (int): The size of the board of <self>.
        board_choice (int): The choice how to create a board (0 for entering, 1 for generating).
        ships (dict): Contains configuration of ships: (key, value) = (size, amount).
        ships_amount (int): Total amount of ships on the board of <self>.
        mines (dict): Contains configuration of mines: (key, value) = (size, amount).
        mines_amount (int): Total amount of mines on the board of <self>.
        checked_squares (set): A set of squares on the board of <self>'s 
                                enemy which have been checked by <self>.
        shot_mines (set): A set of points which are the coordinates of mines on 
                            the enemy's map, which were shot by <self>.
        shot_mines_around (set): A set of points which are the coordinates of squares
                                    located around mines on the enemy's map, which were shot by <self>.
        map (Map): A map of <self>.
    """
    
    def __init__(self, name, board_size, board_choice, ships, mines):
        """Initializes an instance of class <Player>.

        Args:
            name (str): A name of a player.
            board_size (int): A size of the board of <self>.
            board_choice (int): 0 for entering the board, 1 for generating the board of <self>.
            ships(tuple): ships[0] is a dictionary, where (key, value) = (size, amount):
                            <amount> ships of <size> must be placed.
                            ships[1] is an integer, which defines the total amount of ships.
            mines (tuple): mines[0] is a dictionary, where (key, value) = (size, amount):
                            <amount> mines of <size> must be placed.
                            mines[1] is an integer, which defines the total amount of ships.
        """
        self.name = name
        self.board_size = board_size
        self.board_choice = board_choice
        self.ships = ships[0]
        self.ships_amount = ships[1]
        self.mines = mines[0]
        self.mines_amount = mines[1]
        self.checked_squares = set()
        self.shot_mines = set()
        self.shot_mines_around = set()
        if self.board_choice == 0:
            self.map = Map.user_input(self.board_size, self.ships, self.ships_amount, self.mines, self.mines_amount, self)
        elif self.board_choice == 1:
            self.map = Map.generate(self.board_size, self.ships, self.mines)
        else:
            raise ValueError(f"Can't create a player: wrong value of <board_choice>. Expected: 0 or 1, got: {board_choice}")
        
    
    def __repr__(self):
        return f"Player(name={self.name}, board_size={self.board_size}, board_choice={self.board_choice}, ships = {self.ships}, mines = {self.mines})"
    
    
    ATTACK_ANSWER = {
        0: "Miss",
        1: "Mine",
        2: "Shot",
        3: "Destroyed"
        }
    
    def attack(self, other, position):
        """Starts an attack on <position> of <other> (object of class <Player>).

        Args:
            other (Player): The enemy.
            position (str): A square to attack.
        
        Returns:
            message (int): Encoded result of the attack (0, 1, 2 or 3).

        """        
        point = Map.decode(position)
        if point in self.checked_squares:
            raise ValueError(f"You've already checked this square: square {position}")
        else:
            if other.map.map[point[0]][point[1]] == " ":
                print(Player.ATTACK_ANSWER[0])
                return 0, None
            else:
                obj = other.map.objects[other.map.map[point[0]][point[1]]]
                if isinstance(obj, Mine):
                    print(Player.ATTACK_ANSWER[1])
                    return 1, obj
                elif isinstance(obj, Ship) and obj.health == 1:
                    print(Player.ATTACK_ANSWER[3])
                    return 3, obj
                elif isinstance(obj, Ship) and obj.health != 1:
                    print(Player.ATTACK_ANSWER[2])
                    return 2, obj
                else:
                    raise NotImplementedError("Maybe new objects were added.")
    
    def consequences(self, other, position, res, obj):
        """Changes boards and objects after attack.

        Args:
            other (Player): They were attacked.
            position (str): The position on <other>'s board which was attacked.
            res (int): Result of the attack.
            obj (<Object>'s inheritant): An object which was under attack.
        """
        point = Map.decode(position)
        if res == 0:
            self.checked_squares.add(point)
        elif res == 1:
            self.checked_squares = self.checked_squares | obj.get_body()
            self.shot_mines = self.shot_mines | obj.get_body()
            self.shot_mines_around = self.shot_mines_around | (obj.get_area() - obj.get_body())
            obj.shot.add(point)
            delete = set()
            for point in self.shot_mines | self.shot_mines_around:
                try:
                    if self.map.map[point[0]][point[1]] in self.map.objects.keys():
                        self.map.objects[self.map.map[point[0]][point[1]]].shot.add(point)
                        self.map.objects[self.map.map[point[0]][point[1]]].health -= 1
                        if (isinstance(self.map.objects[self.map.map[point[0]][point[1]]], Ship) and
                            self.map.objects[self.map.map[point[0]][point[1]]].health == 0):
                            self.ships_amount -= 1
                        else:
                            pass
                        other.checked_squares.add(point)
                        delete.add(point)
                    else:
                        other.checked_squares.add(point)
                        pass
                except IndexError:
                    continue
            self.shot_mines = self.shot_mines - delete
            self.shot_mines_around = self.shot_mines_around - delete
        elif res == 2:
            self.checked_squares.add(point)
            obj.health -= 1
            obj.shot.add(point)
        elif res == 3:
            shot = obj.get_area()
            self.checked_squares = self.checked_squares | shot
            obj.health -= 1
            obj.shot.add(point)
            other.ships_amount -= 1
            other.map.around = other.map.around | (shot - obj.get_body())
        else:
            raise NotImplementedError()
