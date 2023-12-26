from note import Note


class Notebook:

    def __init__(self):
        self.notebook = []
        self.note = ""

    def add(self, title, text):
        self.note = Note()
        self.note.set_title(title)
        self.note.set_text(text)
        self.notebook.append(self.note)
