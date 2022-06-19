from pyo import *

s = Server().boot()
s.start()
wav = SquareTable()
env = CosTable([(0,0), (100,1), (500,.3), (8191,0)])
met = Metro(.125, 12).play()
amp = TrigEnv(met, table=env, dur=1, mul=.1)
pit = TrigXnoiseMidi(met, dist='loopseg', x1=20, scale=1, mrange=(48,84))
out = Osc(table=wav, freq=pit, mul=amp).out()






# from pyo import *

# s = Server(duplex=0).boot()

# soundfile = SndTable(SNDS_PATH + "/transparent.aif")

# src = Looper(soundfile, dur=2, xfade=0, mul=0.3)
# src2 = src.mix(2).out()

# # Four parallel stereo comb filters. The delay times are chosen
# # to be as uncorrelated as possible. Prime numbers are a good
# # choice for delay lengths in samples.
# comb1 = Delay(src, delay=[0.0297, 0.0277], feedback=0.65)
# comb2 = Delay(src, delay=[0.0371, 0.0393], feedback=0.51)
# comb3 = Delay(src, delay=[0.0411, 0.0409], feedback=0.5)
# comb4 = Delay(src, delay=[0.0137, 0.0155], feedback=0.73)

# combsum = src + comb1 + comb2 + comb3 + comb4

# # The sum of the original signal and the comb filters
# # feeds two serial allpass filters.
# all1 = Allpass(combsum, delay=[0.005, 0.00507], feedback=0.75)
# all2 = Allpass(all1, delay=[0.0117, 0.0123], feedback=0.61)

# # Brightness control.
# lowp = Tone(all2, freq=3500, mul=0.25).out()

# s.gui(locals())




# from pyo import *

# s = Server().boot()

# # FM implements the basic Chowning algorithm
# fm1 = FM(carrier=250, ratio=[1.5, 1.49], index=10, mul=0.3)
# fm1.ctrl()

# # CrossFM implements a frequency modulation synthesis where the
# # output of both oscillators modulates the frequency of the other one.
# fm2 = CrossFM(carrier=250, ratio=[1.5, 1.49], ind1=10, ind2=2, mul=0.3)
# fm2.ctrl()

# # Interpolates between input objects to produce a single output
# sel = Selector([fm1, fm2]).out()
# sel.ctrl(title="Input interpolator (0=FM, 1=CrossFM)")

# # Displays the spectrum contents of the chosen source
# sp = Spectrum(sel)

# s.gui(locals())