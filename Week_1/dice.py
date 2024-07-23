import numpy as np
import matplotlib.pyplot as plt

expectationValue = []
a = []

for i in range(1000):
    x = np.random.randint(1, 7)
    a.append(x)
    expectationValue.append(sum(a)/len(a))

plt.plot(expectationValue)
plt.show()