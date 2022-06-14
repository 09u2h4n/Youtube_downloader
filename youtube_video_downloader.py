from subprocess import getoutput
from sys import exit
from os import getcwd, rename

"""
TODO
*Playlist system,
*Channel and Searching system will be added
*System will be optimized
*Useless things will be deleted
"""

class Downloader(object):
    def get_module(self):
        """If you have moduler error or something about modules use this method."""
        pip_list = getoutput("pip list")
        if "pytube" not in pip_list.split():
            getoutput("pip install pytube==12.1.0")
        else:
            pass
    
    get_module(self="__self__")

    def __doc__(self):
        print("""
Usage :
Download video for;
obj = Downloader("https://youtu.be/m4gnMWua4xo").download_video()
or 
Download audio for;
obj = Downloader("https://youtu.be/m4gnMWua4xo").download_audio()
        """)

    def __init__(self, url):
        from pytube import YouTube, Playlist
        pwd = getcwd()
        self.url = url
        self.pwd = pwd

        try:
            yt = YouTube(self.url)
            self.yt = yt
        except:
            pass

        pl = Playlist(self.url)
        self.pl = pl

    def download_video(self):
        try:
            print("Downloading..")
            self.yt.streams.get_highest_resolution().download()
            print(f"Downloaded in {self.pwd}")
        except:
            print("Command line download method started..")
            getoutput(f"pytube {self.url}")
            print(f"Downloaded in {self.pwd}")
        
    def download_audio(self):
        try:
            print("Downloading..")
            self.yt.streams.get_audio_only().download()
            try:
                rename(f"{self.yt.title}.mp4", f"{self.yt.title}.mp3")
            except FileExistsError:
                print(f"Cannot create an existing file ('mp3' file could not be downloaded). The file named '{self.yt.title}.mp4' has been downloaded")
                return
            print(f"Downloaded in {self.pwd}")
        except:
            print("Command line download method started..")
            getoutput(f"pytube {self.url} -a")
            try:
                rename(f"{self.yt.title}.mp4", f"{self.yt.title}.mp3")
            except FileExistsError:
                print(f"Cannot create an existing file ('mp3' file could not be downloaded). The file named '{self.yt.title}'.mp4 has been downloaded")
                return
            print(f"Downloaded in {self.pwd}")

    def download_playlist(self):
        print(f"Downloading.. {self.pl.title}")
        video_num = 0
        for video in self.pl.videos:
            video_num += 1
            video.streams.get_highest_resolution().download(output_path=f"{self.pl.title}", filename=f"{video_num}){video.title}.mp4")
            


#Downloader("https://youtube.com/playlist?list=PLKKYLPm3FCARcMH5790kD0KqZF3QCrgZN").download_playlist()
