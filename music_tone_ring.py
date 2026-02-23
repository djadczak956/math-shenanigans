import numpy as np

z12 = list(range(0, 12))
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
tone_vals = dict(zip(z12, tones))

def add_table() -> None:
    pass

def mult_table() -> None:
    pass

