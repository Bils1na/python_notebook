from notebook import Notebook
import file_handler


def download_data_base():
    notebook.notebook.clear()
    json_data = file_handler.pull_db()
    for element in json_data.items():
        notebook.add(element[1][0], element[1][2], element[1][1])


def save_data_base():
    file_handler.push_db(data)


notebook = Notebook()
data = {}
