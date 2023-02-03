from keras.models import load_model
import random
import numpy as np
from music21 import *
from theAI import *

inst = ["Piano", "Violin", "Flute"]
tempi = ["Largo", "Adagio", "Andante", "Moderato", "Allegro", "Presto", "Slow", "Moderate", "Fast"]
pianoArtists = ["Bach", "Chopin", "Debussy", "Ellington", "Corea", "Anime"]
violinArtists = ["Mozart", "Paganini", "Vivaldi"]
fluteArtists = ["Brahms", "Wagner"]
showSheetMusic = False

def getInst():
    print("Available instruments:")
    print(inst)
    return input("Enter instrument: ")

def getArtist(inst):
    if inst == "Piano":
        print("Piano artists:")
        print(pianoArtists)
    elif inst == "Violin":
        print("Violin artists:")
        print(violinArtists)
    elif inst == "Flute":
        print("Flute artists:")
        print(fluteArtists)
    else:
        print("Artist for", inst, "not supported.")
        return "USER CHOICE ERROR"
    return input("Enter artist: ")

def getTempo():
    print("Tempi:")
    print(tempi)
    return (input("Enter tempo: "))

def getMeasures():
    return int(input("Enter number of measures: "))

def getFile():
    return input("Enter write file (.mid): ")

def getSheetMusicInput():
    return input("Would you like to generate sheet music? (y/n) ")

def getRepeat():
    return input("Would you like to generate music with the same settings? (y/n) ")

def MusicTest():
    print("\n\n")
    print("AI MUSIC GENERATOR")
    print("-----------------------------------------")
    inst = getInst()
    print("")
    artist = getArtist(inst)
    print("")
    tempo = getTempo()
    print("")
    numMeasures = getMeasures()
    print("")
    #inputFile = getFile()
    #print("")
    inputFile = inst + artist + "_predicted.mid"
    if getSheetMusicInput() == 'y':
        showSheetMusic = True
    print("\n")
    print("-----------------------------------------")
    print("Generating music...\n")
    generateMusic(inst, artist, tempo, numMeasures, inputFile, showSheetMusic)
    generateSame = True
    while generateSame:
        if getRepeat() == 'y':
            print("-----------------------------------------")
            generateMusic(inst, artist, tempo, numMeasures, inputFile, showSheetMusic)
        else:
            generateSame = False

MusicTest()