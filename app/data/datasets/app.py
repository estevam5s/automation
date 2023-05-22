import pandas as pd

def convert_xlsx_to_csv(xlsx_file, csv_file):
    # Ler o arquivo Excel (.xlsx) e carregar em um DataFrame
    df = pd.read_excel(xlsx_file)
    
    # Salvar o DataFrame em um arquivo CSV
    df.to_csv(csv_file, index=False)

# Exemplo de uso da função
xlsx_file = 'data.xlsx'  # Substitua pelo caminho e nome do seu data .xlsx
csv_file = 'data.csv'  # Nome do data .csv de saída
convert_xlsx_to_csv(xlsx_file, csv_file)
