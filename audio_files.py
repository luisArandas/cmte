

# luis arandas 22-05-2022
# play sequence of audio files from folder

import pyo as pyo
import os

server = pyo.Server()
server.boot()

print("server -> ", server)

folder = "/Users/luisarandas/github/cmte/media/"
files = os.listdir(folder)

table = pyo.SndTable()
print("table -> ", table)

for i in files:
    _file = folder+os.sep+i
    print("file info -> ", i, pyo.sndinfo(_file))
    table.append(_file)


print("table duration ", table.getDur()) # duration in seconds
print("table size ", table.getSize()) # size in samples

audio = pyo.Osc(table=table, freq=table.getRate(), mul=.4).out()

server.gui(locals())
# server.start()
