"""A collection of function for doing my project."""
import random
import string

from time import sleep
from IPython.display import clear_output

class Animal():
    """
    Basic class definition of animal with attributes to be inherited.
    This method is based off of the Bot() class from A4, Artificial Agents

    Attributes
    ----------
    character: int, optional
        the symbol of the animal to be drawn on a grid
    position: list, optional
        the current coordinates of the animal on a grid
    moves: list, optional
        the possible changes in coordinates this animal can take
    grid_size: int, determined
        the size of the (square) grid the animal will be in
    draw: boolean, determined
        whether or not this animal should be drawn on the board

    """
    def __init__(self, character = 8982, position = [0, 0], moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]):
        self.character = chr(character)
        self.position = position
        self.moves = moves
        self.grid_size = None
        self.draw = True

class Butterfly(Animal):
    """
    A butterfly class, inheriting the Animal class

    Attributes
    ----------
    character: int, optional
        the symbol of the butterfly to be drawn on a grid
    position: list, optional
        the current coordinates of the butterfly on a grid
    moves: list, optional
        the possible changes in coordinates this butterfly can take
    down: boolean, determined
        whether or not this butterfly is going toward the bottom of the grid

    """
    def __init__(self, character = 861, position = [0, 3], moves = [[1, 0], [-1, 0]]):
        super().__init__(character, position, moves)
        self.down = True
    def fly(self):
        """
        Changes the butterfly's position based on its current direction.
        Note: the butterfly moves vertically only, in a single column.
    
        Returns
        ----------
        new_pos: list
            the new coordinates of the butterfly
        """
        has_new_pos = False
        while (not has_new_pos):
            if (self.down):
                new_pos = add_lists(self.moves[0], self.position)
            else:
                new_pos = add_lists(self.moves[1], self.position)
            if (not check_bounds(new_pos, self.grid_size)): # if the butterfly has reached the edge of the grid, change dir
                self.down = not self.down
            else:
                has_new_pos = True
        return new_pos
    def move(self):
        """
        Changes the butterfly's position into its new coordinates returned by the fly() method.
        """
        self.position = self.fly()
        
class Bird(Animal):
    """
    A bird class, inheriting the Animal class

    Attributes
    ----------
    character: int, optional
        the symbol of the bird to be drawn on a grid
    position: list, optional
        the current coordinates of the bird on a grid
    moves: list, optional
        the possible changes in coordinates this bird can take
    right: boolean, determined
        whether or not this bird is going toward the bottom of the grid

    """
    def __init__(self, character = 670, position = [3, 0], moves = [[0, 1], [0, -1]]):
        super().__init__(character, position, moves)
        self.right = True
    def flap(self):
        """
        Changes the bird's position based on its current direction.
        Note: the bird moves horizontally only, in a single row.
    
        Returns
        ----------
        new_pos: list
            the new coordinates of the bird
        """
        has_new_pos = False
        while (not has_new_pos):
            if (self.right):
                new_pos = add_lists(self.moves[0], self.position)
            else:
                new_pos = add_lists(self.moves[1], self.position)
            if (not check_bounds(new_pos, self.grid_size)):
                self.right = not self.right
            else:
                has_new_pos = True
        return new_pos
    def move(self):
        """
        Changes the bird's position into its new coordinates returned by the flap() method.
        """
        self.position = self.flap()

class Snake(Animal):
    """
    A snake class, inheriting the Animal class

    Attributes
    ----------
    character: int, optional
        the symbol of the snake to be drawn on a grid
    position: list, optional
        the current coordinates of the snake on a grid
    moves: list, optional
        the possible changes in coordinates this snake can take
    right: boolean, determined
        whether or not this snake is going toward the right of the grid
    up: boolean, determined
        whether or not this snake is going toward the top of the grid

    """
    def __init__(self, character = int('06AF', 16), position = [4, 0], moves = [[-1, 1], [1, 1], [-1, -1], [1, -1]]):
        super().__init__(character, position, moves)
        self.right = True;
        self.up = True;
    def slither(self):
        """
        Changes the snake's position based on its current direction.
        Note: the snake moves diagonally in a zigzag pattern across two rows.
    
        Returns
        ----------
        new_pos: list
            the new coordinates of the snake
        """
        has_new_pos = False
        while (not has_new_pos):
            if (self.right and self.up):
                new_pos = add_lists(self.moves[0], self.position)
            elif (self.right):
                new_pos = add_lists(self.moves[1], self.position)
            elif (not self.right and self.up):
                new_pos = add_lists(self.moves[2], self.position)
            else:
                new_pos = add_lists(self.moves[3], self.position)
            self.up = not self.up
            if (not check_bounds(new_pos, self.grid_size)):
                self.right = not self.right
                self.up = not self.up
            else:
                has_new_pos = True
        return new_pos
    def move(self):
        """
        Changes the snake's position into its new coordinates returned by the slither() method.
        """
        self.position = self.slither()

