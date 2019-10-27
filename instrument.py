# IMPORTANT: You need to install the playSound module with "pip3 install playsound" (On Linux terminal) for this to work.
# To use: run in shell with "python3 playingSound.py".
# Commands are: "up" to move up a chord, "actionwn" to move down a chord, "play" to play the sound and "exit" to exit.

from playsound import playsound

class instrument():
    """
    This class creates a musical instrument object. Sounds must be provided as mp3. Requires the playsound module.
    
    Instance Variables:
        
        chord_list (list): Contains the names of the mp3 files as Strings.
        chord_number (int): Keeps track of what chord we are on. Used to pick an element in chord_list at index chord_number.
    
    Constructor:
        
        instrument(mp3_sounds_filename): 
            Creates an instrument object. The parameter must be the name of a file. The file must contain the names
            of all the mp3 files to be used. All of the names must be on seperate lines each.

    Public Functions:

        play(signal): 
            Preforms an action on the musical insturment. Can either change chord, play the chord or do nothing.
            The signal parameter is an integer between 1 to 4. 
                      
            1 - moves the chord actionwn. 
            2 - moves the chord up.
            3 - plays the current chord.
            4 - simply actiones nothing (Left for additional functionality later on).
    """
    

    # Contructor to make a musical intrument.
    def __init__(self, mp3_sounds_filename):
        self.chord_list = []
        self.chord_number = 0
        self.mp3_sounds_filename = mp3_sounds_filename
        
        self.__gen_list_instrument()
    
    
    # Private function to generate a chord list for the instrument.
    def __gen_list_instrument(self):
        with open(self.mp3_sounds_filename, "r") as f:
            for line in f:
                self.chord_list.append(line.strip())


    # This function recieves a signal and preforms an action on an instrument object.
    def action(self, signal):
        # Check what kind of signal we have recieved.  
        if signal == 1:
            if self.chord_number == 0:
                print("At lowest possible chord")
            else: 
                self.chord_number -= 1
                print("Chord moved down")
            print(f"Chord number: {self.chord_number}")
        elif signal == 2:
            if self.chord_number == len(self.chord_list) - 1:
                print("At highest possible chord")
            else:
                self.chord_number += 1
                print("Chord moved up")
            print(f"Chord number: {self.chord_number}")
        elif signal == 3:
            print("Playing sound")
            playsound(self.chord_list[self.chord_number])
        elif signal == 4:
            pass

