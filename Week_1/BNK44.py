'''
BNK มี 44 คน แต่ละคนมี photo set 3 ใบ (รูปทั้งหมด 132 แบบ)
1 ซองมี 5 ใบ ไม่ซ้ำ
เรา main 1 คน (3 ใบ) ต้องซื้อกี่ซองถึงได้คนที่เรา main 1 ใบ
'''
import numpy as np
import matplotlib.pyplot as plt
arr = []
for i in range(100):
    count = 1
    photoset = list(range(132))
    np.random.shuffle(photoset)
    while (0 in photoset[0:5] or 1 in photoset[0:5] or 2 in photoset[0:5]) == False:
        count += 1
        np.random.shuffle(photoset)
    arr.append(count)
print(sum(arr)/(i+1))
plt.plot(arr)
plt.show()