from dearpygui.core import *
from dearpygui.simple import *

def save_callback(sender, data):
    print("Hello again!")

with window("Sample Window"):
    add_text("Hello, Analytics Vidhya Readers!")
    add_button("Click me and check terminal!", callback=save_callback)
    add_input_text("string", default_value="Enter your name")
    add_slider_float("float", default_value=0.273, max_value=1)

start_dearpygui()