from player import *
from evaluate import *

if __name__ == "__main__":
    p1 = Player(True)
    p1.first_throw()
    print(p1.Dice)
    p1.keep_dice()
    p1.rethrow()
    print(p1.Dice)
    evaluate(p1)
    printres(p1)

    p2 = Player()
    p2.first_throw()
    p2.keep_dice()
    p2.rethrow()
    evaluate(p2)
    print("Player 2:")
    printres(p2)

    print(decide(p1, p2))





