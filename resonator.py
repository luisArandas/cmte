

# luis arandas 30-06-2022
# ressonator


from pyo import *
import random

s = Server().boot()

# Six random frequencies.
freqs = [random.uniform(1000, 3000) for i in range(6)]

# Six different plucking speeds.
pluck = Metro([0.9, 0.8, 0.6, 0.4, 0.3, 0.2]).play()

# LFO applied to the decay of the resonator.
decay = Sine(0.1).range(0.01, 0.15)

# Six ComplexRes filters.
rezos = ComplexRes(pluck, freqs, decay, mul=5).out()

# Change chime frequencies every 7.2 seconds
def new():
    freqs = [random.uniform(1000, 3000) for i in range(6)]
    rezos.freq = freqs


pat = Pattern(new, 7.2).play()

s.gui(locals())