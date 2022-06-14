

# luis arandas 26-05-2022
# gui controller for pyo

# [todo]
# granulator
# sample-accurate file mesher
# cv controllable with dc-coupled audio cards
# osc matrix
# filters on buttons

import pyo as pyo
import dearpygui.dearpygui as dpg
from os import listdir, path
import time

audio_server = pyo.Server()
audio_server.boot()
audio_table = pyo.SndTable()

current_selected_file = ""
audio_file_extensions = [".mp3", ".flac", ".aiff", ".wav", ".ogg", ".alac", ".dsd"]
current_audio_table_text = ""

dpg.create_context()
# dpg.set_global_font_scale(1.6)
dpg.create_viewport(title=' ', width=1280, height=720)


def select_directory(sender, app_data):
    with dpg.file_dialog(tag='file_dialog', width=750, height=450, directory_selector=True, show=True, modal=True, callback=process_directory):
        dpg.add_file_extension(".*")


def process_directory(sender, app_data):
    directory = app_data["file_path_name"]
    files = listdir(directory)
    dpg.configure_item("files_listbox", items=files)
    dpg.set_value("file_text", directory)


def select_file(sender, app_data):
    selected_file = app_data
    cwd = dpg.get_value("file_text")
    selected_file = cwd + "/" + selected_file

    global current_selected_file
    current_selected_file = selected_file


def load_audio_to_table(file_name):
    print("loading -> ", file_name)
    global current_audio_table_text
    x = str(pyo.sndinfo(file_name))
    current_audio_table_text += (x + " \n")
    dpg.set_value("current_audios_in_the_table", current_audio_table_text)

 
def check_audio_extension(file_name):
    x = file_name[-4:]
    if '.' in x:
        if x in audio_file_extensions:
            load_audio_to_table(file_name)
        else:
            pass
    else:
        pass


def audio_table_callback():
    print("audio table callback ", current_audio_table_text)


def add_audio_file(sender, app_data):
    check_audio_extension(current_selected_file)

def add_audio_folder(sender, app_data):
    print(sender)
    print(app_data)



with dpg.window(tag="mainwindow"):

    with dpg.window(tag="generative_start", width=417, height=305, menubar=False, no_title_bar=True, no_move=True, no_resize=True):
        
        dpg.set_item_pos("generative_start", [5., 5.])
        dpg.add_text("directory explorer")
        dpg.add_separator()
        dpg.add_text("not selected", tag="file_text")
        
        with dpg.group(horizontal=True):

            dpg.add_button(label="choose directory", width=128, callback=select_directory)
            dpg.add_button(label="add audio file", width=128,callback=add_audio_file)
            dpg.add_button(label="add audio folder", width=128,callback=add_audio_folder)

        dpg.add_listbox(tag="files_listbox", label=' ', callback=select_file, num_items=12, width=400)

    with dpg.window(tag="table_viewer", width=417, height=400, menubar=False, no_title_bar=True, no_move=True, no_resize=True):
        
        dpg.set_item_pos("table_viewer", [5., 315.])
        dpg.add_text("table buffer")
        dpg.add_separator()
        dpg.add_spacer()
        # dpg.add_listbox(tag="table_listbox", label='table_listbox', callback=audio_table_callback, num_items=len(current_audio_table), width=400)
        dpg.add_text(current_audio_table_text, tag="current_audios_in_the_table", wrap=400)



dpg.setup_dearpygui()
dpg.show_viewport()

dpg.set_primary_window("mainwindow", True)
dpg.start_dearpygui()
dpg.destroy_context()
