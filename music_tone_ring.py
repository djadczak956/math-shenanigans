import numpy as np
from int_mod_ring import int_mod_ring

z12 = int_mod_ring(12)
z12_vals = z12.to_list()
base_tones = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
#
while True:
    root = input("Pick a root note: ")
    if root in base_tones:
        print(f"Selected {root} as root note.")
        break
    else:
        print("Try again (pick one of the following: 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'). ")

tones = base_tones
tone_vals = dict(zip(z12_vals, tones))

#TODO: Finish this
def int_to_tones(tone_vals):
    pass

