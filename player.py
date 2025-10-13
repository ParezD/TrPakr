from random import randrange

class Player:
    def __init__(self, human_player=False):
        self.Hooman = human_player
        self.Dice = []
        self.toRethrow = []
        self.toKeep = []

    def __keep2reroll(self, keep):
        alldice = [0,1,2,3,4]
        keeplist = []
        for i in keep:
            if i-1 not in keeplist:
                keeplist.append(i-1)
        rerollidxs = []
        for i in alldice:
            if i not in keeplist:
                rerollidxs.append(i)
        return rerollidxs

    def first_throw(self):
        self.Dice = [randrange(6)+1 for i in range(5)]

    def rethrow(self):
        self.toRethrow = []
        self.toRethrow = self.__keep2reroll(self.toKeep)
        for i in self.toRethrow:
            self.Dice[i] = randrange(6)+1

    def __keep_user_input_help(self):
        keep = [int(i) for i in input().strip().split()]
        for i in keep:
            if i < 1 or i > 5:
                print("Invalid die/dice.")
                return None
        return keep

    def __keep_user_input(self):
        while(True):
            diceToKeep = self.__keep_user_input_help()
            if diceToKeep is not None:
                break
        return diceToKeep

    def keep_dice(self):
        self.toKeep = []
        if self.Hooman:
            self.toKeep = self.__keep_user_input()
        else:
            self.toKeep = [] #imp[lement some keeping decisionmaking


