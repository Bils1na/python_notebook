from tkinter import *
from tkinter import ttk
import notebook_handler
from notebook_handler import notebook, data as notebook_data


def render_table():
    clear_table()
    fill_table()


def clear_table():
    table.delete(*table.get_children())


def fill_table():
    id = 0
    for note in notebook.notebook:
        id += 1
        table.insert("", END, values=(id, note.get_title(), note.get_date(), note.get_text()))


def dismiss(window):
    window.grab_release()
    window.destroy()


def create_note(title, text, window):
    notebook.add(title.get(),
                 text.get("1.0", END))
    render_table()
    dismiss(window)


def add_note():
    ui_adding = Toplevel()
    ui_adding.title("Добавление заметки")
    ui_adding.geometry("554x512")
    ui_adding.protocol("WM_DELETE_WINDOW", lambda: dismiss(ui_adding))

    title_group = LabelFrame(ui_adding, borderwidth=0)
    title_group.grid(column=0, row=0, sticky="we", padx=[2,0], pady=[2,15])
    adding_title = Label(title_group, text="Введите название заметки: ")
    adding_title.grid(column=0, row=0)
    title_input = Entry(title_group, width=64)
    title_input.grid(column=2, row=0, padx=[0,1])

    text_group = LabelFrame(ui_adding, borderwidth=0)
    text_group.grid(column=0, row=1, sticky="we", padx=[2,0])
    adding_text = Label(text_group, text="Введите текст заметки: ")
    adding_text.grid(column=0, row=1, sticky="we")
    text_input = Text(text_group, width=67, height=20)
    text_input.grid(column=0, row=2, sticky="we", padx=[1,0])

    btns = LabelFrame(ui_adding, borderwidth=0)
    btns.grid(column=0, row=3, pady=[30, 0])
    create_btn = Button(btns, text="Create", command=lambda: create_note(title_input, text_input, ui_adding))
    cancel_btn = Button(btns, text="Cancel", command=lambda: dismiss(ui_adding))
    create_btn.grid(column=0, row=3, ipadx=10, ipady=10, padx=[0,15])
    cancel_btn.grid(column=1, row=3, ipadx=10, ipady=10)

    ui_adding.grab_set()


def open_note(event):
    try:
        ui_note = Toplevel()
        ui_note.geometry("554x512")
        ui_note.protocol("WM_DELETE_WINDOW", lambda: dismiss(ui_note))
        ui_note.title(f"Заметка {get_note_data(event)[1]}")
        note_text = Label(ui_note, text=get_note_data(event)[3])
        note_text.grid(column=0, row=0)
        ui_note.grab_set()
    except:
        print("Выброс исключения")


def get_note_data(event):
    for selection in table.selection():
        item = table.item(selection)
        return item["values"]


def get_notes_data():
    data = []
    for note in table.get_children():
        data.append(table.item(note)["values"])
    return data


def save_notes():
    notes_data = get_notes_data()
    for element in notes_data:
        notebook_data[element[0]] = (element[1], element[2], element[3])
    notebook_handler.save_data_base()


def load_notes():
    notebook_handler.download_data_base()
    render_table()


ui = Tk()
ui.title("Notebook")
ui.geometry("554x512")
ui.resizable(False, False)

btns = LabelFrame(ui, borderwidth=0)
btns.grid(column=2, row=0)
btn1 = Button(btns, text="Add note", command=add_note)
btn2 = Button(btns, text="Search by date")
btn3 = Button(btns, text="All notes")
btn4 = Button(btns, text="Save", command=save_notes)
btn5 = Button(btns, text="Load", command=load_notes)
btn1.grid(column=0, row=0, ipadx=30, ipady=10, sticky="we")
btn2.grid(column=0, row=1, ipadx=30, ipady=10, sticky="we")
btn3.grid(column=0, row=2, ipadx=30, ipady=10, sticky="we")
btn4.grid(column=0, row=3, ipadx=30, ipady=10, sticky="we")
btn5.grid(column=0, row=4, ipadx=30, ipady=10, sticky="we")

columns = ("id", "name", "date")
table = ttk.Treeview(columns=columns, show="headings", height=24)
table.grid(column=0, row=0, sticky="ns", ipadx=15, padx= [5,0])
table.heading("id", text="№")
table.heading("name", text="Note")
table.heading("date", text="Date")
table.column(0, width=35)
table.column(2, width=100)
table.bind("<Double-1>", open_note)

scroll_bar = Scrollbar(ui, orient="vertical", command=table.yview)
scroll_bar.grid(column=1, row=0, ipady=85, sticky="ns")

table["yscrollcommand"] = scroll_bar.set

load_notes()
