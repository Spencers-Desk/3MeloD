import math
from config import ProjectConfig, SongConfig

# Default name for the project configuration file.
config_default_name: str = "config.txt"

project_config: ProjectConfig = ProjectConfig()
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
song_name, song_directory = song_config.get_song_properties()

# tempo of the song - sixteenth note is unit - if you used an eighth note rhythm divide your tempo by 2
tempo = song_config.get_song_tempo()

#song octave adjustment. It is free to adjust as needed
x_octave_adj, y_octave_adj, z_octave_adj = song_config.get_song_octaves_adjustment()

# Comment characters - use this to add characters that indicated a comment
comment = ['', ' ', '#', '\n']



##### END OF INPUTS - ONLY NERDS MAY PASS THIS LINE #####

# reference frequency
f_ref = 440  #Hz "A4"

# steps per revolution divided by distance per revolution = steps/distance
x_stepdist = (360/x_ang) / x_rpr
y_stepdist = (360/y_ang) / y_rpr
z_stepdist = (360/z_ang) / z_rpr

x_A4_feedrate = (f_ref / x_stepdist) * 60 * 2**x_octave_adj
y_A4_feedrate = (f_ref / y_stepdist) * 60 * 2**y_octave_adj
z_A4_feedrate = (f_ref / z_stepdist) * 60 * 2**z_octave_adj



##### Note Dictionaries #####
melody_dictionary = {
    'ref': x_A4_feedrate,  # A4 ~ 440Hz
    'E2': -29,
    'e2': -29,
    'F2': -28,
    'f2': -28,
    'Fs2': -27,
    'fs2': -27,
    'Gf2': -27,
    'gf2': -27,
    'G2': -26,
    'g2': -26,
    'Gs2': -25,
    'gs2': -25,
    'Af2': -25,
    'af2': -25,
    'A2': -24,
    'a2': -24,
    'As2': -23,
    'as2': -23,
    'Bf2': -23,
    'bf2': -23,
    'B2': -22,
    'b2': -22,
    'C3': -21,
    'c3': -21,
    'Cs3': -20,
    'cs3': -20,
    'Df3': -20,
    'df3': -20,
    'D3': -19,
    'd3': -19,
    'Ds3': -18,
    'ds3': -18,
    'Ef3': -18,
    'ef3': -18,
    'E3': -17,
    'e3': -17,
    'F3': -16,
    'f3': -16,
    'Fs3': -15,
    'fs3': -15,
    'Gf3': -15,
    'gf3': -15,
    'G3': -14,
    'g3': -14,
    'Gs3': -13,
    'gs3': -13,
    'Af3': -13,
    'af3': -13,
    'A3': -12,
    'a3': -12,
    'As3': -11,
    'as3': -11,
    'Bf3': -11,
    'bf3': -11,
    'B3': -10,
    'b3': -10,
    'C4': -9,
    'c4': -9,
    'Cs4': -8,
    'cs4': -8,
    'Df4': -8,
    'df4': -8,
    'D4': -7,
    'd4': -7,
    'Ds4': -6,
    'ds4': -6,
    'Ef4': -6,
    'ef4': -6,
    'E4': -5,
    'e4': -5,
    'F4': -4,
    'f4': -4,
    'Fs4': -3,
    'fs4': -3,
    'Gf4': -3,
    'gf4': -3,
    'G4': -2,
    'g4': -2,
    'Gs4': -1,
    'gs4': -1,
    'Af4': -1,
    'af4': -1,
    'A4': 0,
    'a4': 0,
    'As4': 1,
    'as4': 1,
    'Bf4': 1,
    'bf4': 1,
    'B4': 2,
    'b4': 2,
    'C5': 3,
    'c5': 3,
    'Cs5': 4,
    'cs5': 4,
    'Df5': 4,
    'df5': 4,
    'D5': 5,
    'd5': 5,
    'Ds5': 6,
    'ds5': 6,
    'Ef5': 6,
    'ef5': 6,
    'E5': 7,
    'e5': 7,
    'F5': 8,
    'f5': 8,
    'Fs5': 9,
    'fs5': 9,
    'Gf5': 9,
    'gf5': 9,
    'G5': 10,
    'g5': 10,
    'Gs5': 11,
    'gs5': 11,
    'Af5': 11,
    'af5': 11,
    'A5': 12,
    'a5': 12,
    'As5': 13,
    'as5': 13,
    'Bf5': 13,
    'bf5': 13,
    'B5': 14,
    'b5': 14,
    'C6': 15,
    'c6': 15,
    'Cs6': 16,
    'cs6': 16,
    'Df6': 16,
    'df6': 16,
    'D6': 17,
    'd6': 17,
    'Ds6': 18,
    'ds6': 18,
    'Ef6': 18,
    'ef6': 18,
    'E6': 19,
    'e6': 19,
    'F6': 20,
    'f6': 20,
    'Fs6': 21,
    'fs6': 21,
    'Gf6': 21,
    'gf6': 21,
    'G6': 22,
    'g6': 22,
    'Gs6': 23,
    'gs6': 23,
    'Af6': 23,
    'af6': 23,
    'A6': 24,
    'a6': 24
}

