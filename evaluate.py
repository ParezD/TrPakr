
def evaluate(player):
    dice = [i for i in player.Dice]
    dice.sort(reverse=True)
    nasob = [0]*6
    for i in range(6):
        for j in range(5):
            if dice[j] == i+1:
                nasob[i] += 1

    comb = [[],[],[],[],[],[]]
    #for i in reversed(range(6))
    for i in range(5, -1, -1):
        comb[nasob[i]].append(i+1)

    if len(comb[5]) > 0:
        player.combination = 8
        player.nums[0] = comb[5][0]
        return
    
    if len(comb[4]) > 0:
        player.combination = 7
        player.nums[0] = comb[4][0]
        player.nums[1] = comb[1][0]
        return

    if len(comb[3]) > 0 and len(comb[2]) > 0:
        player.combination = 6
        player.nums[0] = comb[3][0]
        player.nums[1] = comb[2][0]
        return

    if nasob[1] == nasob[2] == nasob[3] == nasob[4] == nasob[5]:
        player.combination = 5
        return

    if nasob[0] == nasob[1] == nasob[2] == nasob[3] == nasob[4]:
        player.combination = 4
        return

    if len(comb[3]) > 0:
        player.combination = 3
        player.nums[0] = comb[3][0]
        player.nums[1] = comb[1][0]
        player.nums[2] = comb[1][1]
        return

    if len(comb[2]) == 2:
        player.combination = 2
        player.nums[0] = comb[2][0]
        player.nums[1] = comb[2][1]
        player.nums[2] = comb[1][0]
        return

    if len(comb[2]) == 1:
        player.combination = 1
        player.nums[0] = comb[2][0]
        player.nums[1] = comb[1][0]
        player.nums[2] = comb[1][1]
        player.nums[3] = comb[1][2]
        return

    if len(comb[1]) == 5:
        player.combination = 0
        player.nums[0] = comb[1][0]
        player.nums[1] = comb[1][1]
        player.nums[2] = comb[1][2]
        player.nums[3] = comb[1][3]
        player.nums[4] = comb[1][4]
        return


def printres(player):
    match player.combination:
        case 8:
            print("Five of a kind! - 5x", player.nums[0])
        case 7:
            print("Four of a kind! - 4x", player.nums[0], ", ", player.nums[1])
        case 6:
            print("Fullhouse! - 3x", player.nums[0], ", 2x", player.nums[1])
        case 5:
            print("High flush! - 2, 3, 4, 5, 6")
            # idk what its called leave me alone
        case 4:
            print("Low flush! - 1, 2, 3, 4, 5")
            # idk what its called leave me alone
        case 3:
            print("Three of a kind! - 3x", player.nums[0], ", ", player.nums[1], ", ", player.nums[2])
        case 2:
            print("Two pairs! - 2x", player.nums[0], ", 2x", player.nums[1], ", ", player.nums[2])
        case 1:
            print("Pair! - 2x", player.nums[0], ", ", player.nums[1], ", ", player.nums[2], ", ", player.nums[3])
        case 0:
            print("Go fuck yourself! - ", player.nums[0], ", ", player.nums[1], ", ", player.nums[2], ", ", player.nums[3], ", ", player.nums[4])

def comp(v1, v2):
    if v1 == v2:
        return 0
    elif v1 > v2:
        return 1
    else:
        return 2

def decide(p1, p2):
    if p1.combination > p2.combination:
        return 1
    elif p2.combination > p1.combination:
        return 2
    else:
        match p1.combination:
            case 8: # five of a kind
                return comp(p1.nums[0], p2.nums[0])
            case 7: # four of a kind
                val1 = comp(p1.nums[0], p2.nums[0])
                if val1: return val1
                else: return comp(p1.nums[1], p2.nums[1])
            case 6: # fullhouse
                val = [None]*2
                for i in range(2):
                    val[i] = comp(p1.nums[i], p2.nums[i])
                    if val[i]:
                        return val[i]
                return 0
            case 5: # high flush
                return 0
            case 4: # low flush
                return 0
            case 3: # three of a kind
                val = [None]*3
                for i in range(3):
                    val[i] = comp(p1.nums[i], p2.nums[i])
                    if val[i]:
                        return val[i]
                return 0
            case 2: # two pairs
                val = [None]*3
                for i in range(3):
                    val[i] = comp(p1.nums[i], p2.nums[i])
                    if val[i]:
                        return val[i]
                return 0
            case 1: # pair
                val = [None]*4
                for i in range(4):
                    val[i] = comp(p1.nums[i], p2.nums[i])
                    if val[i]:
                        return val[i]
                return 0
            case 0: # notin
                val = [None]*5
                for i in range(5):
                    val[i] = comp(p1.nums[i], p2.nums[i])
                    if val[i]:
                        return val[i]
                return 0

