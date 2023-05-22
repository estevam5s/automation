import csv

class CSVDataReader:
    def read_data(self, file_path):
        data = []
        with open(file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
        return data
