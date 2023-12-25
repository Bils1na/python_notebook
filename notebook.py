from note import Note

class Notebook():

    def __init__(self):
        self.notebook = []

    def add(self, text):
        self.note = Note()
        self.note.set_text(text)
        self.notebook.append(self.note)
