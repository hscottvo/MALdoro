from anime_comfy_levels import *
from justwatch_query import get_links
from classes import *
from mal import *
from converter import *
from video import *
import csv
import concurrent.futures
import threading
import multiprocessing
import time
from UI import Window
from tkinter import *
from tkinter.ttk import Combobox, Separator
from tkinter import messagebox

genres_list = Genres()
anime_id_new = []
anime_id_completed = []

from tkinter import *
from tkinter.ttk import Combobox, Separator
from tkinter import messagebox
import time
import pandas as pd
from classes import *
from video import *
from justwatch_query import * 
from anime_comfy_levels import genre_finder, anime_levels
#Creating tkinter window

df = pd.read_csv("saved.csv")
# df = df.sort_values(by='Ratio')
final_list = []



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
        self.master.geometry('1200x600')
        self.master.title('MALdoro')
        
        # self.create_upperframe()
        self.create_lowerframe()
        # self.create_upperentries()
        self.create_lowerentries()
        #minute, second = self.create_lowerentries()
        #self.update_clock()
        #self.submit(minute, second)
        # self.upperframe.pack(side="right", fill="both", expand=False, padx=4)
        self.lowerframe.pack(side="left", fill="both", expand=True, padx=4, pady=4)
        
        
        #self.countdown()
        ###############################################################################try to add a pause button
    # def create_upperframe(self):
    #     self.upperframe = Frame(self.master, width=980, height=490)
    #     self.upperframe.config(background="#ffffff")
    #     # Vseparator = Separator(self.upperframe, orient='vertical')
    #     # Vseparator.grid(column = 1, row = 2, columnspan = 2 , sticky = E)

    def create_lowerframe(self):
        self.lowerframe = Frame(self.master, width=830, height=200)
        self.lowerframe.config(background="#a3a4ad")

    # def create_upperentries(self):
    #     self.create_upperframe()
    #     GenreList=["Comedy","Horror","Action","Adventure","Mystery","Romance","Fantasy","Psychological","School","Shounen","Magic","Slice of Life",]
    #     length = len(GenreList)
    #     half = length // 2
    #     c = 6
    #     for i in range(0, half):
    #         r = i +10
            
    #         Checkbutton(self.upperframe, text=GenreList[i]).grid(row=r, column=c+5, pady=4, padx=0, sticky = W)
    #         self.upperframe.grid_columnconfigure(c+1, weight=1)
    #     for i in range(half, length):
    #         r2 = i - half + 10 
            
    #         Checkbutton(self.upperframe, text=GenreList[i]).grid(row=r2, column=c+6, pady=4, padx=0, sticky = W)
    #         self.upperframe.grid_columnconfigure(c+1, weight=1)

    #     r = 2
    #     ################## ToDo Drop Down
    #     Label(self.upperframe, text="Intensity level : ",font = ("Times New Roman", 10)).grid(row=r, column=c+5, pady=4, padx=0, sticky = S)
    #     self.upperframe.grid_columnconfigure(c+1, weight=1)
    #     n = StringVar()
    #     IntensityLvl = Combobox(self.upperframe, width = 27, textvariable = n, state= "readonly")
    #     IntensityLvl['values'] = ('1', '2','3','4','5','6','7','8','9','10')
    #     IntensityLvl.grid(column = c+6, row = r)
    #     intensitylevel = IntensityLvl.get()
    #     self.upperframe.grid_columnconfigure(c+1, weight=1)        
    #     ################## submit button        
    #     Submit = Button(self.upperframe, text="Submit", command = print_intensity)
    #     Submit.grid(column = c+6, row = r+20, sticky = E)
    
    def create_lowerentries(self):
        self.create_lowerframe()
        # AnimeList=df.loc[0:10]
        
        length = len(final_list)
        c = 0
    # Anime Titles Column    
        Label(self.lowerframe, text="Anime Titles").grid(column=c+1, pady=4, padx=0, sticky = W)
        # print(AnimeList[0]['Title'])
        for i in range(0, length):
            r = i +10
            Button(self.lowerframe, text=final_list[i].title, command=lambda title=final_list[i].title: anime_click(title)).grid(row=r, column=c+1, pady=4, padx=0, sticky = W)
            self.lowerframe.grid_columnconfigure(c+2, weight=1)
    # Anime Intensity
        Label(self.lowerframe, text="Genres").grid(row = 0, column=c+2, pady=4, padx=0, sticky = W)
        for i in range(0, length):
            r2= i +10
            
            Label(self.lowerframe, text=final_list[i].genres).grid(row=r2, column=c+2, pady=4, padx=0, sticky = W)
            self.lowerframe.grid_columnconfigure(c+1, weight=1)
        Label(self.lowerframe, text="Anime Intensity Level").grid(row = 0, column=c+3, pady=4, padx=2, sticky = W)
        for i in range(0, length):
            r= i +10
            
            Label(self.lowerframe, text=final_list[i].ratio()).grid(row=r, column=c+3, pady=4, padx=0, sticky = W)
            self.lowerframe.grid_columnconfigure(c+1, weight=1)
    # def submit(self, minute, second):
    #         r=2
    #         c=2
    #         self.create_lowerframe()
    #         #temp = int(minute.get()) * 60 + int(second.get())
    #         try:
    #             # the input provided by the user is
    #             # stored in here :temp
    #             temp =  int(minute.get())*60 + int(second.get())
    #         except:
    #             print("Please input the right value")
    #         while temp >-1:
                
    #             # divmod(firstvalue = temp//60, secondvalue = temp%60)
    #             mins,secs = divmod(temp,60)
        
    #             # Converting the input entered in mins or secs to
    #             # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
    #             # 50min: 0sec)
               
    #             # using format () method to store the value up to
    #             # two decimal places
                
    #             minute.set("{0:2d}".format(mins))
    #             second.set("{0:2d}".format(secs))
        
    #             # updating the GUI window after decrementing the
    #             # temp value every time
    #             self.update()
    #             time.sleep(1)
        
    #             # when temp value = 0; then a messagebox pop's up
    #             # with a message:"Time's up"
    #             if (temp == 0):
    #                 messagebox.showinfo("Time Countdown", "Time's up ")
                
    #             # after every one sec the value of temp will be decremented
    #             # by one
    #             temp -= 1       

    