mid_dictionary = {
    'ref': y_A4_feedrate, #4225  # issue
    'E2': -29,
    'e2': -29,
    'F2': -28,
    'f2': -28,
    'Fs2': -27,
    'fs2': -27,
    'Gf2': -27,
    'gf2': -27,
    'G2': -26,
    'g2': -26,
    'Gs2': -25,
    'gs2': -25,
    'Af2': -25,
    'af2': -25,
    'A2': -24,
    'a2': -24,
    'As2': -23,
    'as2': -23,
    'Bf2': -23,
    'bf2': -23,
    'B2': -22,
    'b2': -22,
    'C3': -21,
    'c3': -21,
    'Cs3': -20,
    'cs3': -20,
    'Df3': -20,
    'df3': -20,
    'D3': -19,
    'd3': -19,
    'Ds3': -18,
    'ds3': -18,
    'Ef3': -18,
    'ef3': -18,
    'E3': -17,
    'e3': -17,
    'F3': -16,
    'f3': -16,
    'Fs3': -15,
    'fs3': -15,
    'Gf3': -15,
    'gf3': -15,
    'G3': -14,
    'g3': -14,
    'Gs3': -13,
    'gs3': -13,
    'Af3': -13,
    'af3': -13,
    'A3': -12,
    'a3': -12,
    'As3': -11,
    'as3': -11,
    'Bf3': -11,
    'bf3': -11,
    'B3': -10,
    'b3': -10,
    'C4': -9,
    'c4': -9,
    'Cs4': -8,
    'cs4': -8,
    'Df4': -8,
    'df4': -8,
    'D4': -7,
    'd4': -7,
    'Ds4': -6,
    'ds4': -6,
    'Ef4': -6,
    'ef4': -6,
    'E4': -5,
    'e4': -5,
    'F4': -4,
    'f4': -4,
    'Fs4': -3,
    'fs4': -3,
    'Gf4': -3,
    'gf4': -3,
    'G4': -2,
    'g4': -2,
    'Gs4': -1,
    'gs4': -1,
    'Af4': -1,
    'af4': -1,
    'A4': 0,
    'a4': 0,
    'As4': 1,
    'as4': 1,
    'Bf4': 1,
    'bf4': 1,
    'B4': 2,
    'b4': 2,
    'C5': 3,
    'c5': 3,
    'Cs5': 4,
    'cs5': 4,
    'Df5': 4,
    'df5': 4,
    'D5': 5,
    'd5': 5,
    'Ds5': 6,
    'ds5': 6,
    'Ef5': 6,
    'ef5': 6,
    'E5': 7,
    'e5': 7,
    'F5': 8,
    'f5': 8,
    'Fs5': 9,
    'fs5': 9,
    'Gf5': 9,
    'gf5': 9,
    'G5': 10,
    'g5': 10,
    'Gs5': 11,
    'gs5': 11,
    'Af5': 11,
    'af5': 11,
    'A5': 12,
    'a5': 12,
    'As5': 13,
    'as5': 13,
    'Bf5': 13,
    'bf5': 13,
    'B5': 14,
    'b5': 14,
    'C6': 15,
    'c6': 15,
    'Cs6': 16,
    'cs6': 16,
    'Df6': 16,
    'df6': 16,
    'D6': 17,
    'd6': 17,
    'Ds6': 18,
    'ds6': 18,
    'Ef6': 18,
    'ef6': 18,
    'E6': 19,
    'e6': 19,
    'F6': 20,
    'f6': 20,
    'Fs6': 21,
    'fs6': 21,
    'Gf6': 21,
    'gf6': 21,
    'G6': 22,
    'g6': 22,
    'Gs6': 23,
    'gs6': 23,
    'Af6': 23,
    'af6': 23,
    'A6': 24,
    'a6': 24
}

