

import matplotlib.pyplot as plt
import numpy as np
Math = [100, 90]
English = [90, 80]
Physics = [80, 80]
Computer = [80, 90]
x = np.arange(2) 
width = 0.2
labels = ['Math', 'English', 'Physics', 'Computer']
names = ['Bill', 'Mary']

# ******************************
# Make your code
# ******************************
fig,ax = plt.subplots()
rec1 = ax.bar(x-width-width/2, Math, width, label="Math")
rec2 = ax.bar(x-width/2, English, width, label="English")
rec3 = ax.bar(x+width/2, Computer, width, label="Computer")
rec4 = ax.bar(x+width+width/2, Physics, width, label="Physics")
ax.set_title("Grouped graph for scores")
ax.legend()
ax.set_xticks(x, names)
ax.bar_label(rec1, padding=3)
ax.bar_label(rec2, padding=3)
ax.bar_label(rec3, padding=3)
ax.bar_label(rec4, padding=3)
plt.show()
fig.savefig('A11.png')
