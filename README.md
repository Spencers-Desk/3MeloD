# 3MeloD
An attempt at bringing music to your 3D printer =)

 ## Getting .gcode for your 3D Printer
 Welcome to 3MeloD! This is an actively changing project undergoing many changes. A good start is watching the first 10 minutes of the video below (click the image).

 [![3MeloD Tutorial/Code Breakdown](https://img.youtube.com/vi/KTuAyzkVVfQ/0.jpg)](https://www.youtube.com/watch?v=KTuAyzkVVfQ)

 ### Download Required Software
 You're going to need to download a few different things to get started (this won't be the case in the future).

 1. Python3 - https://www.python.org/downloads/
 2. PyCharm (or prefered IDE) - https://www.jetbrains.com/pycharm/
 3. GitHub repository - https://github.com/Spencers-Desk/3MeloD

The video above can walk you through this section.

### Configuration File

Next, you should find some information about your printer. If you don't have a configuration file (you're not running Klipper) go to the following link and find the configuration for your printer (more than likely one exists)

https://github.com/Klipper3d/klipper/blob/master/config/printer-creality-ender3-v2-2020.cfg

Once all of the software is downloaded, you're going to need open up 3MeloD as a project in your IDE. Now you're going to need to fill out the configuration file.

[config.txt](config.txt)

First you will fill out the angle per step for each of your stepper motors. More than likely, you can leave them as 3.6.

Next you will add the distance travelled per stepper motor revolution. This is where the Klipper configuration file comes in handy. For example going into the above link to the Ender 3v2 configuration file, you can see the following...

```
[stepper_x]
step_pin: PC2
dir_pin: PB9
enable_pin: !PC3
microsteps: 16
rotation_distance: 40
endstop_pin: ^PA5
position_endstop: 0
position_max: 235
homing_speed: 50
```

The line we are interested in is `rotation distance: 40`. Get this for your x, y, and z axis and fill in the config.txt file.

Finally, insert the dimensions of your printer, but a little smaller. For instance, if your printer is 250x250x250 then input 240x240x240. (This isn't strictly necessary, just out of caution).

### .gcode Generation

Now it is time to actually generate some .gcode.

First, you need to select what song you want to generate .gcode for. Assuming that the song is either from the main repository or has been formatted following the repository example, you will only need to edit the song name in the config.txt file. For example, you would change the "Megalovania" part of the below code, to the name of the folder your song's .txt files are stored in. For example, "Sea Shanty 2" is a directory holding the files for the song "Sea Shanty 2".

```
config_filepath = "Megalovania/song_config.txt"
```

If you wish to change anything about the song itself, you can do so in the respective songs `song_config.txt` file. Things like tempo, octave shift, etc.

Once yuu've prepped the config files, the only thing left to do is to run the script. It will spit out a .gcode file. You then either copy this file or its contents to your printer as you would with any other .gcode file.

<br />

## Transcriping your own music

If you wish to transcribe your own music, I would highly recommend watching the tutorial video linked at the top of this page. Below is the jist of transcribing though.

### Notes
Notes are written as `A4, B4, C3` etc... `A4` is the A just above middle C, defined as 440Hz.

### Rhythm
Within a .txt file, every line represent a sixteenth note. So, if you wanted to play an A4 as a sixteenth note, this would be the resulting .txt.
```
A4
```
If you wanted to play 2 sixteenth notes, both A4, you would type the following...
```
A4
a4
```
Note the difference in capitalization. When you want to play the same note and have it sound rhythmically distinct from the last, you need to change the capitzliation. If you want to play different notes, the capitzliation will not affect the music. i.e.
```
A4
B4
```
is the same as
```
A4
b4
```
or any permutation.
If you want to play rhythms that are longer than a sixteenth note, this is how you'd go about that. Imagine you want to play an A4 as an eighth note, a B4 as a quarter note, and then an A4 as 2 sixteenth notes. This is the following .txt file for that.
```
A4
A4
B4
B4
B4
B4
A4
a4
```
Instead of an eighth note, visualize 2 sixteenth notes with a tie between them. Instead of a quarter note, imagine 4 sixteenth notes with a tie combining them all. This is how the music must be written.

### Rests

If you wish to have a rest, this works in the same way. The following is a rest.
```
r
```
If you wish to play a quarter rest, the same logic applies.
```
r
r
r
r
```
Capital R's will not work, must be lower case.

### Comments

If you wish to leave comments in your files, start the line with one of the following characters in the below example.
```
# This is a comment
```
If you're not a fan of using the `#` and want to define another character, you can do so in the 3MeloD.py file.
