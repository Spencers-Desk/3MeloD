import math

##### Inputs #####
# you need to have the melody.txt, mid.txt, and bass.txt inside a folder named after the song
# Song name (directory)
song_name = "Sea Shanty 2"

# Position you want printer to start in (mm)
start_x = 100
start_y = 100
start_z = 50


# tempo of the song
tempo = 100  #bpm

# reference note
x_A4 = 10600
y_A4 = 8450
z_A3 = 525


##### END OF INPUTS - ONLY NERDS MAY PASS THIS LINE #####





##### Note Dictionaries #####
melody_dictionary = {
    'ref': x_A4,  # A4 ~ 440Hz
    'G3': -14,
    'Gs3': -13,
    'Af3': -13,
    'A3': -12,
    'As3': -11,
    'Bf3': -11,
    'B3': -10,
    'C4': -9,
    'Cs4': -8,
    'Df4': -8,
    'D4': -7,
    'Ds4': -6,
    'Ef4': -6,
    'E4': -5,
    'F4': -4,
    'Fs4': -3,
    'Gf4': -3,
    'G4': -2,
    'Gs4': -1,
    'Af4': -1,
    'A4': 0,
    'As4': 1,
    'Bf4': 1,
    'B4': 2,
    'C5': 3,
    'Cs5': 4,
    'Df5': 4,
    'D5': 5,
    'Ds5': 6,
    'Ef5': 6,
    'E5': 7,
    'F5': 8,
    'Fs5': 9,
    'Gf5': 9,
    'G5': 10,
    'Gs5': 11,
    'Af5': 11,
    'A5': 12,
    'As5': 13,
    'Bf5': 13,
    'B5': 14,
    'C6': 15,
    'Cs6': 16,
    'Df6': 16,
    'D6': 17,
    'Ds6': 18,
    'Ef6': 18,
    'E6': 19,
    'F6': 20,
    'Fs6': 21,
    'Gf6': 21,
    'G6': 22,
    'Gs6': 23,
    'Af6': 23,
    'A6': 24
}

mid_dictionary = {
    'ref': y_A4, #4225  # issue
    'A2': -24,
    'As2': -23,
    'Bf2': -23,
    'B2': -22,
    'C3': -21,
    'Cs3': -20,
    'Df3': -20,
    'D3': -19,
    'Ds3': -18,
    'Ef3': -18,
    'E3': -17,
    'F3': -16,
    'Fs3': -15,
    'Gf3': -15,
    'G3': -14,
    'Gs3': -13,
    'Af3': -13,
    'A3': -12,
    'As3': -11,
    'Bf3': -11,
    'B3': -10,
    'C4': -9,
    'Cs4': -8,
    'Df4': -8,
    'D4': -7,
    'Ds4': -6,
    'Ef4': -6,
    'E4': -5,
    'F4': -4,
    'Fs4': -3,
    'Gf4': -3,
    'G4': -2,
    'Gs4': -1,
    'Af4': -1,
    'A4': 0,
    'As4': 1,
    'Bf4': 1,
    'B4': 2,
    'C5': 3,
    'Cs5': 4,
    'Df5': 4,
    'D5': 5,
    'Ds5': 6,
    'Ef5': 6,
    'E5': 7,
    'F5': 8,
    'Fs5': 9,
    'Gf5': 9,
    'G5': 10,
    'Gs5': 11,
    'Af5': 11,
    'A5': 12,
    'As5': 13,
    'Bf5': 13,
    'B5': 14,
    'C6': 15,
    'Cs6': 16,
    'Df6': 16,
    'D6': 17,
    'Ds6': 18,
    'Ef6': 18,
    'E6': 19,
    'F6': 20,
    'Fs6': 21,
    'Gf6': 21,
    'G6': 22,
    'Gs6': 23,
    'Af6': 23,
    'A6': 24
}

bass_dictionary = {
    'ref': z_A3,
    'E1':-29,
    'F1': -28,
    'Fs1': -27,
    'Gf1': -27,
    'G1': -26,
    'Gs1': -25,
    'Af1': -25,
    'A1': -24,
    'As1': -23,
    'Bf1': -23,
    'B1': -22,
    'C2': -21,
    'Cs2': -20,
    'Df2': -20,
    'D2': -19,
    'Ds2': -18,
    'Ef2': -18,
    'E2': -17,
    'F2': -16,
    'Fs2': -15,
    'Gf2': -15,
    'G2': -14,
    'Gs2': -13,
    'Af2': -13,
    'A2': -12,
    'As2': -11,
    'Bf2': -11,
    'B2': -10,
    'C3': -9,
    'Cs3': -8,
    'Df3': -8,
    'D3': -7,
    'Ds3': -6,
    'Ef3': -6,
    'E3': -5,
    'F3': -4,
    'Fs3': -3,
    'Gf3': -3,
    'G3': -2,
    'Gs3': -1,
    'Af3': -1,
    'A3': 0,
    'As3': 1,
    'Bf3': 1,
    'B3': 2,
    'C4': 3,
    'Cs4': 4,
    'Df4': 4,
    'D4': 5,
    'Ds4': 6,
    'Ef4': 6,
    'E4': 7,
    'F4': 8,
    'Fs4': 9,
    'Gf4': 9,
    'G4': 10,
    'Gs4': 11,
    'Af4': 11,
    'A4': 12,
}


##### functions #####

# takes in note and dictionary, spits out feedrate for one axis
def frequency_finder(note, dictionary):
    global tempo

    if note == 'r':
        return 0  # return feed rate of 0 for rests
    else:
        return dictionary['ref'] * 2 ** (dictionary[note] / 12)    # (reference speed) * 2^((note offset)/12)



