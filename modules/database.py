import csv

class Database:
    def __init__(self, file_path):
        self.file_path = file_path
        self.records = []
        self.load_data()

    def load_data(self):
        with open(self.file_path, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            self.records = [row for row in reader]

    def get_all(self):
        return self.records