bass_dictionary = {
    'ref': z_A4_feedrate,
    'E1':-41,
    'e1':-41,
    'F1': -40,
    'f1': -40,
    'Fs1': -39,
    'fs1': -39,
    'Gf1': -39,
    'gf1': -39,
    'G1': -38,
    'g1': -38,
    'Gs1': -37,
    'gs1': -37,
    'Af1': -37,
    'af1': -37,
    'A1': -36,
    'a1': -36,
    'As1': -35,
    'as1': -35,
    'Bf1': -35,
    'bf1': -35,
    'B1': -34,
    'b1': -34,
    'C2': -33,
    'c2': -33,
    'Cs2': -32,
    'cs2': -32,
    'Df2': -32,
    'df2': -32,
    'D2': -31,
    'd2': -31,
    'Ds2': -30,
    'ds2': -30,
    'Ef2': -30,
    'ef2': -30,
    'E2': -29,
    'e2': -29,
    'F2': -28,
    'f2': -28,
    'Fs2': -27,
    'fs2': -27,
    'Gf2': -27,
    'gf2': -27,
    'G2': -26,
    'g2': -26,
    'Gs2': -25,
    'gs2': -25,
    'Af2': -25,
    'af2': -25,
    'A2': -24,
    'a2': -24,
    'As2': -23,
    'as2': -23,
    'Bf2': -23,
    'bf2': -23,
    'B2': -22,
    'b2': -22,
    'C3': -21,
    'c3': -21,
    'Cs3': -20,
    'cs3': -20,
    'Df3': -20,
    'df3': -20,
    'D3': -19,
    'd3': -19,
    'Ds3': -18,
    'ds3': -18,
    'Ef3': -18,
    'ef3': -18,
    'E3': -17,
    'e3': -17,
    'F3': -16,
    'f3': -16,
    'Fs3': -15,
    'fs3': -15,
    'Gf3': -15,
    'gf3': -15,
    'G3': -14,
    'g3': -14,
    'Gs3': -13,
    'gs3': -13,
    'Af3': -13,
    'af3': -13,
    'A3': -12,
    'a3': -12,
    'As3': -11,
    'as3': -11,
    'Bf3': -11,
    'bf3': -11,
    'B3': -10,
    'b3': -10,
    'C4': -9,
    'c4': -9,
    'Cs4': -8,
    'cs4': -8,
    'Df4': -8,
    'df4': -8,
    'D4': -7,
    'd4': -7,
    'Ds4': -6,
    'ds4': -6,
    'Ef4': -6,
    'ef4': -6,
    'E4': -5,
    'e4': -5,
    'F4': -4,
    'f4': -4,
    'Fs4': -3,
    'fs4': -3,
    'Gf4': -3,
    'gf4': -3,
    'G4': -2,
    'g4': -2,
    'Gs4': -1,
    'gs4': -1,
    'Af4': -1,
    'af4': -1,
    'A4': 0,
    'a4': 0,
    'As4': 1,
    'as4': 1,
    'Bf4': 1,
    'bf4': 1,
    'B4': 2,
    'b4': 2,
    'C5': 3,
    'c5': 3,
    'Cs5': 4,
    'cs5': 4,
    'Df5': 4,
    'df5': 4,
    'D5': 5,
    'd5': 5,
    'Ds5': 6,
    'ds5': 6,
    'Ef5': 6,
    'ef5': 6,
    'E5': 7,
    'e5': 7,
    'F5': 8,
    'f5': 8,
    'Fs5': 9,
    'fs5': 9,
    'Gf5': 9,
    'gf5': 9,
    'G5': 10,
    'g5': 10,
    'Gs5': 11,
    'gs5': 11,
    'Af5': 11,
    'af5': 11,
    'A5': 12,
    'a5': 12,
    'As5': 13,
    'as5': 13,
    'Bf5': 13,
    'bf5': 13,
    'B5': 14,
    'b5': 14,
    'C6': 15,
    'c6': 15,
    'Cs6': 16,
    'cs6': 16,
    'Df6': 16,
    'df6': 16,
    'D6': 17,
    'd6': 17,
    'Ds6': 18,
    'ds6': 18,
    'Ef6': 18,
    'ef6': 18,
    'E6': 19,
    'e6': 19,
    'F6': 20,
    'f6': 20,
    'Fs6': 21,
    'fs6': 21,
    'Gf6': 21,
    'gf6': 21,
    'G6': 22,
    'g6': 22,
    'Gs6': 23,
    'gs6': 23,
    'Af6': 23,
    'af6': 23,
    'A6': 24,
    'a6': 24
}




