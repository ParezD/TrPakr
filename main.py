from player import *

if __name__ == "__main__":
    p1 = Player(True)
    p1.first_throw()
    print(p1.Dice)
    p1.keep_dice()
    p1.rethrow()
    print(p1.Dice)



