from model.csv_data_reader import CSVDataReader

class HomeService:
    def __init__(self):
        self.data_reader = CSVDataReader()

    def get_data(self):
        file_path = 'app/data/pedidos.csv'
        data = self.data_reader.read_data(file_path)
        return data
