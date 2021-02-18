from __future__ import annotations
import numpy as np

HEIGHT = 20
WIDTH = 10


class TetrisBoard:
    def __init__(self) -> None:
        self.grid = [
            [Cell(row, col) for col in range(1, WIDTH + 1)]
            for row in range(1, HEIGHT + 1)
        ]

    def get_cell(self, row: int, col: int) -> Cell:
        if row not in range(1, HEIGHT + 1) or col not in range(1, WIDTH + 1):
            raise IndexError(
                f"Attempted to get cell for invalid coordinates ({row}, {col})"
            )

        return self.grid[row][col]

    def __repr__(self) -> str:
        return "\n".join([str(row) for row in self.grid])


class Cell:
    def __init__(self, row: int, column: int) -> None:
        self.row = row
        self.column = column
        self.occupied = False

    def set_occupied(self, occupied: bool) -> None:
        self.occupied = occupied

    def __repr__(self) -> str:
        return "X" if self.occupied else "-"


board = TetrisBoard()
board.get_cell(1, 1).set_occupied(True)
board.get_cell(5, 7).set_occupied(True)
print(board)