import pandas as pd
import streamlit as st

class RentabilidadeAnalyzer:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def load_data(self):
        df = pd.read_csv(self.input_file)
        return df

    def calculate_rentabilidade(self, df):
        # Cálculos de rentabilidade
        df['CUSTO'] = df['LUCRO'] * 0.2  # Exemplo de cálculo de custo (20% do lucro)
        df['QUANTIDADE'] = df['LUCRO'] / df['CUSTO']  # Exemplo de cálculo de quantidade

        return df

    def generate_rentabilidade_csv(self, df):
        df.to_csv(self.output_file, index=False)

    def analyze_rentabilidade(self):
        df = self.load_data()
        df = self.calculate_rentabilidade(df)
        self.generate_rentabilidade_csv(df)

        # Insights
        total_rentabilidade = df['LUCRO'].sum()
        total_custo = df['CUSTO'].sum()
        total_quantidade = df['QUANTIDADE'].sum()

        # Exibir insights com Streamlit
        st.title("Análise de Rentabilidade")
        st.write("Total de Rentabilidade:", total_rentabilidade)
        st.write("Total de Custo:", total_custo)
        st.write("Total de Quantidade:", total_quantidade)


# Criar instância do analisador de rentabilidade
def rentabilidade(file, newfile):

    # Criar instância do analisador de rentabilidade
    analyzer = RentabilidadeAnalyzer(file, newfile)

    # Gerar insights
    analyzer.analyze_rentabilidade()
