import numpy as np
import matplotlib.pyplot as plt

'''
1 บาท เข้าเกม
โยนลูกเต๋า 3 ลูกพร้อมกัน
แต้มเรียงได้เงิน 6 บาท
แต้มซ้ำ (ตอง) 12 บาท
'''

money = []
countre = 0
countso = 0

for i in range(1, 10000):
    dice = []
    dice.append(np.random.randint(1, 7))
    dice.append(np.random.randint(1, 7))
    dice.append(np.random.randint(1, 7))
    dice.sort()
    if dice[0] == dice[1] and dice[1] == dice[2]:
        countre += 1
    elif dice[0]+1 == dice[1] and dice[1]+1 == dice[2]:
        countso += 1
    else:
        income = 0

    exp = -1 + (countre/i)*12 + (countso/i)*6
    money.append(exp)
print(exp)
plt.plot(money)
plt.show()
