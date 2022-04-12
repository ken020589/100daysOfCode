##!/usr/bin/env python
#day13 plot

import matplotlib.pyplot as plt

listx = [0,5,6,9,13,19]
listy = [0,10,4,6,18,15]

list1 = [0,2,5,9,15,19]
list2 = [0,8,15,2,16,18]

plt.title('Title', fontsize = 20)
plt.xlabel('X Label', fontsize = 12)
plt.ylabel('Y Label', fontsize = 12)
plt.xlim(0,20) # X label range
plt.ylim(0,20) # Y label range

plt.grid(color='red', linestyle=':', linewidth=1, alpha=0.4)

plt.plot(listx,listy,'c-.o') # color='cyan', lw='1', ls='-.', label='label'
plt.plot(list1,list2,'r-.o')
plt.show()