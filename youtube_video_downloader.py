from subprocess import getoutput
from os import getcwd, rename

"""
TODO
*Channel and Searching system will be added
*System will be optimized
*Useless things will be deleted
"""

class Downloader(object):
    def __get_module(self):
        """If you have moduler error or something about modules use this method."""
        pip_list = getoutput("pip list")
        if "pytube" not in pip_list.split():
            print("Installing a module")
            getoutput("pip install pytube==12.1.0")
            print("Installed\n")
        elif "pytube" in pip_list.split():
            pass
        else:
            print("Please install manually!")
    
    __get_module(self="self")

    def __doc__(self):
        print("""
Usage :
Downloading video with highest resolution for;
>>Downloader("https://youtu.be/m4gnMWua4xo").download_video()
Downloading video with special resolution for:
>>Downloader("https://youtu.be/m4gnMWua4xo").download_video(res="360p")
or 
Download audio for;
>>Downloader("https://youtu.be/m4gnMWua4xo").download_audio()
or 
Download Playlist videos for;
>>Downloader("https://youtube.com/playlist?list=PLUNPjaQ-i_voID9V4u9L23XWiwpUPY0sG").download_playlist()
Download Playlist just video's audio for;
>>Downloader("https://youtube.com/playlist?list=PLUNPjaQ-i_voID9V4u9L23XWiwpUPY0sG").download_playlist(audio = True)
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
            pl = Playlist(self.url)
            self.pl = pl

    def download_video(self, res="0"):
        if res == "0":
            print("Downloading..")
            self.yt.streams.get_highest_resolution().download()
            print(f"Downloaded in {self.pwd}")
        elif res != "0":
            print("Downloading..")
            try:
                self.yt.streams.get_by_resolution(res).download()
            except AttributeError:
                print(f"Could not find: {res}")
            print(f"Downloaded in {self.pwd}")
        
    def download_audio(self):
        print("Downloading..")
        self.yt.streams.get_audio_only().download(filename=f"{self.yt.title}.mp3")
        print(f"Downloaded in {self.pwd}")

    def download_playlist(self, audio = False):
        video_num = 0
        if audio == False:
            print(f"Downloading.. {self.pl.title}")
            for video in self.pl.videos:
                video_num += 1
                video.streams.get_highest_resolution().download(output_path=f"{self.pl.title}", filename=f"{video_num}){video.title.replace('/', '')}.mp4")
                print(f"Downloaded '{video.title}.mp4'")
            print(f"Downloaded all videos in {self.pwd} ==> {self.pl.title}")
        elif audio == True:
            print(f"Downloading.. {self.pl.title}")
            for video in self.pl.videos:
                video_num += 1
                video.streams.get_audio_only().download(output_path=f"{self.pl.title} Audios", filename=f"{video_num}){video.title.replace('/', '')}.mp3")
                print(f"Downloaded '{video.title}.mp3'")
            print(f"Downloaded all videos in {self.pwd} ==> {self.pl.title}")
