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
    #print(p1.combination)
    #print(p1.numbers)
    
    #p2 = Player()
    #p2.Dice = [1,2,3,4,5]
    #evaluate(p2)
    #print(p2.combination)
    #print(p2.numbers)
    #printres(p2)




