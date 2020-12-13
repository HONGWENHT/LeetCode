import collections
from typing import List


class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.snake = collections.deque([(0, 0)])
        self.dirs = {'U': (1, 0), 'D': (-1, 0), 'R': (0, 1), 'L': (0, -1)}
        self.width = width
        self.height = height
        self.food_p = 0
        self.snake_set = set([(0, 0)])
        self.food = food

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        """
        new_row = self.snake[0][0] + self.dirs[direction][0]
        new_col = self.snake[0][1] + self.dirs[direction][1]

        if new_row < 0 or new_row >= self.height or new_col < 0 or new_col >= self.width:
            return -1

        if (new_row, new_col) in self.snake_set and new_row != self.snake[-1][0] and new_col != self.snake[-1][1]:
            return -1

        if self.food_p < len(self.food) and new_row == self.food[self.food_p][0] and new_col == self.food[self.food_p][
            1]:
            self.food_p += 1
        else:
            tail = self.snake.pop()
            self.snake_set.remove(tail)

        self.snake.appendleft((new_row, new_col))
        self.snake_set.add((new_row, new_col))

        return len(self.snake) - 1

# ["SnakeGame","move","move","move","move","move","move"]
# [[3,2,[[1,2],[0,1]]],["R"],["D"],["R"],["U"],["L"],["U"]]

s = SnakeGame(3, 2, [[1, 2], [0, 1]])
s.move("R")
s.move("D")
s.move("R")
s.move("U")
s.move("L")
s.move("U")