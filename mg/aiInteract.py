#purpose of this file is to be used to interact with our AI

#most functions within here are designed to simply parse what the users changes from the UI are into the training file.




import random
import numpy as np
import theAI
import fileinput
from UI import *

instrumentList = ["Piano", "Violin", "Flute"]
pianoArtistList = ["Bach", "Chopin", "Debussy", "Ellington", "Corea", "Anime"]
violinArtistList = ["Mozart", "Paganini", "Vivaldi"]
fluteArtistList = ["Brahms","Wagner"]
tempoList = ["Largo", "Adagio", "Andante", "Moderato", "Allegro", "Presto", "Slow", "Moderate", "Fast"]
def MusicTest(inst, artist, tempo, numMeasures, inputFile, showSheetMusic):
    # Parameter Checking
    if (inst == "Instrument"):
        inst = random.choice(instrumentList)
    if (inst == "Piano" and not artist in pianoArtistList):
        artist = random.choice(pianoArtistList)
    elif (inst == "Violin" and not artist in violinArtistList):
        artist = random.choice(violinArtistList)
    elif (inst == "Flute" and not artist in fluteArtistList):
        artist = random.choice(fluteArtistList)
    if (tempo == "Tempo"):
        tempo = random.choice(tempoList)

    # Fix the if statement for measure as it cannot be a str type, meaning we can't set nummeasures to "".
    if (numMeasures <= 0):
        numMeasures = random.randint(1, 100)
        

    # Adds more checks that handles some possible edge cases.
    # The following handles the case where user doesn;t select anything in the gui. If thats the case, error-message will be outputted,
    # and exit the program
    if not inst:
        print("Please select an instrument.")
        exit(1)
    if not artist:
        print ("Please select an artist.")
        exit(1)
    if not tempo:
        print ("Please select a tempo.")
        exit(1)

    
    # Now, need to check for the input file extension if user decides to import his or her's own tempo or notes.
    filePath = ['/ai']
    for inputFile in filePath:
        extension = os.path.splitext(inputFile)[-1].lower() # This will split the extension of the file. Youtube has a good tutuorial on this. 
        if extension == ". midi" or extension == " .txt":
            inputFile.open()
            if (inputFile.isempty()): # if the imported file is empty, user need to import a new file ends with ".midi" or ".txt" 
                print ("Please don't import an empty file!")
            else: 
               continue
    

    '''
    print(inst)
    print(artist)
    print(tempo)
    print(numMeasures)
    print(inputFile)
    print(showSheetMusic)
    '''

    theAI.generateMusic(inst, artist, tempo, numMeasures, inputFile, showSheetMusic) # Interact with the AI and generate the music.
    
    return inputFile
# MusicTest()