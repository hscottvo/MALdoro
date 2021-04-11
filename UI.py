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
        self.master.geometry('750x350')
        self.master.title('MALdoro')
        
        self.create_upperframe()
        self.create_lowerframe()
        self.create_buttonentries()
        self.update_clock()
        self.upperframe.pack(side="top", fill="both", expand=True, padx=4)
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
    def create_buttonentries(self):
        self.create_upperframe()
        GenreList=["Ecchi","Harem","Action","Adventure","Mystery","Romance","Fantasy","Psychological","School","Shounen","Magic","Slice of Life",]
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
    def update_clock(self):
        c=1
        r=2
        self.create_lowerframe()
        now = time.strftime("%H:%M:%S")

        Label(self.lowerframe,text = now).grid(row=r, column=c+5, pady=4, padx=0)
        self.lowerframe.grid_rowconfigure(2)
        self.master.after(10, self.update_clock)
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


window = Tk()
app = Window(window)

window.mainloop()

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






