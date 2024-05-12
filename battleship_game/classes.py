"""The module contains classes for the implementation of the
battleship game.

"""
    
from copy import deepcopy

class Object:

    _id_counter = 0

    def __init__(self, position):
        """Initializes an <object> which is supposed to be placed on the board.

        Args:
            position (str): An upper-left square of the <object> body.
        """
        self.id = Object._id_counter + 1
        self.position = Map.encode(position)
    
    def get_body(self):
        pass

    def get_area(self):
        pass
    

class Ship(Object):
    """An object in the game.

    Attributes:
        id_counter (int): An identifier of an object of class <Ship>.
        position (tuple): (i, j) for i-coordinate and j-coordinate of the upper-left square,
                            occupied by an <object>.
        orientation (int): 0 for horizontal orientation, 1 for vertical orientation. 
        size (int): Size of an object of class <Ship>.
        health (int): Defines how much area of a <Ship> is shot if there is any of this kind.
    """

    def __init__(self, position, orientation, size):
        """Expected orientation: 0 for 'h' or 1 for 'v'.
        """
        Object.__init__(self, position)
        self.orientation = orientation
        self.size = size
        self.health = self.size
        self.id = Object._id_counter
        Object._id_counter += 1

    def get_body(self):
        """
        Returns:
            body (list): Contains tuples with points(squares), occupied by a <Ship>,
                            in the given coordinate system.
        """
        body = []
        if self.orientation == 0:
            for j in range(self.size):
                body.append((self.position[0], self.position[1] + j))
        elif self.orientation == 1:
            for i in range(self.size):
                body.append((self.position[0] + i, self.position[1]))
        else:
            pass
        return body
    
    def get_area(self):
        """
        Returns:
            area (list): Contains tuples with points(squares), occupied by a <Ship>, and the points, which 
                            are located at the distance of 1 square (vertically, horizontally, diagonally)
                            in the given coordinate system.
        """
        area = self.get_body()
        aux = []
        for point in area:
            i, j = point
            for delta_i, delta_j in [[-1, 0], [1, 0], [0, -1], [0, 1],
                                     [-1, 1], [-1, -1], [1, 1], [1, -1]]:
                next_i, next_j = i + delta_i, j + delta_j
                aux.append((next_i, next_j))
        return area + aux
    
class Mine(Object):
    pass

