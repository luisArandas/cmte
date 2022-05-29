

# be careful with headphones!

import pyo as pyo
import numpy as np

server = pyo.Server().boot()

snippet_len_secs = 3
samples = pyo.secToSamps(snippet_len_secs) 

monte_carlo_array = np.random.random_sample(samples) # np array with uniform random numbers between 0 and 1
monte_carlo_table = pyo.DataTable(samples, init=monte_carlo_array.tolist())
# monte_carlo_table.normalize() # Should normalize to range -1 to 1
monte_carlo_table.removeDC() # this is the normalise I want
monte_carlo_table.view() # But here seems not to do so, see graph

output = pyo.Osc(table=monte_carlo_table, freq=1.0/snippet_len_secs, mul=0.5).out() # loop the snippet using Osc object

server.gui(locals())