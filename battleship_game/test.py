from classes import *

test_map = Map(9)

ship1 = Ship("a1", 0, 3)
test_map.add(ship1)
ship2 = Ship("b3", 1, 2)
test_map.add(ship2)

test_map._show()
test_map.show_for_user()
enemy = Player()
enemy.checked_squares.append((2, 1))
enemy.checked_squares.append((3, 1))
enemy.checked_squares.append((7, 7))
test_map.show_for_enemy(enemy)