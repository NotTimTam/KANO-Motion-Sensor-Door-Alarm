"""child of door-alarm.py. Go there for more info.
This script will be uncommented to save time. Basically: it plays a noise when told to by door-alarm.py!"""

import simpleaudio as sa
import time

def run_sound_alarm():
    wave_obj = sa.WaveObject.from_wave_file("alert.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()
