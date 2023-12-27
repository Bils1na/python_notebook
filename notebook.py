from note import Note


class Notebook:

    def __init__(self):
        self.notebook = []
        self.note = 0

    def add(self, title, text, id=0, *date):
        self.note = Note()
        self.note.set_title(title)
        self.note.set_text(text)
        if date:
            self.note.set_date(date)
        if self.note.get_id() == 0:
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
