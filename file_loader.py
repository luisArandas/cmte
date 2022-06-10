

# luis arandas 26-05-2022
# gui controller for pyo

# [todo]
# granulator
# sample-accurate file mesher
# cv controllable with dc-coupled audio cards
# osc matrix
# filters on buttons

import dearpygui.dearpygui as dpg
from os import listdir, path
import time

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

    dpg.set_value("file_info_n", "file :" + selected_file)
    dpg.set_value("file_info_1", "last accessed :" + time.ctime(path.getatime(selected_file)))
    dpg.set_value("file_info_2", "last modified :" + time.ctime(path.getmtime(selected_file)))
    dpg.set_value("file_info_3", "last changed  :" + time.ctime(path.getctime(selected_file)))
    # dpg.set_value("file_info_4", "file size     :" + path.getsize(selected_file))

def add_audio_file(sender, app_data):
    print(sender)
    print(app_data)

def add_audio_folder(sender, app_data):
    print(sender)
    print(app_data)


with dpg.window(tag="mainwindow"):

    with dpg.window(tag="generative start", width=417, height=305, menubar=False, no_title_bar=True, no_move=True, no_resize=True):
        dpg.set_item_pos("generative start", [5., 5.])
        dpg.add_text("directory explorer")
        dpg.add_separator()

        dpg.add_text("not selected", tag="file_text")
        with dpg.group(horizontal=True):
            dpg.add_button(label="choose directory", width=128, callback=select_directory)
            dpg.add_button(label="add audio file", width=128,callback=add_audio_file)
            dpg.add_button(label="add audio folder", width=128,callback=add_audio_folder)

        dpg.add_listbox(tag="files_listbox", label=' ', callback=select_file, num_items=12, width=400)

        # dpg.add_text(tag="file_info_n")
        # dpg.add_text(tag="file_info_1")
        # dpg.add_text(tag="file_info_2")
        # dpg.add_text(tag="file_info_3")
        # dpg.add_text(tag="file_info_4")

dpg.setup_dearpygui()
dpg.show_viewport()

dpg.set_primary_window("mainwindow", True)
dpg.start_dearpygui()
dpg.destroy_context()
