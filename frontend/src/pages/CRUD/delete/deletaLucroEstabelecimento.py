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
        df_lucros = pd.DataFrame({'ID': range(1, len(lucros)+1), 'LUCRO': lucros})
        st.dataframe(df_lucros)

        st.subheader('Gráfico de Lucros')
        fig, ax = plt.subplots()
        ax.plot(np.arange(len(lucros)), lucros)
        ax.set_xlabel('Período')
        ax.set_ylabel('LUCRO')
        ax.set_title('Lucros ao longo do tempo')
        st.pyplot(fig)

# Serviço para obter, atualizar e excluir os lucros
class LucroService:
    def __init__(self, lucro_query):
        self.lucro_query = lucro_query

    def obter_lucros(self):
        return self.lucro_query.obter_lucros()

    def atualizar_lucro(self, lucro_id, novo_lucro):
        self.lucro_query.salvar_lucro(lucro_id, novo_lucro)

    def excluir_lucro(self, lucro_id):
        self.lucro_query.excluir_lucro(lucro_id)

# Query para buscar, salvar e excluir os lucros
class CsvLucroQuery:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def obter_lucros(self):
        df = pd.read_csv(self.csv_file)
        lucros = df['LUCRO'].tolist()
        return lucros

    def salvar_lucro(self, lucro_id, novo_lucro):
        df = pd.read_csv(self.csv_file)
        df.loc[lucro_id - 1, 'LUCRO'] = novo_lucro
        df.to_csv(self.csv_file, index=False)

    def excluir_lucro(self, lucro_id):
        df = pd.read_csv(self.csv_file)
        df.drop(lucro_id - 1, inplace=True)
        df.reset_index(drop=True, inplace=True)
        df.to_csv(self.csv_file, index=False)

# Função principal
def deleteLucro(file):
    csv_file = file
    lucro_query = CsvLucroQuery(csv_file)
    lucro_service = LucroService(lucro_query)
    lucros = lucro_service.obter_lucros()

    lucro_interface = LucroConsultaStreamlit()
    lucro_interface.exibir_lucros(lucros)

    st.sidebar.subheader('Atualizar Lucro')
    lucro_id = st.sidebar.selectbox('ID do Lucro', range(1, len(lucros)+1))
    novo_lucro = st.sidebar.number_input('Novo Lucro', value=lucros[lucro_id - 1])

    if st.sidebar.button('Atualizar'):
        lucro_service.atualizar_lucro(lucro_id, novo_lucro)
        st.sidebar.success(f'Lucro ID {lucro_id} atualizado com sucesso!')

    st.sidebar.subheader('Excluir Lucro')
    lucro_id = st.sidebar.selectbox('ID do Lucro', range(1, len(lucros) + 1), key="excluir_lucro")

    if st.sidebar.button('Excluir'):
        lucro_service.excluir_lucro(lucro_id)
        st.sidebar.success(f'Lucro ID {lucro_id} excluído com sucesso!')
