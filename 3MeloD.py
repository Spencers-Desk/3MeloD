import math
from typing import Tuple
from config import ProjectConfig, SongConfig
import music_dictionaries as md

# Default name for the project configuration file.
config_default_name: str = "config.txt"

project_config: ProjectConfig = ProjectConfig()
from config import ProjectConfig, SongConfig

if not project_config.could_load_file(config_default_name):
    print(f"failed to load \"{config_default_name}\" file")
    exit(-1)


##### Inputs #####
# motor angle per step
x_ang, y_ang, z_ang = project_config.get_printer_angles_per_step()

# rotation distance per revolution (mm)
x_rpr, y_rpr, z_rpr = project_config.get_printer_rot_distance_per_rev()

# Printer Dimensions
x_dim, y_dim, z_dim = project_config.get_printer_dimensions()

song_config: SongConfig = SongConfig()
if not song_config.could_load_file(project_config.get_song_config_path()):
    print("failed to load the corresponding song config file")
    exit(-1)


# --SONG SPECIFIC INPUTS-- #
# you need to have the melody.txt, mid.txt, and bass.txt inside a folder directory
song_name: str
song_directory: str
song_name, song_directory = song_config.get_song_properties()

# tempo of the song - sixteenth note is unit - if you used an eighth note rhythm divide your tempo by 2
tempo: int | float = song_config.get_song_tempo()

#song octave adjustment. It is free to adjust as needed
x_octave_adj, y_octave_adj, z_octave_adj = song_config.get_song_octaves_adjustment()

# Comment characters - use this to add characters that indicated a comment
comment: list[str] = ['', ' ', '#', '\n']



##### END OF INPUTS - ONLY NERDS MAY PASS THIS LINE #####

# reference frequency
f_ref: int = 440  #Hz "A4"

# steps per revolution divided by distance per revolution = steps/distance
x_stepdist: float = (360/x_ang) / x_rpr
y_stepdist: float = (360/y_ang) / y_rpr
z_stepdist: float = (360/z_ang) / z_rpr

md.melody_dictionary['ref']: dict[str, int] = int((f_ref / x_stepdist) * 60 * 2**x_octave_adj)
md.mid_dictionary['ref']: dict[str, int] = int((f_ref / y_stepdist) * 60 * 2**y_octave_adj)
md.bass_dictionary['ref']: dict[str, int] = int((f_ref / z_stepdist) * 60 * 2**z_octave_adj)


# takes in note and dictionary, spits out feedrate for one axis
def frequency_finder(note: str, dictionary: dict[str, int]) -> float:
    global tempo
    while True:
        try:
            if note == 'r':  # checking for a rest
                return 0  # return feed rate of 0 for rests
            elif note in dictionary:
                return dictionary['ref'] * 2 ** (dictionary[note] / 12)    # (reference speed) * 2^((note offset)/12)
            elif note not in dictionary:
                raise ValueError
        except ValueError:
            print(f'Incorrect note found at: {i} (note will be after this line more than likely) Note: {note}')


def kinematics(speed: float, this_note: str, last_note: str, dim: float, current_pos: float, last_pos: float) \
        -> Tuple[float, float]:
    global tempo

    mid_pos: float = dim/2
    move_length: float = speed / 60 * (15 / tempo)

    if this_note != last_note:  # different note being played - move towards middle of axis
        if current_pos <= mid_pos:
            last_pos = current_pos  # update position
            current_pos = current_pos + move_length
        elif current_pos > mid_pos:
            last_pos = current_pos  # update position
            current_pos = current_pos - move_length
        else:
            print('Error traveled outside range')

    if this_note == last_note:  # same note, we want to keep moving in the same direction, IF we can
        if last_pos < current_pos:  # moving negative to positive
            if (current_pos + move_length) > dim:  # moving same direction takes us out of axis range
                last_pos = current_pos  # update position
                current_pos -= move_length  # direction change
            else:
                last_pos = current_pos  # update position
                current_pos += move_length  # continue same direction
        elif last_pos > current_pos:  # moving positive to negative
            if (current_pos - move_length) < 5:  # if out of range (don't want it to be quite 0)
                last_pos = current_pos  # update position
                current_pos += move_length  # change direction
            else:
                last_pos = current_pos  # update position
                current_pos -= move_length  # continue same direction

    return current_pos, last_pos


# takes in x, y, and z distances, finds speed of combined move
def vector_finder(x_: float, y_: float, z_: float) -> float:
    vec_length: float = math.sqrt(x_ ** 2 + y_ ** 2 + z_ ** 2)
    return vec_length / (15 / tempo) * 60





##### main #####
# create arrays to hold notes
melody_notes: list[str] = []
mid_notes: list[str] = []
bass_notes: list[str] = []

current_x: float = 10.0
current_y: float = y_dim/2
current_z: float = z_dim/2

last_x: float = current_x
last_y: float = current_y
last_z: float = current_z

melody: str = f'{song_directory}/melody.txt'
mid: str = f'{song_directory}/mid.txt'
bass: str = f'{song_directory}/bass.txt'

# read in melody, mid, and bass from .txt files
with open(melody, "r") as f:
    for line in f:
        if line[0] not in comment:
            melody_notes.append(line.rstrip())

with open(mid, "r") as f:
    for line in f:
        if line[0] not in comment:
            mid_notes.append(line.rstrip())

with (open(bass, "r") as f):
    for line in f:
        if line[0] not in comment:
            bass_notes.append(line.rstrip())

##### ERROR CHECKING #####
if (len(melody_notes) != len(mid_notes)) or (len(melody_notes) != len(bass_notes)) or (len(mid_notes) != len(bass_notes)):
    print('Different amount of notes in files')
    print(f'Melody: {len(melody_notes)}  Mid: {len(mid_notes)}  Bass: {len(bass_notes)}')

# assemble text file name
file_name: str = f'{song_directory}/{song_name}.gcode'

with open(file_name, 'w') as file:
    file.write(f'G28\nG1 X{current_x} Y{current_y} Z{current_z} F2000\nG4 P1000\nM118 Now playing: {song_name}\n')

    # translate notes into speeds
    for i in range(0, len(melody_notes) - 1):
        # check if there are any notes playing on current beat - if not, issue a pause
        if melody_notes[i] == 'r' and mid_notes[i] == 'r' and bass_notes[i] == 'r':
            file.write(f"G4 P{15 / tempo * 1000}\n")
        else:
            current_x, last_x = kinematics(frequency_finder(melody_notes[i], md.melody_dictionary), melody_notes[i], melody_notes[i-1], x_dim, current_x, last_x)
            current_y, last_y = kinematics(frequency_finder(mid_notes[i], md.mid_dictionary), mid_notes[i], mid_notes[i - 1], y_dim, current_y, last_y)
            current_z, last_z = kinematics(frequency_finder(bass_notes[i], md.bass_dictionary), bass_notes[i], bass_notes[i - 1], z_dim, current_z, last_z)

            dist_x = current_x - last_x
            dist_y = current_y - last_y
            dist_z = current_z - last_z

            feedrate = vector_finder(dist_x, dist_y, dist_z)

            file.write(f"G1 X{current_x} Y{current_y} Z{current_z} F{feedrate}\n")


# if __name__ == '__main__':
#     pass
