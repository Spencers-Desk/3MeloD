# To-Do List for 3MeloD

- [ ] Written tutorial for readme
- [ ] Start gcode
- [X] ~~separate config file for printer configuration (remove from 3MeloD.py)~~ ~ Accomplished by @jrfq98
- [ ] .gcode printer requirements printout
- [ ] add variable for changing subdivision method (15 / tempo)
- [ ] Web Server
- [ ] Create "Music" directory for all songs
- [ ] MIDI file read ins
- [ ] Tempo Switching
- [ ] Improved Rhythm Interpretation
- [ ] Core X-Y/X-Z kinematics



## QOL/Usability Improvements

### - Printer Select List
Printer config is widely available through the Klipper GitHub page. Creating a list of the most common printers from that
invaluable resource would allow 3MeloD users to select a printer from a list rather than finding and inputting their own
configuration. (configuration would still be available for custom/unaccounted for printers!)

### - Written tutorial for readme
How to use 3MeloD needs to be added to readme file

### - Start gcode
Adding an area to **config.txt** where you can write start gcode 

### - separate config file for printer configuration (remove from 3MeloD.py)

### - .gcode printer requirements printout
The higher the note, the higher the speed required to play the note. Adding a variable that tracks/function that finds the highest note in each .txt file. Output the max velocity for each axis.

### - add variable for changing subdivision method (15 / tempo)
Currently, music is interpreted as each .txt line being a sixteenth note. If a song doesn't contain sixteenth notes (i.e. an eigth note being the shortest value) then you'd have to write A4, A4, for an eighth note.

**Unsure if this is a good idea or not. Can currently be accomplished by halving/doubling tempo. Also, increasing subdivision to a quarter note could be an issue if a quarter note can't fit on an axis. This would require more kinematics considerations...**


### - Web Server
Hosting a web server for 3MeloD (like other peoples gcode webpages) would elimnate the user's need to download python, IDE, Github clone etc... Just choose the song/copy paste song, input printer config, generate .gcode.


### - Create "Music" directory for all songs
I'm not sure if this would help readability or not.


### - MIDI file read ins
Ability to read in MIDI files would be great. Unaware if there are apps to point and click to create music then generate midi file? If so, would be more accessible than typing the notes?




<br />

## Kinematics
How the 3MeloD.py script interprets and translates the .txt files to .gcode files.

### - Tempo Switching
Adding tempo switching ability eliminates splitting songs into multiple files. Add tempo changes to .txt files between notes (as if it were a comment), recording where tempo change occurs, tempo change after note 64 (between measure 4&5), record tempo_change = [65,...], tempos = [100] (would need to add a `start_tempo` variable. Have `tempo=start_tempo` in initialization section.
```
if i in tempo_change
  tempo = tempos[need to retrieve index] -tbd
```
This would make for easy tempo switching within the .txt files.



### - Improved Rhythm Interpretation
The longest rhythm value able to be played is determined by both the note pitch (velocity) and rhythm value (time spent @velocity). The length required is `distance = velocity * time`. Having the music be analyzed rather than one line at a time, it should be interpreted as one note at a time. i.e.
```
B4
A4
A4
A4
A4
C4
```
Rather than going line by line, this would be analyzed in 3 sections.
-Can we do the A4 in one move?
-is note (all A4 combined) able to be completed on one axis
-if yes, can we adjust past notes to make it happen?
-if no, how can we subdivide note to make it sound best? (split whole note in half rather than 1/4 & 3/4)




### - Core X-Y/X-Z kinematics
In its current state, 3MeloD assumes that movement along an axis (x, y, or z). Core-kinematic printers do not work in this way. A single stepper rotating would result in a diagonal motion in the core-plane of the printer.
- [ ] add printer kinematic variable to config.txt
```
printer_kinematics = cartesian #corexy #corexz #etc...
```
- [ ] add `if` statement to kinematics function
```
if printer_kinematics = cartesian
  current kinematics function
else if printer_kinematics = corexy
  core-xy kinematics
```
- [ ] create kinematics for cartesian printer (current function, just reformat)
- [ ] create kinematics for core-xy printer
- [ ] create kinematics for core-xz printer



<br />



