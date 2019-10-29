# IMPORTANT: You need to install the playSound module with "pip3 install playsound" (On Linux terminal) for this to work.
# To use example: Run "playingSoundTest.py" or "hotCrossBuns.py"

import numpy as np
import os
import errno
# import simpleaudio as sa
# from pydub import AudioSegment
# from pydub.playback import play
from scipy.io.wavfile import write
from playsound import playsound

class instrument():
    """
    This class creates a musical instrument object. Sounds must be provided as mp3. Requires the playsound module.
    
    Instance Variables:
        
        chord_list (list): Contains the names of the mp3 files as Strings.
        chord_number (int): Keeps track of what chord we are on. Used to pick an element in chord_list at index chord_number.
        mp3_sounds_filename (String): The name of the file that contains all the mp3 files.
        sound_queue (list): A list containing all the names of sounds (.wav files) which have been queued up.
    
    Constructor:
        
        instrument(mp3_sounds_filename): 
            Creates an instrument object. The parameter must be the name of a file (As a String). The file must contain the names
            of all the mp3 files to be used. All of the names must be on seperate lines each.

    Public Functions:

        play(signal): 
            Preforms an action on the musical insturment. Can either change chord, play the chord or do nothing.
            The signal parameter is an integer between 1 to 4. 
                      
            1 - moves the chord actionwn. 
            2 - moves the chord up.
            3 - plays the current chord.
            4 - simply actiones nothing (Left for additional functionality later on).
    
        gen_sound(freq, time, play):
            Generates a mono-frequence sound. Parameters are "freq" which is the frequency, "time" which is the amount of
            time (in seconds) the sound is played for, and "play" which will play the sound immediately after generation
            if set to True. This function will generate a directory named "sound_files" if it does not already exist.

        queue_sound(freq, time):
            Adds a sound to the sound queue. Parameters are "freq" which is the frequency and "time" which is the amount
            of time (in seconds) the sound is played for.

        queue_play():
            Plays all the sounds in the sound queue.

        queue_clear():
            Clears the sound queue, making it an empty list again.
        
        queue_del():
            Removes the most recent item from the sound_queue.
    """
    

    # Contructor to make a musical intrument.
    def __init__(self, mp3_sounds_filename = None):
        if mp3_sounds_filename is None:
            self.chord_list = None
            self.sound_queue = []
        else:
            self.chord_list = []
            self.chord_number = 0
            self.mp3_sounds_filename = mp3_sounds_filename
            self.sound_queue = []

            self.__gen_list_instrument()
    

    # Private function to generate a chord list for the instrument.
    def __gen_list_instrument(self):
        with open(self.mp3_sounds_filename, "r") as f:
            for line in f:
                self.chord_list.append(line.strip())


    # This function recieves a signal and preforms an action on an instrument object.
    def action(self, signal):
        # Check to see if we have provided a text file.
        if self.chord_list == None:
            print("Instrument constructor must be called with a String argument in order to use the .action() function")
            return None
        
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


    # Generates a sound as a .wav file. Immediately plays the sound if "play" is set to True. Returns file_name.
    def gen_sound(self, freq = 300, time = 1, play = False):
        sampling_rate = 44100
        samples = 44100*time
        x = np.arange(samples)
        data = None
        scaled = None
        dir_path = None

        if freq == 0:
            file_name = f"./sound_files/silence_{freq}_{time}.wav"
            data = np.random.uniform(0, 0, int(samples))
            scaled = data
        else:
            file_name = f"./sound_files/sinewave_{freq}_{time}.wav"
            data = np.sin(2 * np.pi * freq * x / sampling_rate)
            scaled = np.int16(data/np.max(np.abs(data)) * 32767)

        dir_path = os.path.dirname(file_name)
        
        # Create directory if it does not already exist.
        if not os.path.exists(dir_path):
            try:
                os.makedirs(dir_path)
            except OSError as e:
                # Do not raise an error if the file already exists. Only raise if some other kind of error.
                # This stops race conditions.
                if e.errno != errno.EEXISTS:
                    raise 

        write(file_name, sampling_rate, scaled)
            
        if play == True:
            playsound(file_name)

        return file_name


    # Generates the sounds and adds them to a queue.
    def queue_sound(self, freq, time = 1):
        self.sound_queue.append(self.gen_sound(freq, time))
    

    # Plays all the sounds that have been queued
    def queue_play(self):
        for i in self.sound_queue:
            playsound(i)
    

    # Clears the sound_queue, making it an empty list again.
    def queue_clear(self):
        self.sound_queue.clear()

    
    # Removes the most recent item from the sound queue.
    def queue_del(self):
        self.sound_queue.pop()
