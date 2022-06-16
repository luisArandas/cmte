


import pyo as pyo
import numpy as np
from scipy.io.wavfile import read
import math

s = pyo.Server(sr=44100, nchnls=2, buffersize=512, duplex=1).boot()

def terrain(size=256, freq=1, phase=16):
    l = []
    xfreq = 2 * math.pi * freq
    for i in range(size):
        ph = math.sin(i/float(phase))
        tmp = [math.sin(xfreq * (j/float(size)) + ph) for j in range(size)]
        l.append(tmp)
    return l

SIZE = 512
m = pyo.NewMatrix(SIZE, SIZE, terrain(SIZE, 2, 16)).normalize()
m.view()
rnd = pyo.Randi(0.05, 0.45, .1)
x = pyo.Sine([99.5,99.76], 0, .49, .5)
y = pyo.Sine([25, 51.5, 75.2, 100.1], 0, rnd, .5)
a = pyo.MatrixPointer(m, x, y, mul=.1).out()

s.gui(locals())


# a = read("media/concrete.wav")
# print("a ", a)
# x = np.array(a[1],dtype=float)
# print("x ", x)
# print("yoyo")