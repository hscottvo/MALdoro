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


########## Labels
lbl=Label(window, text="Genres", fg='black', font=("Times New Roman", 12))
lbl.place(x=60, y=50)
########## Bunch of Checkboxes      
v1 = IntVar()
v2 = IntVar()
C1 = Checkbutton(window, text = "Ecchi", variable = v1)
C2 = Checkbutton(window, text = "Harem", variable = v2)
C1.place(x=100, y=100)
C2.place(x=180, y=100)

########## Dropdown lists
Label(window, text = "To Do level : ", 
        font = ("Times New Roman", 10)).grid(column = 0, 
        row = 15, padx = 10, pady = 25) 
n = StringVar()
ToDoLvl = Combobox(window, width = 27, textvariable = n, state= "readonly")
  
# Adding combobox drop down list
ToDoLvl['values'] = ('1', '2','3','4','5',)
  
ToDoLvl.grid(column = 1, row = 15)
ToDoLvl.current(1) 

separator = Separator(window, orient='horizontal')
separator.place(relx=0, rely=0.47, relwidth=1, relheight=1)

window.mainloop()


