import pandas as pd

def calcular_lucro(input_file, output_file):
    # Lê o arquivo CSV
    df = pd.read_csv(input_file)

    # Calcula o lucro
    df['LUCRO'] = df['ITEM'].apply(lambda x: int(x.split()[0]) * 10)

    # Salva o resultado em um novo arquivo CSV
    df.to_csv(output_file, index=False)
