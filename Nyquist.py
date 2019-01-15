# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 09:45:54 2019

@author: Red

"""
import numpy as np
import matplotlib.pyplot as plt
import math
z = np.complex(1+2j/(2+2j))
print(z.real)
print(z.imag)

def Plot(w_range):
    w = np.arange(0,w_range,0.1)
    real_vals = np.zeros(len(w))
    imag_vals = np.zeros(len(w))
    e=math.exp(1)
    print(e)
    for i in range(0,len(w)):
        omega = w[i]
        function = np.complex(e**(-1j*omega)/(1+1j*omega))
        real_vals[i] = function.real
        imag_vals[i] = function.imag
    plt.plot(real_vals,imag_vals)
    plt.show()   
Plot(1000)

        
    

    