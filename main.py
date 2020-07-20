import time
from tetris import Tetris

def main():
    game = Tetris(width=10, height=12)

    while not game.isFinished:
        # One game update
        game.update()
        print(game)
        time.sleep(0.2)
    # Game is done
    # Print score
    # Ask user if they want to play again (call main again?)
main()