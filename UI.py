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

########################################
# import tkinter as tk
# from tkinter import ttk

# # Creating tkinter window
# window = tk.Tk()
# window.geometry('350x250')
# # Label
# ttk.Label(window, text = "To Do level : ", 
#         font = ("Times New Roman", 10)).grid(column = 0, 
#         row = 15, padx = 10, pady = 25)
  
# n = tk.StringVar()
# ToDoLvl = ttk.Combobox(window, width = 27, 
#                             textvariable = n, state= "readonly")
  
# # Adding combobox drop down list
# ToDoLvl['values'] = ('1', 
#                      '2',
#                      '3',
#                      '4',
#                      '5',)
  
# ToDoLvl.grid(column = 1, row = 15)


# # Shows february as a default value
# ToDoLvl.current(1) 
# window.mainloop()





from tkinter import *
from tkinter.ttk import Combobox, Separator
#Creating tkinter window
window = Tk()
window.geometry('650x750')
window.title('MALdoro')

####################  Buttons
Submit = Button(window, text="Submit")
Submit.place(x=550, y= 450)

####################  Labels
lbl=Label(window, text="Genres", fg='black', font=("Times New Roman", 12))
lbl.place(x=450, y=100)


####################  Bunch of Checkboxes 
#########Genre Checkboxes
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()
v5 = IntVar()
v6 = IntVar()
v7 = IntVar()
v8 = IntVar()
v9 = IntVar()
v10 = IntVar()
v11 = IntVar()
v12 = IntVar()
C1 = Checkbutton(window, text = "Ecchi", variable = v1)
C2 = Checkbutton(window, text = "Harem", variable = v2)
C3 = Checkbutton(window, text = "Action", variable = v3)
C4 = Checkbutton(window, text = "Adventure", variable = v4)
C5 = Checkbutton(window, text = "Mystery", variable = v5)
C6 = Checkbutton(window, text = "Romance", variable = v6)
C7 = Checkbutton(window, text = "Fantasy", variable = v7)
C8 = Checkbutton(window, text = "Psychological", variable = v8)
C9 = Checkbutton(window, text = "School", variable = v9)
C10 = Checkbutton(window, text = "Shounen", variable = v10)
C11 = Checkbutton(window, text = "Magic", variable = v11)
C12 = Checkbutton(window, text = "Slice of Life", variable = v12)
C1.place(x=450, y=150)
C2.place(x=520, y=150)
C3.place(x=450, y=200)
C4.place(x=520, y=200)
C5.place(x=450, y=250)
C6.place(x=520, y=250)
C7.place(x=450, y=300)
C8.place(x=520, y=300)
C9.place(x=450, y=350)
C10.place(x=520, y=350)
C11.place(x=450, y=400)
C12.place(x=520, y=400)

####################  Dropdown lists
Label(window, text = "To Do level : ", font = ("Times New Roman", 10)).place(x=450, y=25)
n = StringVar()
ToDoLvl = Combobox(window, width = 27, textvariable = n, state= "readonly")
ToDoLvl['values'] = ('1', '2','3','4','5',)
  
ToDoLvl.place(x=450, y=50)
ToDoLvl.current(1) 

####################  Separators
Vseparator = Separator(window, orient='vertical')
Vseparator.place(relx=0.65, rely=0, relwidth=0, relheight=1)
Vseparator2 = Separator(window, orient='vertical')
Vseparator2.place(relx=0.45, rely=0, relwidth=0, relheight=1)
Vseparator3 = Separator(window, orient='vertical')
Vseparator3.place(relx=0.25, rely=0, relwidth=0, relheight=1)

Hseparator = Separator(window, orient='horizontal')
Hseparator.place(relx=0, rely=0.7, relwidth=1, relheight=1)



window.mainloop()


