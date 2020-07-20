import numpy as np
import constants
#import keyboard

# TODO: implement storing block
# TODO: implement rotating blocks
# TODO: test/fix keyboard input when internet
# TODO: implement clearing lines, score system
class Tetris:
    def __init__(self, width=10, height=20):
        self.width = width
        self.height = height
        self.current_block = self._generate_block()
        self.blocks = []
        self.isFinished = False
        
        # 2D array where each square of the board is represented by a character
        # 4 top rows are not part of the screen
        self.board = np.full((height + 4, width), constants.EMPTY)

    def update(self):
        # Listen for input from user
        # perform action according to input (if no valid input, move 1 down)
        action = [None, 'down', 'left', 'right'][int(np.random.randint(4))]
        #action = self._get_action()
        self._perform_action(action)
    
    def _generate_block(self):
        block_type = "IJLOSTZ"[int(np.random.randint(7))]
        return Tetromino(block_type, self)

    #def _get_action(self):
     #   try:
      #      for action, keypress in constants.actions.items():
       #         if keyboard.is_pressed(keypress):
        #            return action
        #except:
         #   return None

    def _perform_action(self, action):
        self.current_block.update_coords(action)
        if not self.current_block.isActive:
            self.blocks.append(self.current_block)
            self._update_board(self.current_block)
            self.isFinished = max(map(lambda x: x[1], self.current_block.coords)) <= 4
            self.current_block = self._generate_block()
    
    def _update_board(self, block):
        for x, y in block.coords:
            self.board[y:y+1, x:x+1] = block.block_type

    def check_for_collision(self, coords):
        # Check if the inactive blocks collide with the given coordinates
        for coord in coords:
            for block in self.blocks:
                if coord in block.coords:
                    return True
        return False

    def __str__(self):
        board = self.board.copy()
        for x,y in self.current_block.coords:
            board[y:y+1, x:x+1] = self.current_block.block_type
        return str(board)+"\n"
    

class Tetromino:
    def __init__(self, block_type, game):
        self.block_type = block_type
        self.isActive = True
        self.game = game
        self.coords = self._initialize_coords(block_type)
    
    def _initialize_coords(self, block_type):
        middle = int(self.game.width/2)
        if block_type == constants.I_BLOCK:
            return [(middle - 1 + i, 0) for i in range(4)]
        if block_type == constants.J_BLOCK:
            return [(middle - 1 + i, 1) for i in range(3)] + [(middle - 1, 0)]
        if block_type == constants.L_BLOCK:
            return [(middle - 1 + i, 1) for i in range(3)] + [(middle + 1, 0)]
        if block_type == constants.O_BLOCK:
            return [(middle, i) for i in range(2)] + [(middle + 1, i) for i in range(2)]
        if block_type == constants.S_BLOCK:
            return [(middle, i) for i in range(2)] + [(middle - 1, 1), (middle + 1, 0)]
        if block_type == constants.T_BLOCK:
            return [(middle, i) for i in range(2)] + [(middle - 1, 1), (middle + 1, 1)]
        if block_type == constants.Z_BLOCK:
            return [(middle, i) for i in range(2)] + [(middle - 1, 0), (middle + 1, 1)]


    def update_coords(self, action):
        if action is None:
            if max(map(lambda x: x[1], self.coords)) < self.game.height + 4 - 1:
                self._attempt_update([(x[0], x[1] + 1) for x in self.coords])
            else:
                self.isActive = False
                return
        elif action == 'down':
            if max(map(lambda x: x[1], self.coords)) < self.game.height + 4 - 2:
                self._attempt_update([(x[0], x[1] + 2) for x in self.coords])
            else:
                self.update_coords(None)
        elif action == 'left':
            if min(map(lambda x: x[0], self.coords)) > 0:
                self._attempt_update([(x[0] - 1, x[1]) for x in self.coords])
        elif action == 'right':
            if max(map(lambda x: x[0], self.coords)) < self.game.width - 1:
                self._attempt_update([(x[0] + 1, x[1]) for x in self.coords])
        if self.game.check_for_collision(map(lambda x: (x[0], x[1] + 1), self.coords)):
            self.isActive = False
    
    def _attempt_update(self, new_coords):
        if not self.game.check_for_collision(new_coords):
            self.coords = new_coords