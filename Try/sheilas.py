"""import numpy as np
from matplotlib import pyplot as plt
rho = 1000
D = 16.3
mu = 0.001

v_avg = np.arange(0.000001, 0.0005, 0.000001)

Re = (rho*v_avg*D)/mu

f_plot = []

for i in Re:
    if i<= 2100:
        f = 16/i
    else:
        f = 0.079/(i**0.25)
    f_plot.append(f)

plt.plot(v_avg, f_plot)
plt.xlabel("V_avg")
plt.ylabel("f")
plt.show()

plt.plot(v_avg, Re)
plt.xlabel("V_avg")
plt.ylabel("Re")
plt.show()
"""
#hhhh
"""gcddghgvmgcvtjhyfgcgcgntjyygcgchytgcjcnfchchcthgcnccfcggftfg"""

listt = [1,2,3,4,5]

for a in listt:
    print(f"{a}")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(magician)
print(f"I can't wait to see your next trick, {magician.title()}.\n")
print(magician) 