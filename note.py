from datetime import datetime


class Note:

    def __init__(self):
        self.id = 0
        self.title = ""
        self.text = ""
        self.date = datetime.now().strftime("%d.%m.%y-%H:%M")

    def set_text(self, text):
        self.text = text

    def get_text(self):
        return self.text

    def set_title(self, text):
        self.title = text

    def get_title(self):
        return self.title

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def print_values(self):
        return f"{self.get_id()} {self.get_title()} {self.get_date()}"
