import random, math
import numpy as np
import matplotlib.pyplot as plt


d6 = (1, 2, 3, 4, 5, 6)
d8 = (1, 2, 3, 4, 5, 6, 7, 8)
d10 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
d12 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
d20 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

def dice_rolls(dice, num_dice):
    rolls = []
    for i in range(num_dice):
        rolls.append(random.choice(dice))
    return rolls

# dice_rolls(d6, 4)

def avg_sum(dice, num_dice, keep, add=0, rounds=10000):
    sums = []
    for j in range(rounds):
        rolls = dice_rolls(dice, num_dice)
        rolls.sort(reverse=True)
        rolls = rolls[:keep]
        rolls_add = [x + add for x in rolls]
        sums.append(sum(rolls_add))
    return sums

# r_6 = avg_sum(d6, 4, 3)
# plt.title("4d6k3 10,000 Round Average Sum")
# plt.hist(r_6, 15)
# plt.show()

# r_12 = avg_sum(d12, 1, 1, add=5)
# plt.title("1d12+5 10,000 Round Average Sum")
# plt.hist(r_12, 12)
# plt.show()

def avg_rolls(dice, num_dice, keep, add=0, rounds=10000):
    roll_list = []
    avg_rolls = []
    for j in range(rounds):
        rolls = dice_rolls(dice, num_dice)
        rolls.sort(reverse=True)
        rolls = rolls[:keep]
        rolls_add = [x + add for x in rolls]
        roll_list.append(rolls_add)
    for m in range(len(roll_list[0])):
        roll_set = []
        for i in range(len(roll_list)):
            roll_set.append(roll_list[i][m])
        avg = sum([x for x in roll_set])/len(roll_set)
        avg_rolls.append(avg)
    return avg_rolls

# r_6 = avg_rolls(d6, 4, 3, rounds=100)
# r_6

def skill_rolls (dice, num_dice, keep, add=0, rounds=10000):
    all_rolls = []
    avg_rolls = []
    for i in range(rounds):
        roll_6 = []
        for i in range(6):
            roll = dice_rolls(dice, num_dice)
            roll.sort(reverse=True)
            roll = roll[:keep]
            roll_add = [x + add for x in roll]
            roll_6.append(sum(roll_add))
        roll_6.sort(reverse=True)
        all_rolls.append(roll_6)
    for m in range(len(all_rolls[0])):
        roll_set = []
        for i in range(len(all_rolls)):
            roll_set.append(all_rolls[i][m])
        avg = sum([x for x in roll_set])/len(roll_set)
        avg_rolls.append(avg)
    return avg_rolls

r_6 = skill_rolls(d6, 4, 3)
r_6

r12 = skill_rolls(d12, 1, 1, add=5)
r12

r10 = skill_rolls(d10, 1, 1, add=7)
r10

r_6 = skill_rolls(d6, 3, 3, rounds=100000)
r_6
r_61 = skill_rolls(d6, 4, 3, rounds=100000)
r_61

r6_5 = avg_rolls(d6, 5, 5)
sum(r6_5)