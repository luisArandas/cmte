

# luis arandas 26-05-2022
# gui controller for pyo

# [todo]
# granulator
# sample-accurate file mesher
# cv controllable with dc-coupled audio cards
# osc matrix
# filters on buttons

import dearpygui.dearpygui as dpg
import pyo as pyo

server = pyo.Server()
server.boot()

def save_callback():
    print("Save Clicked")
    print("server -> ", server)

dpg.create_context()
dpg.create_viewport(title=' ', width=800, height=600)
dpg.setup_dearpygui()

with dpg.window(tag="main", label="main", width=400, height=300):

    dpg.set_item_pos("main", [0., 0.])
    dpg.add_button(label="Save", callback=save_callback)

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()