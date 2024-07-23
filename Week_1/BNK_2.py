'''
BNK มี 44 คน แต่ละคนมี photo set 3 ใบ (รูปทั้งหมด 132 แบบ)
1 ซองมี 5 ใบ ไม่ซ้ำ
เรา main 1 คน (3 ใบ) ต้องซื้อกี่ซองถึงได้คนที่เรา main ได้ทั้ง 3 ใบ
'''

import numpy as np
import matplotlib.pyplot as plt
import time

arr = []
for i in range(1000):
    count = 0
    mainphoto = [3,4,5]
    photoset = list(range(132))
    np.random.shuffle(photoset)
    while mainphoto != [1,2,3]:
        #if (0 in photoset[0:5] or 1 in photoset[0:5] or 2 in photoset[0:5]) == False:
            #count += 1.
        selectedPhoto = photoset[0:5]
        if 0 in selectedPhoto:
            mainphoto[0]= 1
            #mainphoto.remove(0)
        if 1 in selectedPhoto:
            mainphoto[1]= 2
            #mainphoto.remove(1)
        if 2 in selectedPhoto:
            mainphoto[2]= 3
            #mainphoto.remove(2)
        count +=1
        mainphoto.sort()
        np.random.shuffle(photoset)
    arr.append(count)
print(sum(arr)/(i+1))
plt.plot(arr)
plt.show()