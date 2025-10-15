
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
        player.numbers[0] = comb[5][0]
        return
    
    if len(comb[4]) > 0:
        player.combination = 7
        player.numbers[0] = comb[4][0]
        player.numbers[1] = comb[1][0]
        return

    if len(comb[3]) > 0 and len(comb[2]) > 0:
        player.combination = 6
        player.numbers[0] = comb[3][0]
        player.numbers[1] = comb[2][0]
        return

    if nasob[1] == nasob[2] == nasob[3] == nasob[4] == nasob[5]:
        player.combination = 5
        return

    if nasob[0] == nasob[1] == nasob[2] == nasob[3] == nasob[4]:
        player.combination = 4
        return

    if len(comb[3]) > 0:
        player.combination = 3
        player.numbers[0] = comb[3][0]
        player.numbers[1] = comb[1][0]
        player.numbers[2] = comb[1][1]
        return

    if len(comb[2]) == 2:
        player.combination = 2
        player.numbers[0] = comb[2][0]
        player.numbers[1] = comb[2][1]
        player.numbers[2] = comb[1][0]
        return

    if len(comb[2]) == 1:
        player.combination = 1
        player.numbers[0] = comb[2][0]
        player.numbers[1] = comb[1][0]
        player.numbers[2] = comb[1][1]
        player.numbers[3] = comb[1][2]
        return

    if len(comb[1]) == 5:
        player.combination = 0
        player.numbers[0] = comb[1][0]
        player.numbers[1] = comb[1][1]
        player.numbers[2] = comb[1][2]
        player.numbers[3] = comb[1][3]
        player.numbers[4] = comb[1][4]
        return


def printres(player):
    match player.combination:
        case 8:
            print("Five of a kind! - 5x", player.numbers[0])
        case 7:
            print("Four of a kind! - 4x", player.numbers[0], ", ", player.numbers[1])
        case 6:
            print("Fullhouse! - 3x", player.numbers[0], ", 2x", player.numbers[1])
        case 5:
            print("High flush! - 2, 3, 4, 5, 6")
            # idk what its called leave me alone
        case 4:
            print("Low flush! - 1, 2, 3, 4, 5")
            # idk what its called leave me alone
        case 3:
            print("Three of a kind! - 3x", player.numbers[0], ", ", player.numbers[1], ", ", player.numbers[2])
        case 2:
            print("Two pairs! - 2x", player.numbers[0], ", 2x", player.numbers[1], ", ", player.numbers[2])
        case 1:
            print("Pair! - 2x", player.numbers[0], ", ", player.numbers[1], ", ", player.numbers[2], ", ", player.numbers[3])
        case 0:
            print("Go fuck yourself! - ", player.numbers[0], ", ", player.numbers[1], ", ", player.numbers[2], ", ", player.numbers[3], ", ", player.numbers[4])
