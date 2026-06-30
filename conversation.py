import json
import os

FILE = r"C:\project_3\conversion_history\history.json"


class User_Conversation:

    def __init__(self):

        if os.path.exists(FILE):

            with open(FILE, "r") as f:
                self.history = json.load(f)

        else:
            self.history = []

    def add(self, text):

        self.history.append({

            "role": "user",
            "text": text

        })

        self.save()

    def save(self):

        with open(FILE, "w") as f:

            json.dump(self.history, f, indent=4)

    def get(self):

        return self.history