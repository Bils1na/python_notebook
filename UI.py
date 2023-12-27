from tkinter import *
from tkinter import ttk, messagebox
from notebook_handler import notebook, data as notebook_data
import notebook_handler


class UI:

    def __init__(self):
        self.ui = Tk()
        self.ui.title("Notebook")
        self.ui.geometry("541x512")
        self.ui.resizable(False, False)

        buttons = LabelFrame(self.ui, borderwidth=0)
        buttons.grid(column=2, row=0)
        btn1 = Button(buttons, text="Create", command=self.add_note_window)
        btn2 = Button(buttons, text="Search by date", command=self.search_by_date_window)
        btn3 = Button(buttons, text="All notes", command=self.display_notebook)
        btn4 = Button(buttons, text="Save", command=self.save_notes)
        btn5 = Button(buttons, text="Load", command=self.load_notes)
        btn6 = Button(buttons, text="Delete", command=self.delete_note)
        btn1.grid(column=0, row=0, ipadx=30, ipady=10, sticky="we", pady=15, padx=(3, 0))
        btn6.grid(column=0, row=1, ipadx=30, ipady=10, sticky="we", pady=15, padx=(3, 0))
        btn2.grid(column=0, row=2, ipadx=30, ipady=10, sticky="we", pady=15, padx=(3, 0))
        btn3.grid(column=0, row=3, ipadx=30, ipady=10, sticky="we", pady=15, padx=(3, 0))
        btn4.grid(column=0, row=4, ipadx=30, ipady=10, sticky="we", pady=15, padx=(3, 0))
        btn5.grid(column=0, row=5, ipadx=30, ipady=10, sticky="we", pady=15, padx=(3, 0))

        self.columns = ("id", "name", "date")
        self.table = ttk.Treeview(columns=self.columns, show="headings", height=24)
        self.table.grid(column=0, row=0, sticky="ns", ipadx=15, padx=(5, 0))
        self.table.heading("id", text="№")
        self.table.heading("name", text="Note")
        self.table.heading("date", text="Date")
        self.table.column(0, width=35)
        self.table.column(2, width=100)
        self.table.bind("<Double-1>", self.open_note_window)

        scroll_bar = Scrollbar(self.ui, orient="vertical", command=self.table.yview)
        scroll_bar.grid(column=1, row=0, ipady=85, sticky="ns")

        self.table["yscrollcommand"] = scroll_bar.set

        self.load_notes()

    def render_table(self, date=""):
        self.clear_table()
        self.fill_table(date)

    def clear_table(self):
        self.table.delete(*self.table.get_children())

    def fill_table(self, date):
        if date:
            for note in notebook.notebook:
                if date == note.get_date()[0].split("-")[0]:
                    self.table.insert("", END, values=(note.get_id(), note.get_title(),
                                                       note.get_date(), note.get_text()))
        else:
            for note in notebook.notebook:
                self.table.insert("", END, values=(note.get_id(), note.get_title(),
                                                   note.get_date(), note.get_text()))

    def dismiss(self, window):
        window.grab_release()
        window.destroy()

    def create_note(self, title, text, window):
        notebook_handler.note_id += 1
        notebook.add(title.get(),
                     text.get("1.0", END), id=notebook_handler.note_id)
        self.render_table()
        self.dismiss(window)

    def edit_note(self, new_title, new_text, window):
        for note in self.table.selection():
            notebook.edit(self.table.item(note)["values"][0],
                          new_title.get(),
                          new_text.get("1.0", END))
            self.render_table()
            self.dismiss(window)

            messagebox.showinfo("Заметка изменена", "Заметка изменена успешно!")

    def delete_note(self):
        for select in self.table.selection():
            notebook.delete(self.table.item(select)["values"][0])
            self.render_table()

    def display_notebook(self):
        self.render_table()

    def display_notebook_by_date(self, date, window):
        self.render_table(date)
        self.dismiss(window)

    def add_note_window(self):
        ui_adding = Toplevel()
        ui_adding.title("Добавление заметки")
        ui_adding.geometry("554x470")
        ui_adding.protocol("WM_DELETE_WINDOW", lambda: self.dismiss(ui_adding))
        ui_adding.resizable(False, False)

        title_group = LabelFrame(ui_adding, borderwidth=0)
        title_group.grid(column=0, row=0, sticky="we", padx=(2, 0), pady=(2, 15))
        adding_title = Label(title_group, text="Введите название заметки: ")
        adding_title.grid(column=0, row=0)
        title_input = Entry(title_group, width=64)
        title_input.grid(column=2, row=0, padx=(0, 1))

        text_group = LabelFrame(ui_adding, borderwidth=0)
        text_group.grid(column=0, row=1, sticky="we", padx=(2, 0))
        adding_text = Label(text_group, text="Введите текст заметки: ")
        adding_text.grid(column=0, row=1, sticky="we")
        text_input = Text(text_group, width=67, height=20)
        text_input.grid(column=0, row=2, sticky="we", padx=(1, 0))

        btns = LabelFrame(ui_adding, borderwidth=0)
        btns.grid(column=0, row=3, pady=(30, 0))
        create_btn = Button(btns, text="Create", command=lambda: self.create_note(title_input, text_input, ui_adding))
        cancel_btn = Button(btns, text="Cancel", command=lambda: self.dismiss(ui_adding))
        create_btn.grid(column=0, row=3, ipadx=10, ipady=10, padx=(0, 15))
        cancel_btn.grid(column=1, row=3, ipadx=10, ipady=10)

        ui_adding.grab_set()

    def open_note_window(self, event):
        try:
            ui_note = Toplevel()
            ui_note.geometry("559x500")
            ui_note.protocol("WM_DELETE_WINDOW", lambda: self.dismiss(ui_note))
            ui_note.title(f"Заметка {self.get_note_data(event)[1]}")
            ui_note.resizable(False, False)
            ui_note["bg"] = "white"
            note_group = LabelFrame(ui_note, borderwidth=0, bg="white")
            note_group.grid(column=0, row=0)
            note_title = Label(note_group, text=self.get_note_data(event)[1], bg="white")
            note_title.grid(column=0, row=0)
            note_text = Label(note_group, text=self.get_note_data(event)[3], bg="white", width=80, wraplength=550)
            note_text.grid(column=0, row=1, pady=30)

            btns = LabelFrame(ui_note, borderwidth=0, bg="white")
            btns.grid(column=0, row=1, pady=(30, 0))
            create_btn = Button(btns, text="Edit", command=lambda: self.edit_note_window(self.get_note_data(event)[3],
                                                                                         self.get_note_data(event)[1],
                                                                                         ui_note))
            cancel_btn = Button(btns, text="Cancel", command=lambda: self.dismiss(ui_note))
            create_btn.grid(column=0, row=0, ipadx=10, ipady=10, padx=(0, 15))
            cancel_btn.grid(column=1, row=0, ipadx=10, ipady=10)

            ui_note.grab_set()
        except:
            print("Выброс исключения")

    def edit_note_window(self, text, title, ui_note):
        self.dismiss(ui_note)

        ui_edit = Toplevel()
        ui_edit.title("Редактирование заметки")
        ui_edit.geometry("554x470")
        ui_edit.protocol("WM_DELETE_WINDOW", lambda: self.dismiss(ui_edit))
        ui_edit.resizable(False, False)

        title_group = LabelFrame(ui_edit, borderwidth=0)
        title_group.grid(column=0, row=0, sticky="we", padx=(2, 0), pady=(2, 15))
        adding_title = Label(title_group, text="Изменить название заметки: ")
        adding_title.grid(column=0, row=0)
        title_input = Entry(title_group, width=64)
        title_input.insert(END, title)
        title_input.grid(column=2, row=0, padx=(0, 1))

        text_group = LabelFrame(ui_edit, borderwidth=0)
        text_group.grid(column=0, row=1, sticky="we", padx=(2, 0))
        adding_text = Label(text_group, text="Редактировать текст заметки: ")
        adding_text.grid(column=0, row=1, sticky="we")
        text_input = Text(text_group, width=67, height=20)
        text_input.insert(END, text)
        text_input.grid(column=0, row=2, sticky="we", padx=(1, 0))

        btns = LabelFrame(ui_edit, borderwidth=0)
        btns.grid(column=0, row=3, pady=(30, 0))
        edit_btn = Button(btns, text="Edit", command=lambda: self.edit_note(title_input, text_input, ui_edit))
        cancel_btn = Button(btns, text="Cancel", command=lambda: self.dismiss(ui_edit))
        edit_btn.grid(column=0, row=3, ipadx=10, ipady=10, padx=(0, 15))
        cancel_btn.grid(column=1, row=3, ipadx=10, ipady=10)

        ui_edit.grab_set()

    def search_by_date_window(self):
        ui_search = Toplevel()
        ui_search.title("Добавление заметки")
        ui_search.geometry("420x180")
        ui_search.resizable(False, False)

        search_group = LabelFrame(ui_search, borderwidth=0)
        search_group.grid(column=0, row=0, pady=35)
        search_text = Label(search_group, text="Введите дату для поиска: ")
        search_text.grid(column=0, row=0)
        search_input = Entry(search_group, width=44)
        search_input.grid(column=1, row=0)

        btns = LabelFrame(ui_search, borderwidth=0)
        btns.grid(column=0, row=1, pady=10)
        search_btn = Button(btns, text="Search",
                            command=lambda: self.display_notebook_by_date(search_input.get(), ui_search))
        cancel_btn = Button(btns, text="Cancel", command=lambda: self.dismiss(ui_search))
        search_btn.grid(column=0, row=3, ipadx=10, ipady=10, padx=(0, 15))
        cancel_btn.grid(column=1, row=3, ipadx=10, ipady=10)

        ui_search.grab_set()

    def get_note_data(self, event):
        for selection in self.table.selection():
            item = self.table.item(selection)
            return item["values"]

    def get_notes_data(self):
        data = []
        for note in self.table.get_children():
            data.append(self.table.item(note)["values"])
        return data

    def save_notes(self):
        notes_data = self.get_notes_data()
        for element in notes_data:
            notebook_data[element[0]] = (element[1], element[2], element[3])
        notebook_handler.save_data_base()

    def load_notes(self):
        notebook_handler.download_data_base()
        self.render_table()

    def start(self):
        self.ui.mainloop()
