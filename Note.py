from datetime import datetime

class Note:
    def __init__(self, id, title, body, dateCreate):
        self.id = id
        self.title = title
        self.body = body
        self.dateCreate = dateCreate

    def to_dict(self):
        return {"id": self.id, "title": self.title, "body": self.body, "dateCreate": self.dateCreate}