class Map:
    """Initializes a map for the game.

    Attributes:
        size (int): Positive integer as size of an object of class <Map>.
        map (list): A matrix (list of lists) which represents the map with visible ships, mines, etc.
                      Visible for the owner (<Player>), not visible for <Player>'s enemy.
        objects (dict): Contains all objects which have been placed on the board by this moment;
                            (key, value) = (<object>'s identifier, <object>)
        occupied (list): Contains the points (as tuples (i, j)) which are occupied by objects. No other objects
                            can be placed here.
        prohibited (list): Contains the points (as tuples (i, j)) which are occupied by objects and the points near them
                            at the distance of 1 square in all possible ways. Only mines might be placed here.
                            A mine (object of class <Mine>) can be placed on the point from <prohibited> if and only if
                            it's not in <self.occupied>.
    """
    map_symbols = {
        Mine: "O",
        Ship: "X"
    }

    fog_symbols = {
        ...
    }
    
    size = None

    def __init__(self, size):
        self.size = size
        if Map.size is None:
            Map.size = size
        else:
            if size == Map.size:
                pass
            else:
                raise ValueError("In battleship game maps must have equal dimensions.")
        self.map = [[" " for _ in range(self.size)] for _ in range(self.size)]
        self.fogmap = deepcopy(self.map)
        self.objects = {}
        self.occupied = []
        self.prohibited = []

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
    def encode(cls, string):
        """Encodes a string with coordinates of an object (type: <Ship>, or <Mine>;
        something else is also possible in case of module development).

        Args:
            string (str): A string with coordinates of an object.
                            Expected format: "a1" (<latin-script letter><number>) if size
                            of the board <= 26, "11" (<number><number>) otherwise.
        Returns:
            i (int): The first coordinate of the square, encoded in <string>.
            j (int): The second coordinate of the square, encoded in <string>.

        Raises:
            ValueError: If the string isn't in the format of <latin-script letter><number>
                          or <number><number>.
        """
        encode_first_symbol, encode_second_symbol = cls.coordinate_system()
        string = string.strip()
        if not (string[0] in encode_first_symbol.keys() and int(string[1]) in encode_second_symbol.keys()):
            raise ValueError("Wrong format of square or such a square does not exist. Try again.")
        else:
            i = encode_second_symbol[int(string[1])]
            if Map.size <= 26:
                j = encode_first_symbol[string[0]]
            else:
                j = encode_first_symbol[int(string[0])]
            return i, j
        
    def add(self, object):
        """Places an <object> on the board, if it's possible, thus modifies <self.map>, <self.objects>,
            <self.occupied>, <self.prohibited>.

        Args:
            object (<Object>'s inheritant): An object which might be placed on the <self.map>.

        Raises:
            ValueError: 1. There is at least one point <(i, j)> in object.get_body() which
                            is not defined on the board.
                        2. There is at least one point <(i, j)> in object.get_body() which
                            can't be placed on the board.
        """
        for point in object.get_body():
            if point in self.occupied:
                raise ValueError(f"An object of {type(object)} can't be placed on the map: attempt to place on the occupied square.")
            elif point in self.prohibited and isinstance(object, Ship):
                raise ValueError(f"An object of {type(object)} can't be placed on the map: attempt to place on the prohibited square.")
            elif point in self.prohibited and isinstance(object, Mine):
                pass
            elif point in self.prohibited:
                raise NotImplementedError()
            elif not (0 <= point[0] <= self.size - 1 and 0 <= point[1] <= self.size - 1):
                raise ValueError(f"An object contains the point {point} which is not defined on the board.")
            else:
                pass
        for point in object.get_body():
            i, j = point
            self.map[i][j] = object._id_counter
        self.objects[object.id + 1] = object
        self.occupied += object.get_body()
        for point in object.get_area():
            if point not in self.prohibited and (0 <= point[0] <= self.size - 1 and 0 <= point[1] <= self.size - 1):
                self.prohibited.append(point)
            else:
                pass
    
    def _show(self):
        """Displays a <self.map> as a game map. Contains identifiers of <objects>.
        """
        j = [chr(97+i) for i in range(self.size)]
        print("")
        print("                      ", *j)
        for k in range(len(self.map)):
            print("                    ", f"{k+1}", *self.map[k])


    def show_for_user(self):
        """Displays a <self.map> as a game map for the user (object of <Player>). Marks ships 
            as "X", mines as "O", shot squares as "*".
        """
        for_user_map = deepcopy(self.map)
        for i in range(self.size):
            for j in range(self.size):
                if for_user_map[i][j] not in self.objects.keys():
                    pass
                elif isinstance(self.objects[for_user_map[i][j]], Ship):
                    for_user_map[i][j] = "X"
                elif isinstance(self.objects[for_user_map[i][j]], Mine):
                    for_user_map[i][j] = "O"
                else:
                    pass
        j = [chr(97+i) for i in range(len(for_user_map))]
        print("")
        print("                      ", *j)
        for k in range(len(for_user_map)):
            print("                    ", f"{k+1}", *for_user_map[k])
    
    def show_for_enemy(self, enemy):
        """Displays a <self.map> as a game map for the enemy (object of <Player>). Marks everything
            as "~" at the start of the game. 
            
        If the enemy shots a <Ship>, then the appropriate square is marked as <S> (for shot). 
        If the enemy destroys a <Ship>, then the appropriate squares are marked as <*>. 
        If the enemy shots a <Mine>, then the appropriate square is marked as <M> (for mine).
        If the enemy misses, then the appropriate square is marked as <#>.
        """
        for_enemy_map = deepcopy(self.map)
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) not in enemy.checked_squares:
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


class Player:
    
    def __init__(self):
        self.checked_squares = []
    
    def attack(self, position):
        point = Map.encode(position)
        if point in self.checked_squares:
            raise ValueError(f"You've already checked this square: square {position}")
        else:
            self.checked_squares.append(point)

