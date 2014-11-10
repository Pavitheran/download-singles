__author__ = 'Pavitheran'
__author__ = 'Udara'

from tkinter import *
from getSongLastFm import *
import os




class Application(Frame):
    ## A GUI Application with a button.

    def __init__(self, master):
        ##initializes the Frame
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()



    def create_widgets(self):
        ##Create a label
        self.instruction = Label(self, text = "Artist Name/Song")
        self.instruction.grid(row=0, column=0, columnspan=3, sticky=W)

        ##Create an area where user can type
        self.name = Entry(self)
        self.name.grid(row=0, column=1, sticky=W)

        ##Create a button linked to get_mp3
        self.submit = Button(self, text="One Song", command= lambda: self.download_video(0))
        self.submit.grid(row=2, column=0, sticky=W)

        ##Creates button linked to get_song
        self.topten = Button(self, text="Top Ten", command=lambda: self.download_video(1))
        self.topten.grid(row=2, column=1, sticky=W)

        ##Creates button linked to get_music_vid
        self.getvid = Button(self, text="Music Video", command= lambda: self.download_video(2))
        self.getvid.grid(row=2, column=1, sticky=E)

        ##Create an area where text can be output to
        self.text = Text(self, width=49, height=15, wrap=WORD)
        self.text.grid(row=3, column=0, columnspan=2, sticky=W)

        ##Creates music folder on C Drive for downloaded mp3s
        if not os.path.exists("C:\Music"):
            os.makedirs("C:\Music")

        os.chdir("C:\Music")

        self.text.insert(0.0, "Enter an artist name only for their top ten songs.\n"
                              "Enter artist name + song name for just one song.\n"
                              "\nPlease be patient when downloading top ten songs, it may take up to a minute.\n"
                              "\nMade by Udara and Pavi")



    def download_video(self,flag):
        artist_name = self.name.get()
        self.text.delete(0.0, END)

        if (flag == 0):
            ##Downloads specified song
            get_mp3(artist_name)

        elif (flag == 1):
            ##Downloads top 10 songs
            get_song(artist_name)

        else:
            ##Downloads music video
            get_music_vid(artist_name)

        ##Shows the user a message on successful completion

        self.text.insert(0.0, "Song(s) successfully downloaded and placed in your C:\music directory.")

        self.name.delete(0, END)



##Create and format GUI Window
root = Tk()
root.title("Download Songs")
root.geometry("400x300")
root.resizable(width=FALSE, height=FALSE)

app = Application(root)

##Function that keeps the window open
root.mainloop()

