"""Test for my functions.

Tests how the Butterfly() class acts when its methods (fly, move) are called and its position changes. Also runs
an experiment grid with a standard butterfly.
"""

from functions import Animal, Butterfly, Bird, Snake, add_lists, check_bounds, play_board

##
##

def test_bots():
    assert Butterfly
    butterfly = Butterfly()
    assert butterfly
    assert isinstance(butterfly, Butterfly)
    
    assert butterfly.position == [0,3]
    assert butterfly.down == True
    butterfly.grid_size = 5
    assert isinstance(butterfly.fly(), list)
    butterfly.move()
    assert butterfly.position != [0,3]
    assert butterfly.down == True

    animal = Butterfly()
    play_board(animal, grid_size=5)