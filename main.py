import os
import eel
import webbrowser
from backend.feature import *
from backend.command import *


def start ():
    eel.init("frontend")
    eel.start("index.html", mode="chrome", host="localhost", port=8000, block=True)


    play_assistant_sound()


    eel.start("index.html", mode=None, host="localhost", block=True)
