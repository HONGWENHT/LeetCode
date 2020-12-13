from typing import List


class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.v = v
        self.row = 0
        self.col = 0

    def next(self) -> int:
        ret = self.v[self.row][self.col]
        self.col += 1
        if self.col == len(self.v[self.row]):
            self.row += 1
            self.col = 0
        return ret

    def hasNext(self) -> bool:
        if self.row >= len(self.v) :
            return False
        return True


s = Vector2D([[]])
s.hasNext()