##### functions #####

# takes in note and dictionary, spits out feedrate for one axis
def frequency_finder(note, dictionary):
    global tempo

    if note == 'r':  # checking for a rest
        return 0  # return feed rate of 0 for rests
    elif note not in dictionary:
        print(f'Incorrect note found at: {i} (note will be after this line more than likely) Note: {note}')
    else:
        return dictionary['ref'] * 2 ** (dictionary[note] / 12)    # (reference speed) * 2^((note offset)/12)


def kinematics(speed, this_note, last_note, dim, current_pos, last_pos):
    global tempo

    mid_pos = dim/2
    move_length = speed / 60 * (15 / tempo)

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
def vector_finder(x_, y_, z_):
    vec_length = math.sqrt(x_ ** 2 + y_ ** 2 + z_ ** 2)
    return vec_length / (15 / tempo) * 60





##### main #####
# create arrays to hold notes
melody_notes = []
mid_notes = []
bass_notes = []

current_x = 10
current_y = y_dim/2
current_z = z_dim/2

last_x = current_x
last_y = current_y
last_z = current_z

melody = song_directory
mid = song_directory
bass = song_directory
melody += "/melody.txt"
mid += "/mid.txt"
bass += "/bass.txt"

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
file_name = song_directory
file_name += '/'
file_name += song_name
file_name += '.gcode'


myfile = open(file_name, 'w')


# write start gcode to file
start_gcode = 'G28\n'  # home printer
start_gcode += 'G1 X'  # move to start position
start_gcode += str(current_x)
start_gcode += ' Y'
start_gcode += str(current_y)
start_gcode += ' Z'
start_gcode += str(current_z)
start_gcode += ' F2000\n'
# pause for 1 second
start_gcode += 'G4 P1000\n'  # brief pause
start_gcode += 'M118 Now playing: '
start_gcode += song_name
start_gcode += '\n'

myfile.write(start_gcode)

# translate notes into speeds
for i in range(0, len(melody_notes) - 1):
    # check if there are any notes playing on current beat - if not, issue a pause
    if melody_notes[i] == 'r' and mid_notes[i] == 'r' and bass_notes[i] == 'r':
        myfile.write(f"G4 P{15 / tempo * 1000}\n")
    else:
        current_x, last_x = kinematics(frequency_finder(melody_notes[i], melody_dictionary), melody_notes[i], melody_notes[i-1], x_dim, current_x, last_x)
        current_y, last_y = kinematics(frequency_finder(mid_notes[i], mid_dictionary), mid_notes[i], mid_notes[i - 1], y_dim, current_y, last_y)
        current_z, last_z = kinematics(frequency_finder(bass_notes[i], bass_dictionary), bass_notes[i], bass_notes[i - 1], z_dim, current_z, last_z)

        dist_x = current_x - last_x
        dist_y = current_y - last_y
        dist_z = current_z - last_z

        feedrate = vector_finder(dist_x, dist_y, dist_z)

        myfile.write(f"G1 X{current_x} Y{current_y} Z{current_z} F{feedrate}\n")

myfile.close()



