from tkinter import *

ui = Tk()
ui.title("Notebook")
ui.geometry("512x512")

btn1 = Button(ui, text="Add note")
btn2 = Button(ui, text="Find date")
btn3 = Button(ui, text="All notes")
btn4 = Button(ui, text="Save")
btn5 = Button(ui, text="Load")
btn1.grid(column=0, row=0)
btn2.grid(column=1, row=0)
btn3.grid(column=2, row=0)
btn4.grid(column=3, row=0)
btn5.grid(column=4, row=0)

notes = ["Note #1", "Note #2", "Note #1", "Note #2", "Note #1", "Note #2", "Note #1", "Note #2",
         "Note #1", "Note #2", "Note #1", "Note #2", "Note #1", "Note #2"]
notes_var = StringVar(value=notes)
listbox = Listbox(listvariable=notes_var)
listbox.grid(column=0, row=1)

scroll_bar = Scrollbar(orient="vertical", command=listbox.yview)
scroll_bar.grid(column=0, row=1, columnspan=5)

