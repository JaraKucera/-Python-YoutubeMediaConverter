#**********     Imports     **********
import os
import moviepy.editor
import eyed3
import subprocess
import spotipy
#**********     Classes     **********
#**********     Global      **********
proxy = "#"
global listFiles
#**********     Functions   **********
def download(): #Downloads a given video or playlist provided by link
    subprocess.call(f'youtube-dl --proxy {proxy} {link}')

def convert(path): #Converts video file to audio files
    global listFiles
    for song in listFiles: #List of videos
        videopath = path+"\\"+song #add path to song name
        print("\n\n\n\n"+videopath+"\n\n\n\n\n") #display path
        video = moviepy.editor.VideoFileClip(videopath) #import video file
        audio = video.audio #Extract audio from video file
        artist = input("\nArtist::\n") #Get artist input
        title = input("\nTitle::\n") #Get title of song
        filename = artist+" - "+title+".mp3" #create string in the form "artist - title.mp3"
        audio.write_audiofile(filename) #save audio file
        meta(filename,artist,title) #add metadata

def meta(filename,artist,title): #Adds metadata to audio file
    audiofile = eyed3.load(filename) #Load audio file
    audiofile.tag.artist = artist #add artist tag
    audiofile.tag.title = title #add title tag
    audiofile.tag.save() #save tag
    print(audiofile.tag.artist + "\n"+audiofile.tag.title)

def getListOfFiles(dir): #Find all .mp4 files in project directory and add to list
    global listFiles
    listFiles = []
    for root, dirs, files in os.walk(dir):
        if files:
            for file in files:
                if os.path.splitext(file)[1] == '.mp4':
                    print(file)
                    listFiles.append(file)

def delFiles(dir): #Deletes all .mp4 in given directory
    global listFiles
    for root, dirs, files in os.walk(dir): #walk through directory
        if files:
            for file in files:
                if os.path.splitext(file)[1] == '.mp4':
                    print("Deleting:: "+file)
                    os.remove(file) #remove file if mp4
    listFiles = [] #set list to empty

#**********     Main        **********
link = "https://www.youtube.com/watch?v=20gftvWKwaE"
download()
path = os.path.dirname(os.path.realpath(__file__))
convert(path)
getListOfFiles(path)
delFiles(path)
