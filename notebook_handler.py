from notebook import Notebook
import file_handler


def download_data_base():
    global note_id
    notebook.notebook.clear()
    json_data = file_handler.pull_db()
    for element in json_data.items():
        note_id += 1
        notebook.add(element[1][0], element[1][2], element[0], element[1][1])


def save_data_base():
    file_handler.push_db(data)


notebook = Notebook()
data = {}
note_id = 0
