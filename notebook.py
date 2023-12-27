from note import Note


class Notebook:

    def __init__(self):
        self.notebook = []
        self.note = 0

    def check_id_existing(self, id):
        is_exist = True
        for note in self.notebook:
            if note.get_id() == id:
                is_exist = False
        return is_exist

    def add(self, title, text, id=0, *date):
        self.note = Note()
        self.note.set_title(title)
        self.note.set_text(text)
        if date:
            self.note.set_date(date)
        if self.note.get_id() == 0 and self.check_id_existing(id):
             self.note.set_id(id)
        self.notebook.append(self.note)

    def edit(self, id, title, text):
        for note in self.notebook:
            if int(note.get_id()) == int(id):
                note.set_title(title)
                note.set_text(text)

    def delete(self, id):
        for note in self.notebook:
            if int(note.get_id()) == int(id):
                self.notebook.remove(note)
