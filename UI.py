from tkinter import *
from tkinter.ttk import Combobox, Separator
from tkinter import messagebox
import time
from classes import *
from video import *
from justwatch_query import * 
from anime_comfy_levels import genre_finder, anime_levels
#Creating tkinter window

def anime_click(title):
    open_link(get_links(title))

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        # create master window
        self.master = master
        
        # create root window on initialization
        self.create_rootwindow()

        
    def create_rootwindow(self):
        self.master.geometry('650x270')
        self.master.title('MALdoro')
        
        self.create_upperframe()
        self.create_lowerframe()
        self.create_upperentries()
        self.create_lowerentries()
        #minute, second = self.create_lowerentries()
        #self.update_clock()
        #self.submit(minute, second)
        self.upperframe.pack(side="right", fill="both", expand=False, padx=4)
        self.lowerframe.pack(side="left", fill="both", expand=True, padx=4, pady=4)
        
        
        #self.countdown()
        ###############################################################################try to add a pause button
    def create_upperframe(self):
        self.upperframe = Frame(self.master, width=980, height=490)
        self.upperframe.config(background="#ffffff")
        # Vseparator = Separator(self.upperframe, orient='vertical')
        # Vseparator.grid(column = 1, row = 2, columnspan = 2 , sticky = E)

    def create_lowerframe(self):
        self.lowerframe = Frame(self.master, width=830, height=200)
        self.lowerframe.config(background="#a3a4ad")
    def create_upperentries(self):
        self.create_upperframe()
        GenreList=["H","Harem","Action","Adventure","Mystery","Romance","Fantasy","Psychological","School","Shounen","Magic","Slice of Life",]
        length = len(GenreList)
        half = length // 2
        c = 6
        for i in range(0, half):
            r = i +10
            
            Checkbutton(self.upperframe, text=GenreList[i]).grid(row=r, column=c+5, pady=4, padx=0, sticky = W)
            self.upperframe.grid_columnconfigure(c+1, weight=1)
        for i in range(half, length):
            r2 = i - half + 10 
            
            Checkbutton(self.upperframe, text=GenreList[i]).grid(row=r2, column=c+6, pady=4, padx=0, sticky = W)
            self.upperframe.grid_columnconfigure(c+1, weight=1)

        r = 2
        ################## ToDo Drop Down
        Label(self.upperframe, text="Intensity level : ",font = ("Times New Roman", 10)).grid(row=r, column=c+5, pady=4, padx=0, sticky = S)
        self.upperframe.grid_columnconfigure(c+1, weight=1)
        n = StringVar()
        IntensityLvl = Combobox(self.upperframe, width = 27, textvariable = n, state= "readonly")
        IntensityLvl['values'] = ('1', '2','3','4','5','6','7','8','9','10')
        IntensityLvl.grid(column = c+6, row = r)
        IntensityLvl.current(1)
        self.upperframe.grid_columnconfigure(c+1, weight=1)        
        ################## submit button        
        Submit = Button(self.upperframe, text="Submit")
        Submit.grid(column = c+6, row = r+20, sticky = E)
   
    def create_lowerentries(self):
        self.create_lowerframe()
        AnimeList=["Demon Slayer","Nisekoi","Jujutsu Kaisen","Adventure","Mystery","Romance","Fantasy","Psychological","School","Shounen","Magic","Slice of Life",]
        length = len(AnimeList)
        half = length // 2
        c = 0
    # Anime Titles Column    
        Label(self.lowerframe, text="Anime Titles").grid(column=c+1, pady=4, padx=0, sticky = W)
        
        for i in range(0, half):
            r = i +10
            
            Button(self.lowerframe, text=AnimeList[i], command=lambda title=AnimeList[i]: anime_click(title)).grid(row=r, column=c+1, pady=4, padx=0, sticky = W)
            self.lowerframe.grid_columnconfigure(c+2, weight=1)
    # Anime Intensity
        Label(self.lowerframe, text="Anime Intensity Level").grid(row = 0, column=c+2, pady=4, padx=0, sticky = W)
        for i in range(0, half):
            r2= i +10
            
            Label(self.lowerframe, text=AnimeList[i]).grid(row=r2, column=c+2, pady=4, padx=0, sticky = W)
            self.lowerframe.grid_columnconfigure(c+1, weight=1)
        Label(self.lowerframe, text="Genres").grid(row = 0, column=c+3, pady=4, padx=2, sticky = W)
        for i in range(0, half):
            r= i +10
            
            Label(self.lowerframe, text=AnimeList[i]).grid(row=r, column=c+3, pady=4, padx=0, sticky = W)
            self.lowerframe.grid_columnconfigure(c+1, weight=1)
    def submit(self, minute, second):
            r=2
            c=2
            self.create_lowerframe()
            #temp = int(minute.get()) * 60 + int(second.get())
            try:
                # the input provided by the user is
                # stored in here :temp
                temp =  int(minute.get())*60 + int(second.get())
            except:
                print("Please input the right value")
            while temp >-1:
                
                # divmod(firstvalue = temp//60, secondvalue = temp%60)
                mins,secs = divmod(temp,60)
        
                # Converting the input entered in mins or secs to
                # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
                # 50min: 0sec)
               
                # using format () method to store the value up to
                # two decimal places
                
                minute.set("{0:2d}".format(mins))
                second.set("{0:2d}".format(secs))
        
                # updating the GUI window after decrementing the
                # temp value every time
                self.update()
                time.sleep(1)
        
                # when temp value = 0; then a messagebox pop's up
                # with a message:"Time's up"
                if (temp == 0):
                    messagebox.showinfo("Time Countdown", "Time's up ")
                
                # after every one sec the value of temp will be decremented
                # by one
                temp -= 1       

    
def main():

    window = Tk()
    app = Window(window)
    window.mainloop()
main()