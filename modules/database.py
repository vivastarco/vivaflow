import csv

class Database:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = []
        self.load_data()

    def load_data(self):
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            self.data = [row for row in reader]

    def get_all(self):
        return self.data