# X kinematics
def x(speed, this_note, last_note):
    global tempo
    global current_x
    global last_x

    move_length = speed / 60 * (15 / tempo)
    if this_note != last_note: # different note being played
        if current_x <= 125:
            last_x = current_x
            current_x = current_x + move_length
        elif current_x > 125:
            last_x = current_x
            current_x = current_x - move_length
        else:
            print('Error traveled outside X range')
    if this_note == last_note and last_x < current_x: # moving negative to positive
        if (current_x + move_length) < 250:
            last_x = current_x
            current_x = current_x + move_length
        else:
            last_x = current_x
            current_x = current_x - move_length
    if this_note == last_note and last_x > current_x: # moving positive to negative
        if (current_x - move_length) > 5:
            last_x = current_x
            current_x = current_x - move_length
        else:
            last_x = current_x
            current_x = current_x + move_length



# Y kinematics
def y(speed, this_note, last_note):
    global tempo
    global current_y
    global last_y

    move_length = speed / 60 * (15 / tempo)
    if this_note != last_note: # different note being played
        if current_y <= 125:
            last_y = current_y
            current_y = current_y + move_length
        elif current_y > 125:
            last_y = current_y
            current_y = current_y - move_length
        else:
            print('Error traveled outside y range')
    if this_note == last_note and last_y < current_y: # moving negative to positive
        if (current_y + move_length) < 250:
            last_y = current_y
            current_y = current_y + move_length
        else:
            last_y = current_y
            current_y = current_y - move_length
    if this_note == last_note and last_y > current_y: # moving positive to negative
        if (current_y - move_length) > 5:
            last_y = current_y
            current_y = current_y - move_length
        else:
            last_y = current_y
            current_y = current_y + move_length


# Z kinematics
def z(speed, this_note, last_note):
    global tempo
    global current_z
    global last_z

    move_length = speed / 60 * (15 / tempo)
    if this_note != last_note: # different note being played
        if current_z <= 50:
            last_z = current_z
            current_z = current_z + move_length
        elif current_z > 50:
            last_z = current_z
            current_z = current_z - move_length
        else:
            print('Error traveled outside z range')
    if this_note == last_note and last_z < current_z: # moving negative to positive
        if (current_z + move_length) < 250:
            last_z = current_z
            current_z = current_z + move_length
        else:
            last_z = current_z
            current_z = current_z - move_length
    if this_note == last_note and last_z > current_z: # moving positive to negative
        if (current_z - move_length) > 5:
            last_z = current_z
            current_z = current_z - move_length
        else:
            last_z = current_z
            current_z = current_z + move_length

# takes in x, y, and z distances, finds speed of combined move
def vector_finder(x_, y_, z_):
    vec_length = math.sqrt(x_ ** 2 + y_ ** 2 + z_ ** 2)
    return vec_length / (15 / tempo) * 60





##### main #####
# create arrays to hold notes
melody_notes = []
mid_notes = []
bass_notes = []

# "last" position doesn't exist yet, so is defined here
current_x = start_x
current_y = start_y
current_z = start_z

last_x = start_x
last_y = start_y
last_z = start_z

melody = song_name
mid = song_name
bass = song_name
melody += "/melody.txt"
mid += "/mid.txt"
bass += "/bass.txt"

# read in melody, mid, and bass from .txt files
with open(melody, "r") as f:
    for line in f:
        melody_notes.append(line.rstrip())

with open(mid, "r") as f:
    for line in f:
        mid_notes.append(line.rstrip())

with open(bass, "r") as f:
    for line in f:
        bass_notes.append(line.rstrip())



# create arrays that hold movement speed for melody (x), mid (y), and bass (z)
melody_speed = []
mid_speed = []
bass_speed = []

# assemble text file name
file_name = song_name
file_name += '/'
file_name += song_name
file_name += '.gcode'

# write start gcode to file
myfile = open(file_name, 'w')
# home printer
start_gcode = "G28\n"
# move to start position
start_gcode += "G1 X"
start_gcode += str(start_x)
start_gcode += " Y"
start_gcode += str(start_y)
start_gcode += " Z"
start_gcode += str(start_z)
start_gcode += " F1000\n"
# pause for 1 second
start_gcode += "G4 P1000\n"

myfile.write(start_gcode)

# translate notes into speeds
for i in range(0, len(melody_notes) - 1):
    # check if there are any notes playing on current beat - if not, issue a pause
    if melody_notes[i] == 'r' and mid_notes[i] == 'r' and bass_notes[i] == 'r':
        myfile.write(f"G4 P{15 / tempo * 1000}\n")
    #
    else:
        melody_speed.append(x(frequency_finder(melody_notes[i], melody_dictionary), melody_notes[i], melody_notes[i-1]))
        mid_speed.append(y(frequency_finder(mid_notes[i], mid_dictionary), mid_notes[i], mid_notes[i-1]))
        bass_speed.append(z(frequency_finder(bass_notes[i], bass_dictionary), bass_notes[i], bass_notes[i-1]))

        dist_x = current_x - last_x
        dist_y = current_y - last_y
        dist_z = current_z - last_z

        feedrate = vector_finder(dist_x, dist_y, dist_z)

        myfile.write(f"G1 X{current_x} Y{current_y} Z{current_z} F{feedrate}\n")

myfile.close()

#    with open("melody.txt", "w") as text_file:
#    print(f"G4 P{quarter*tempo}", file=text_file)

# Given C_sharp sixteenth note & Current X
# Want G1 X{current + Cs5/60*sixteenth} F{Cs}


# at any given note
# find feed rate for melody, mid, and bass
# find distance for each to travel
# find feed rate for three axis to travel at once
# G1 X1523689 Y16235786 Z167892345 F######