def ui_main():
    window = Tk()
    app = Window(window)
    window.mainloop()
    
    


# self.title = title
# self.stress_counter = stress_counter
# self.calm_counter = calm_counter
# self.neutral_counter = neutral_counter
# self.genres = genres

def save_list(anime_list):
    titles = []
    stress = []
    calm = []
    neutral = []
    genres = []
    ratio = []
    for anime in anime_list: 
        titles.append(anime.title)
        stress.append(anime.stress_counter)
        calm.append(anime.calm_counter)
        neutral.append(anime.neutral_counter)
        genres.append(anime.genres)
        ratio.append(anime.ratio())

    title_series = pd.Series(titles)
    stress_series = pd.Series(stress)
    calm_series = pd.Series(calm)
    neutral_series = pd.Series(neutral)
    genres_series = pd.Series(genres)
    ratio_series = pd.Series(ratio)

    frame = {"Title":  title_series, "Genres": genres_series, "Stress Level": stress_series, "Calm Level": calm_series, "Neutral Level": neutral_series, "Ratio": ratio_series}

    result = pd.DataFrame(frame)

    result.to_csv("saved.csv")
    return result



def main():
    anime_list = []
    xmlinput = input("enter xml file name: ") # button input
    parse_xml(xmlinput)

    FILENAME = "output.csv"
    with open(FILENAME, newline = "") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[4] == "Plan to Watch":
                anime_id_new.append(row[5])
            elif row[4] == "Completed":
                anime_id_completed.append(row[5])

    choice = input("new or completed? (n/c): ") # button input
    curr_id = []
    if choice.lower() == "n":
        curr_id = anime_id_new
    else:
        curr_id = anime_id_completed
    print("If Create List does not work, check MAL Site")
    choice = input("load anime or create new list? (l/c): ")
    if choice.lower() == "c":
        # mid = int(len(curr_id) / 2)
        # left = int(mid/2)
        # right = int(mid + left)

        # process1 = curr_id[:left]
        # process2 = curr_id[left:mid]
        # process3 = curr_id[mid:right]
        # process4 = curr_id[right:]
        
        # Alpha Future Processing
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = executor.map(anime_levels,curr_id)
            for result in results:
                anime_list.append(result)
        print("\nProcess complete")
        # with concurrent.futures.ProcessPoolExecutor() as executor:
        #     results = executor.map(anime_levels,process2)
        #     for result in results:
        #         anime_list.append(result)
        # print("\nProcess 2 complete")
        # with concurrent.futures.ProcessPoolExecutor() as executor:
        #     results = executor.map(anime_levels,process3)
        #     for result in results:
        #         anime_list.append(result)
        # print("\nProcess 3 complete")
        # with concurrent.futures.ProcessPoolExecutor() as executor:
        #     results = executor.map(anime_levels,process4)
        #     for result in results:
        #         anime_list.append(result)
        # print("\nProcess 4 complete")
    else:
        anime_list = load_file("saved.csv")

    # print(anime_list[0].title, get_links(anime_list[0].title))
    
    main_genre_list = ["Dementia","Horror", "Mystery", "Psychological", "Thriller", "Historical", "Military", "Martial Arts", "Samurai", "Drama", "Police", "Seinen", "Shounen", "Space", "Sci-Fi", "Mecha", "Sports", "Supernatural","Action","Adventure","Comedy", "Ecchi", "Fantasy", "Game", "Harem", "Kids", "Parody", "Slice of Life", "Romance", "Music", "School", "Shoujo", "Shouji Ai", "Shounen Ai", "Yaoi", "Yuri","Magic", "Super Power", "Cars", "Demons", "Josei", "Vampire"]
    for i in main_genre_list:
        print(i,end=" - ")

    specified_genres = []

    while True:
        user_genre = input("\nEnter a Genre (type done when done): ")
        if user_genre in main_genre_list:
            specified_genres.append(user_genre)
        elif user_genre.lower() == "done":
            break
        else:
            print("Not a genre")

    while True:
        user_level = input("How intense is your work (1-10)?")
        if user_level.isdigit():
            user_level = int(user_level)
            if (user_level > 0 and user_level < 11):
                break
        print("Incorrect input") 
    
    genre_specific = []
    genre_specific = genre_finder(anime_list,specified_genres)

    intensity_level = 10 - user_level
    lower_bound = intensity_level - 1
    upper_bound = intensity_level + 1
    global final_list
    final_list = []
    for i in genre_specific:
        show_level = i.ratio()
        if (show_level >= lower_bound and show_level <= upper_bound):
            final_list.append(i)

    if len(final_list) == 0:
        print("No Show Selected - Try other parameters")
    else:
        for show in final_list:
            print(show.title,show.ratio())
    # print(genre_specific[0].title, get_links(genre_specific[0].title))
    # save_list(anime_list)
    ui_main()

if __name__ == "__main__":
    main()
    