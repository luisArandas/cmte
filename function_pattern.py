

# luis arandas 22-05-2022
# trying to integrate diversity in pyo patterns
# fork from http://ajaxsoundstudio.com/pyodoc/examples/09-callbacks/01-periodic-calls.html

from pyo import *
import random
import numpy as np

s = Server().boot()

amp = Fader(fadein=0.005, fadeout=0.05, mul=0.15)
osc = RCOsc(freq=[100, 100], mul=amp).out()
dly = Delay(osc, delay=1.0, feedback=0.5).out()


def recursive_func():
    _x = np.random.randint(100)
    print(_x)


def new_event():

    recursive_func()

    dur = random.choice([0.125, 0.125, 0.125, 0.25, 0.25, 0.5, 1])

    amp.dur = dur

    pat.time = dur

    # Choose a new frequency.
    freq = random.choice(midiToHz([60, 62, 63, 65, 67, 68, 71, 72]))

    # Replace oscillator's frequencies.
    osc.freq = [freq, freq * 1.003]

    # Start the envelope.
    amp.play()


# A Pattern object periodically call the referred function given as
# argument. The "time" argument is the delay between successive calls.
# The play() method must be explicitly called for a Pattern object
# to start its processing loop.
pat = Pattern(function=new_event, time=0.25).play()

s.gui(locals())