

# luis arandas 22-05-2022
# load an arbitrary audio file from the sys

from pyo import *

s = Server().boot()

path = "/Users/luisarandas/github/cmte/media/concrete.wav"

# stereo playback with a slight shift between the two channels.
sf = SfPlayer(path, speed=[1, 0.995], loop=True, mul=0.4).out()

s.gui(locals())
