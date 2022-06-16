

# luis arandas 26-05-2022
# table controller


import pyo as pyo
import dearpygui.dearpygui as dpg
from os import listdir, path
import time
import math

audio_server = pyo.Server()
audio_server.boot()
audio_table = pyo.SndTable()
audio_table.append("/Users/luisarandas/github/cmte/media/concrete.wav")

current_selected_file = ""
audio_file_extensions = [".mp3", ".flac", ".aiff", ".wav", ".ogg", ".alac", ".dsd"]
file_path_arr = []
current_audio_table_text = ""
current_audio_table = None

table_x_data = [0,0]
table_y_data = [0,0]

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


def add_to_visualiser():
    global table_x_data
    global table_y_data
    # audio_table.normalize()
    table = audio_table.getTable() # all=False
    start_distance = 0.0
    x_data = [0.0] # number of samples and define distance
    for i in range(len(table)):
        start_distance = start_distance + 1
        x_data.append(start_distance)

    y_data = table
    table_x_data = x_data
    table_y_data = y_data
    dpg.set_value('series_1', [x_data, y_data])



def load_audio_to_table(file_name):
    # load the actual audio and paths
    file_path_arr.append(file_name)
    audio_table.append(file_name)
    add_to_visualiser()

    x = str(pyo.sndinfo(file_name))
    _x = x.split()
    del _x[1] # remove long float
    s = ''.join(str(x) for x in _x)

    global current_audio_table_text
    text = ((s) + " \n")
    if text in current_audio_table_text:
        pass
    else:
        current_audio_table_text += text
        print("current audio table text -> ", current_audio_table_text)
        dpg.set_value("current_audios_in_the_table", current_audio_table_text)


def check_audio_extension(file_name):
    x = file_name[-4:]
    if '.' in x:
        if x in audio_file_extensions:
            return file_name
        else:
            pass
    else:
        pass


def add_audio_file(sender, app_data):
    path = check_audio_extension(current_selected_file)
    load_audio_to_table(path)


def add_audio_folder(sender, app_data):
    print("TODO!")
    print(sender)
    print(app_data)


# sindatax = []
# sindatay = []

# def generate_plots():
#     audio_table.normalize()
#     yo_y = audio_table.getTable() # all=False
#     start_distance = 0.0
#     x_data = [0.0] # number of samples and define distance
#     for i in range(len(yo_y)):
#         start_distance = start_distance + 1
#         x_data.append(start_distance)
    
#     print("x data ", yo_y)
#     y_data = yo_y

#     global sindatax
#     global sindatay
#     sindatax = x_data
#     sindatay = yo_y

    # global sindatax
    # global sindatay
    # for i in range(50):
    #     sindatax.append(i/100) # just make steps of 0.01
    #     sindatay.append(0.5 + 0.5 * math.sin(50*i/100))

# generate_plots()


with dpg.window(tag="mainwindow"):

    with dpg.window(tag="generative_start", width=335, height=305, menubar=False, no_title_bar=True, no_move=True, no_resize=True):
        
        dpg.set_item_pos("generative_start", [5., 5.])
        dpg.add_text("directory explorer")
        dpg.add_separator()
        dpg.add_text("not selected", tag="file_text")
        
        with dpg.group(horizontal=True):

            dpg.add_button(label="choose dir", width=100, callback=select_directory)
            dpg.add_button(label="add file", width=100, callback=add_audio_file)
            dpg.add_button(label="add folder", width=101, callback=add_audio_folder)

        dpg.add_listbox(tag="files_listbox", label=' ', callback=select_file, num_items=12, width=-1)

    with dpg.window(tag="table_viewer", width=335, height=400, menubar=False, no_title_bar=True, no_move=True, no_resize=True):
        
        dpg.set_item_pos("table_viewer", [5., 315.])
        dpg.add_text("table buffer")
        dpg.add_separator()
        dpg.add_spacer()
        # dpg.add_listbox(tag="table_listbox", label='table_listbox', callback=audio_table_callback, num_items=len(current_audio_table), width=400)
        dpg.add_text(current_audio_table_text, tag="current_audios_in_the_table", wrap=400)

    with dpg.window(tag="plotting_viewer", width=490, height=710, menubar=False, no_title_bar=True, no_move=True, no_resize=True):
        dpg.set_item_pos("plotting_viewer", [345., 5.])
        dpg.add_text("plotting table")
        dpg.add_separator()
        dpg.add_spacer()

        # with dpg.subplots(3, 3, label="", width=-1, height=-1, row_ratios=[5.0, 1.0, 1.0], column_ratios=[5.0, 1.0, 1.0]) as subplot_id:
        #     for i in range(9):
        #         with dpg.plot(no_title=True):
        #             dpg.add_plot_axis(dpg.mvXAxis, label="", no_tick_labels=True)
        #             with dpg.plot_axis(dpg.mvYAxis, label="", no_tick_labels=True):
        #                 dpg.add_line_series(sindatax, sindatay, label="0.5 + 0.5 * sin(x)")

        with dpg.plot(label="", height=190, width=-1, anti_aliased=True):
            dpg.add_plot_legend()

            dpg.add_plot_axis(dpg.mvXAxis, label="", no_tick_labels=True, no_gridlines=True, no_tick_marks=True) #, lock_min=True)
            # dpg.set_axis_limits_auto(dpg.mvXAxis)
            # dpg.fit_axis_data(dpg.mvXAxis)

            with dpg.plot_axis(dpg.mvYAxis, label="", no_tick_labels=True, no_tick_marks=True, lock_min=True, lock_max=True, no_gridlines=True,):
                dpg.set_axis_limits(dpg.last_item(), -1.2, 1.2)

                # series 1 # main table buffer
                dpg.add_line_series(table_x_data, table_y_data, label="series_1", tag="series_1")
                dpg.add_button(label="series_1", user_data = dpg.last_item(), parent=dpg.last_item(), callback=lambda s, a, u: dpg.delete_item(u))


        with dpg.tree_node(label="single players"):

            def _unstage_items(sender, app_data, user_data):
                print("user data ", user_data)
                print("user data [0] ", user_data[1])
                # push the child back onto the container stack
                dpg.push_container_stack(user_data[1])
                # this will 'unpack' the staging container (regular parent deduction rules apply)
                dpg.unstage(user_data[0])
                # pop the child back off the container stack
                dpg.pop_container_stack()

            # when unstaging a stage, it 'unpacks' itself
            with dpg.stage(tag="stage1"):
                dpg.add_button(label="Staged Button 1")

            
            ub1 = dpg.add_button(label="unstage buttons", callback=_unstage_items)
            child_id = dpg.add_child_window(width=-1)
            dpg.set_item_user_data(ub1, ["stage1", child_id])         


dpg.setup_dearpygui()
dpg.show_viewport()

dpg.set_primary_window("mainwindow", True)
dpg.start_dearpygui()
dpg.destroy_context()
