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

# Serviço para obter e atualizar os lucros
class LucroService:
    def __init__(self, lucro_query):
        self.lucro_query = lucro_query

    def obter_lucros(self):
        return self.lucro_query.obter_lucros()

    def atualizar_lucro(self, lucro_id, novo_lucro):
        self.lucro_query.salvar_lucro(lucro_id, novo_lucro)

# Query para buscar e salvar os lucros
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

# Função principal
def insertLucro(file):
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

# Interface para consulta de dados
class DadosConsultaInterface:
    def exibir_dados(self, dados):
        raise NotImplementedError

# Implementação da interface utilizando Streamlit
class DadosConsultaStreamlit(DadosConsultaInterface):
    def exibir_dados(self, dados):
        st.subheader('Tabela de Dados')
        df_dados = pd.DataFrame(dados)
        st.dataframe(df_dados)

        st.subheader('Gráfico de Dados')
        fig, ax = plt.subplots()
        ax.plot(np.arange(len(dados)), dados)
        ax.set_xlabel('Período')
        ax.set_ylabel('DADOS')
        ax.set_title('Dados ao longo do tempo')
        st.pyplot(fig)

# Serviço para obter e atualizar os dados
class DadosService:
    def __init__(self, dados_query):
        self.dados_query = dados_query

    def obter_dados(self):
        return self.dados_query.obter_dados()

    def atualizar_dado(self, dado_id, novo_dado):
        self.dados_query.salvar_dado(dado_id, novo_dado)

# Query para buscar e salvar os dados
class CsvDadosQuery:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def obter_dados(self):
        df = pd.read_csv(self.csv_file)
        dados = df['ITEM'].tolist()
        return dados

    def salvar_dado(self, dado_id, novo_dado):
        df = pd.read_csv(self.csv_file)
        df.loc[dado_id - 1, 'ITEM'] = novo_dado
        df.to_csv(self.csv_file, index=False)

# Função principal
def atualizarPedidos(file):
    csv_file = file
    dados_query = CsvDadosQuery(csv_file)
    dados_service = DadosService(dados_query)
    dados = dados_service.obter_dados()

    dados_interface = DadosConsultaStreamlit()
    dados_interface.exibir_dados(dados)

    st.sidebar.subheader('Atualizar Dado')
    dado_id = st.sidebar.selectbox('ID do Dado', range(1, len(dados)+1))
    novo_dado = st.sidebar.text_input('Novo Dado', value=dados[dado_id - 1])

    if st.sidebar.button('Atualizar'):
        dados_service.atualizar_dado(dado_id, novo_dado)
        st.sidebar.success(f'Dado ID {dado_id} atualizado com sucesso!')

def __atualizar__(lucro, pedido):
    st.title('Atualizar Dados')

    # Opções de atualização
    opcoes = ['Atualizar Pedidos', 'Atualizar Lucro do Estabelecimento']
    escolha = st.sidebar.selectbox('Escolha a opção', opcoes)

    # Verifica qual opção foi escolhida
    if escolha == 'Atualizar Pedidos':
        atualizarPedidos(pedido)
    elif escolha == 'Atualizar Lucro do Estabelecimento':
        insertLucro(lucro)