def add_lists(list1, list2):
    """
    Add corresponding values of two lists together. The lists should have the same number of elements.
    
    Parameters
    ----------
    list1: list
        the first list to add
    list2: list
        the second list to add
        
    Return
    ----------
    output: list
        a new list containing the sum of the given lists
    """
    output = []
    for it1, it2 in zip(list1, list2):
        output.append(it1 + it2)
    return output

def check_bounds(position, size):
    """
    Checks whether a coordinate is within the indices of a grid.
    
    Parameters
    ----------
    position: list
        the coordinate to check for within the grid
    size: int
        the size of the grid to compare the coordinate values to
    
    Return
    ----------
    boolean:
        True if the coordinate is within the grid, false if otherwise
    """
    for elem in position:
        if elem < 0 or elem >= size:
            return False
    return True

def play_board(animals, n_iter=25, grid_size=5, sleep_time=0.3):
    """Run a bot across a board.
    Most of this method is taken from A4, Artificial agents, including the rest of this comment.
    The most notably unique section of this method are lines 128-146, which implements the "eating" feature.
    
    Parameters
    ----------
    animals : Animal() type or list of Animal() type
        One or more animals to be be played on the board
    n_iter : int, optional
        Number of turns to play on the board. default = 25
    grid_size : int, optional
        Board size. default = 5
    sleep_time : float, optional
        Amount of time to pause between turns. default = 0.3.
    """
    # Constant values to check the grid for which animal currently is in that space
    BUTTERFLY_CHAR = chr(861)
    BIRD_CHAR = chr(670)
    SNAKE_CHAR = chr(int('06AF', 16))
    
    # If input is a single animal, put it in a list so that procedures work
    if not isinstance(animals, list):
        animals = [animals]
    
    # Update each bot to know about the grid_size they are on
    for animal in animals:
        animal.grid_size = grid_size

    for it in range(n_iter):

        # Create the grid
        grid_list = [['.'] * grid_size for ncols in range(grid_size)]
        
        # Add bot(s) to the grid
        for animal in animals:
            # Begin "eating" implementation
            if (grid_list[animal.position[0]][animal.position[1]] != '.'): # Check if an animal is already in this grid pos
                if (isinstance(animal, Butterfly)): # If it is a butterfly, it should be eaten by a bird
                    if (grid_list[animal.position[0]][animal.position[1]] == BIRD_CHAR):
                        animal.draw = False
                elif (isinstance(animal, Bird)): # If it is a bird, it should be eaten by a snake/eat a butterfly
                    if (grid_list[animal.position[0]][animal.position[1]] == BUTTERFLY_CHAR):
                        for temp in animals:
                            if (isinstance(temp, Butterfly) and temp.position == animal.position):
                                temp.draw = False
                    elif (grid_list[animal.position[0]][animal.position[1]] == SNAKE_CHAR):
                        animal.draw = False
                elif (isinstance(animal, Snake)): # If it is a snake, it should eat a bird
                    if (grid_list[animal.position[0]][animal.position[1]] == BIRD_CHAR):
                        for temp in animals:
                            if (isinstance(temp, Bird) and temp.position == animal.position):
                                temp.draw = False
            # "Draw" the animal on the grid only if it has not been eaten
            if (animal.draw == True):
                grid_list[animal.position[0]][animal.position[1]] = animal.character    

        # Clear the previous iteration, print the new grid (as a string), and wait
        clear_output(True)
        print('\n'.join([' '.join(lst) for lst in grid_list]))
        sleep(sleep_time)

        # Update bot position(s) for next turn
        for animal in animals:
            animal.move()