from note import Note


class Notebook:

    def __init__(self):
        self.notebook = []
        self.note = 0

    def add(self, title, text, *date):
        self.note = Note()
        self.note.set_title(title)
        self.note.set_text(text)
        if date:
            self.note.set_date(date)
        self.notebook.append(self.note)
