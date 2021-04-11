# from tkinter import *

# def enter():
#     entry = text.get()
#     output.delete(0.0,END)
#     output.insert(END, entry)


# window = Tk()
# window.title("Library")

# canvas = Canvas(window, height=700, width=700)
# canvas.pack()

# frame = Frame(window,bg="black")
# frame.place(relx=0.1,rely=0.1, relheight= 0.8, relwidth=0.8)

# lb1 = Label(frame, text="Enter Word to Search:", bg = "black", fg="white")
# lb1.pack()

# text = Entry(frame,width=50,bg="white")
# text.pack()

# submit_button = Button(frame,text = "Submit",width=6, command= enter)
# submit_button.pack()

# output = Text(frame, width= 70, height= 10, wrap= WORD, background= "white")
# output.pack()

# window.mainloop()


from tkinter import *
from tkinter.ttk import Combobox, Separator
from tkinter import messagebox
import time
#Creating tkinter window


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
        Label(self.upperframe, text="To Do level : ",font = ("Times New Roman", 10)).grid(row=r, column=c+5, pady=4, padx=0, sticky = S)
        self.upperframe.grid_columnconfigure(c+1, weight=1)
        n = StringVar()
        ToDoLvl = Combobox(self.upperframe, width = 27, textvariable = n, state= "readonly")
        ToDoLvl['values'] = ('1', '2','3','4','5','6','7','8','9','10')
        ToDoLvl.grid(column = c+6, row = r)
        ToDoLvl.current(1)
        self.upperframe.grid_columnconfigure(c+1, weight=1)        
        ################## submit button        
        Submit = Button(self.upperframe, text="Submit")
        Submit.grid(column = c+6, row = r+20, sticky = E)
   
    def create_lowerentries(self):
        self.create_lowerframe()
        AnimeList=["H","Harem","Action","Adventure","Mystery","Romance","Fantasy","Psychological","School","Shounen","Magic","Slice of Life",]
        length = len(AnimeList)
        half = length // 2
        c = 0
        Label(self.lowerframe, text="Anime Titles").grid(column=c+1, pady=4, padx=0, sticky = W)
        
        for i in range(0, half):
            r = i +10
            
            Button(self.lowerframe, text=AnimeList[i]).grid(row=r, column=c+1, pady=4, padx=0, sticky = W)
            self.lowerframe.grid_columnconfigure(c+2, weight=1)
        Label(self.lowerframe, text="Anime Stress Level").grid(row = 0, column=c+2, pady=4, padx=0, sticky = W)
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
        
                # Converting the input entered in mins or secs to hours,
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

    #         btn = Button(self.lowerframe, text='Set Time Countdown', bd='5')
    #         btn.grid(column = c+3, row = r+1)

# self.create_lowerframe()
#         c=2
#         r=2
#         # Declaration of variables

#         minute=StringVar()
#         second=StringVar()

#         # setting the default value as 0
#         minute.set("00")
#         second.set("03")
#         # Use of Entry class to take input from the user
#         minuteEntry= Entry(self.lowerframe, width=3, font=("Arial",18,""), textvariable=minute)
#         minuteEntry.grid(column = c, row = r)

#         secondEntry= Entry(self.lowerframe, width=3, font=("Arial",18,""), textvariable=second)
#         secondEntry.grid(column = c+1, row = r)
#         btn = Button(self.lowerframe, text='Set Time Countdown', bd='5')
#         btn.grid(column = c+3, row = r)
#         self.lowerframe.grid_columnconfigure(1, weight=1)
#         return minute, second
####################  Labels
# lbl=Label(window, text="Genres", fg='black', font=("Times New Roman", 12))
# lbl.place(x=450, y=100)



####################  Separators
# Vseparator = Separator(window, orient='vertical')
# Vseparator.place(relx=0.65, rely=0, relwidth=0, relheight=1)
# Vseparator2 = Separator(window, orient='vertical')
# Vseparator2.place(relx=0.45, rely=0, relwidth=0, relheight=1)
# Vseparator3 = Separator(window, orient='vertical')
# Vseparator3.place(relx=0.25, rely=0, relwidth=0, relheight=1)

# Hseparator = Separator(window, orient='horizontal')
# Hseparator.place(relx=0, rely=0.7, relwidth=0, relheight=0)






    # def update_clock(self):
    #     c=1
    #     r=2
    #     self.create_lowerframe()
    #     now = time.strftime("%H:%M:%S")

    #     Label(self.lowerframe,text = now).grid(row=r, column=c+5, pady=4, padx=0)
    #     self.lowerframe.grid_rowconfigure(2)
    #     self.master.after(10, self.update_clock)
    # def countdown(self):
    #     self.create_lowerframe()
    #     t=10 #1500 is 25 minutes
    #     r = 2
    #     c = 6
    #     while t:
    #         mins, secs = divmod(t, 60)
            
    #         timer = '{:02d}:{:02d}'.format(mins, secs)
    #         Label(self.lowerframe, text=timer,font = ("Times New Roman", 10)).grid(row=r, column=c+5, pady=4, padx=0, sticky = S)
            
    #         time.sleep(1)
    #         t -= 1
    #     print('Fire in the hole!!')