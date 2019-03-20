import re


class Diary:

    def __init__(self, eid, edate, title, content):
        self.eid = eid
        self.title = title
        self.edate = edate
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
