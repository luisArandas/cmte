

# luis arandas 22-05-2022
# sequencing functions through pyo object

import pyo as pyo
import numpy as np

s = pyo.Server().boot()

# A four-streams oscillator to produce a chord.
osc = pyo.SineLoop(freq=[0, 0, 0, 0], feedback=0.05, mul=0.2)
rev = pyo.WGVerb(osc.mix(2), feedback=0.8, cutoff=4000, bal=0.2).out()


def set_osc_freqs(notes):
    # PyoObject.set() method allow to change the value of an attribute
    # with an audio ramp to smooth out the change.
    osc.set(attr="freq", value=pyo.midiToHz(notes), port=0.005)


# The sequence of functions (some call set_osc_freqs to change the notes).
def event_0():
    x = np.random.randint(100)
    print("random int ", x)
    print("event 0")
    set_osc_freqs([60, 64, 67, 72])


def event_1():
    x = np.random.randint(100)
    print("random int ", x)
    print("event 1")
    pass


def event_2():
    x = np.random.randint(100)
    print("random int ", x)
    print("event 2")
    set_osc_freqs([60, 64, 67, 69])


def event_3():
    x = np.random.randint(100)
    print("random int ", x)
    print("event 3")
    pass


def event_4():
    x = np.random.randint(100)
    print("random int ", x)
    print("event 4")
    set_osc_freqs([60, 65, 69, 76])


def event_5():
    x = np.random.randint(100)
    print("random int ", x)
    print("event 5")
    pass


def event_6():
    x = np.random.randint(100)
    print("random int ", x)
    print("event 6")
    set_osc_freqs([62, 65, 69, 74])


def event_7():
    x = np.random.randint(100)
    print("random int ", x)
    print("event 7")
    set_osc_freqs([59, 65, 67, 74])


# Integer generator (more about triggers in section 12-triggers)
metro = pyo.Metro(time=0.5).play()
count = pyo.Counter(metro, min=0, max=8)

# Score calls the function named "event_" + count. (if count is 3,
# function named "event_3" is called without argument.
score = pyo.Score(count, fname="event_")

s.gui(locals())