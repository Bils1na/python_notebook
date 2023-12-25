import notebook

if __name__ == '__main__':
    note = notebook.Notebook();

    note.set_text("Note #1")
    print(note.get_text())