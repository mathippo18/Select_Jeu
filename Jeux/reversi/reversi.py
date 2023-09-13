#!/usr/bin/env python

from game import game
try:
    if __name__ == "__main__":
        game.start()
except KeyboardInterrupt:
    print("\n")
