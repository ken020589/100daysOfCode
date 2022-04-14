##!/usr/bin/env python
#day15 pie

import matplotlib.pyplot as plt
sizes = [25, 30, 15, 20, 40]
labels = ['C', 'C#', 'C++', 'Java','Python']
colors = ['red', 'green', 'blue', 'yellow', 'cyan']
explode = (0, 0, 0, 0, 0.2)
plt.pie(sizes, 
    explode=explode, 
    labels=labels, 
    colors=colors, 
    labeldistance=1.1, 
    autopct="%2.1f%%", 
    pctdistance=0.6, 
    shadow=True, 
    startangle=90)

plt.show()