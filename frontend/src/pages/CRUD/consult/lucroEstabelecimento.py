import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Interface para consulta de lucros
class LucroConsultaInterface:
    def exibir_lucros(self, lucros):
        raise NotImplementedError

# Implementação da interface utilizando Streamlit
class LucroConsultaStreamlit(LucroConsultaInterface):
    def exibir_lucros(self, lucros):
        st.subheader('Tabela de Lucros')
        df_lucros = pd.DataFrame({'LUCRO': lucros})
        st.dataframe(df_lucros)

        st.subheader('Gráfico de Lucros')
        fig, ax = plt.subplots()
        ax.plot(np.arange(len(lucros)), lucros)
        ax.set_xlabel('Período')
        ax.set_ylabel('LUCRO')
        ax.set_title('Lucros ao longo do tempo')
        st.pyplot(fig)

# Serviço para obter os lucros
class LucroService:
    def __init__(self, lucro_query):
        self.lucro_query = lucro_query

    def obter_lucros(self):
        return self.lucro_query.obter_lucros()

# Query para buscar os lucros
class CsvLucroQuery:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def obter_lucros(self):
        df = pd.read_csv(self.csv_file)
        lucros = df['LUCRO'].tolist()
        return lucros



