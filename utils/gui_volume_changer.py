

# luis arandas 26-05-2022
# gui controller for audio volume change (w mixer)

import dearpygui.dearpygui as dpg
import pyo as pyo

server = pyo.Server()
server.boot()
server.start()

background_audio_table = pyo.SndTable("media/concrete.wav").normalize() # loading the audio file to RAM
background_freq = background_audio_table.getRate() # gets the frequency relative to the table length
background_sound = pyo.Osc(table=background_audio_table, freq=background_freq, mul=1)# .out()
# background_sound = pyo.SfPlayer("background.wav", speed=1, loop=True, mul=1)

audio_mixer = pyo.Mixer(outs=2, chnls=2) # this is the end of the chain
audio_mixer.addInput(0, background_sound)
audio_mixer.setAmp(0,0,1)
audio_mixer.setAmp(0,1,1)
audio_mixer.out()

def save_callback():
    print("Save Clicked")
    print("server -> ", server)
    audio_mixer.setAmp(0,0,0.05)
    audio_mixer.setAmp(0,1,0.05)



dpg.create_context()
dpg.create_viewport(title=' ', width=800, height=600)
dpg.setup_dearpygui()

with dpg.window(tag="main", label="main", width=400, height=300):

    dpg.set_item_pos("main", [0., 0.])
    dpg.add_button(label="Save", callback=save_callback)

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()