##!/usr/bin/env python
#day14 bar

from turtle import width
import matplotlib.pyplot as plt

width = 0.25
listx = ['C','C++','C#','Java','Python']
listx1 = [x - width/2 for x in range(len(listx))]
listx2 = [x + width/2 for x in range(len(listx))]
listy1 = [6,10,8,18,15]
listy2 = [2,5,16,12,15]

plt.bar(listx1,listy1,width,color='r',label='Boy')
plt.bar(listx2,listy2,width,color='b',label='Girl')

plt.title('Language')
plt.xlabel('Language')
plt.ylabel('num')

plt.ylim(0,20) # Y label range
plt.xticks(range(len(listx)), labels=listx)

plt.show()
