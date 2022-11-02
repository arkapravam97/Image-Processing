# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 11:41:55 2022

@author: Arkaprava Mondal
"""

import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
dy = 27.72,11.96, 0.2
Correlation=[ 133.68,91.48, 7.68]
Y=Correlation
Buffer=['VO2_SiO2','VO2_Si','VO2_TiO2']
X=Buffer
xerr=[0]
fig,ax = plt.subplots()
ax.set_xlabel('Buffer')
ax.set_ylabel('Correlation')
ax.plot(X,Y,'o-',c="blue")
ax.errorbar(X,Y, yerr=dy, fmt='.k');
#plt.savefig("Correlation vs Buffer.png",dpi=3000)
