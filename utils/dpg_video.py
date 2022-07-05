

# luis arandas 05-07-2022
# trying to call videos easily on dpg
# based on https://www.diogoaos.com/blog/display-video-in-a-python-gui-with-dear-pygui/

import av
import sys
# av is a python binding for the ffmpeg library
import numpy as np

fn = sys.argv[1]

def load_video(fn):
    video = av.open(fn)
    fmt = 'rgb24'
    for f in video.decode():
        cf = f.to_ndarray(format=fmt)  # convert to rgb
        yield cf
    video.close()


import dearpygui.dearpygui as dpg

w,h,d = 1280*2 ,720*2 ,3  # the width and height values are overdimensioned to fit a wider range of resolutions
raw_data = np.zeros((h,w,d), dtype=np.float32)

with dpg.texture_registry(show=False):
    dpg.add_raw_texture(w, h, raw_data, format=dpg.mvFormat_Float_rgb, tag="texture_tag")

def update_dynamic_texture(new_frame):
    global raw_data
    h2, w2, d2 = new_frame.shape
    raw_data[:h2, :w2] = new_frame[:,:] / 255


with dpg.window(label="Video player"):
    dpg.add_image("texture_tag")

dpg.create_viewport(title='Dashboard', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()

video_gen = load_video(fn)
for f in video_gen:
    if dpg.is_dearpygui_running():
        update_dynamic_texture(f)
        dpg.render_dearpygui_frame()
    else:
        break  # deal with this scenario appropriately

dpg.destroy_context()

print("hey")