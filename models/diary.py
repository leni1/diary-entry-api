import re
from datetime import date


class Diary:

    def __init__(self, date, title, content):
        self.title = title
        self.date = date
        self.content = content


class Helper:

    def check_entry(self, title, content):

        str_args = [title, content]

        for arg in str_args:
            if not isinstance(arg, str):
                raise TypeError

        valid_title = re.search(r'^[A-Za-z\s]', title)
        valid_content = re.search(
            r'^[\w\d!@#$%^&*()-+_/|}{":;\'><~`.,?\s]', content)

        if valid_title and valid_content:
            return True
        return False

    def create_entry(self, title, content):

        if self.check_entry(title, content):
            entry_date = date.today()
            entry = Diary(entry_date, title, content)
            return entry
