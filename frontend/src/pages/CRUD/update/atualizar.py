import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from deta import Deta


DETA_KEY = "e0zg3sgc85x_rLjU5Zy93MAHEY8UaoCnMGDJSNZiiHNR"

# Initialize Deta
deta = Deta(DETA_KEY)

lucro_db = deta.Base("analiseLucro")
pedidos_db = deta.Base("pedidos")


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
        lucro = self.lucro_query.obter_lucro_por_id(lucro_id)
        if lucro:
            lucro["LUCRO"] = novo_lucro
            self.lucro_query.salvar_lucro(lucro)
            return True
        return False

# Query para buscar e salvar os lucros
class DetaLucroQuery:
    def __init__(self, db):
        self.db = db

    def obter_lucros(self):
        registros = self.db.fetch().items
        lucros = [registro["LUCRO"] for registro in registros]
        return lucros

    def obter_lucro_por_id(self, lucro_id):
        return self.db.get(str(lucro_id)).item

    def salvar_lucro(self, lucro):
        self.db.put(lucro)

# Função principal
def insertLucro():
    lucro_query = DetaLucroQuery(lucro_db)
    lucro_service = LucroService(lucro_query)
    lucros = lucro_service.obter_lucros()

    lucro_interface = LucroConsultaStreamlit()
    lucro_interface.exibir_lucros(lucros)

    st.sidebar.subheader('Atualizar Lucro')
    lucro_id = st.sidebar.selectbox('ID do Lucro', range(1, len(lucros)+1))
    novo_lucro = st.sidebar.number_input('Novo Lucro', value=lucros[lucro_id - 1])

    if st.sidebar.button('Atualizar'):
        if lucro_service.atualizar_lucro(lucro_id, novo_lucro):
            st.sidebar.success(f'Lucro ID {lucro_id} atualizado com sucesso!')
        else:
            st.sidebar.error(f'Lucro ID {lucro_id} não encontrado.')



def show_data_table():
    # Configura a cor de fundo para verde
    st.markdown(
        """
            <style>
                body {
                    background-color: #00FF00;
                }
            </style>
        """,
        unsafe_allow_html=True
    )

    # Insights Criativos
    st.title("Análise de Dados de Lucro")

    st.markdown("Bem-vindo à nossa ferramenta de análise de dados de lucro!")
    st.markdown("Aqui você pode explorar e obter insights valiosos sobre os dados de lucro da sua empresa.")

    # Cria o serviço de lucro
    lucro_query = DetaLucroQuery(lucro_db)
    lucro_service = LucroService(lucro_query)

    # Obtém os lucros
    lucros = lucro_service.obter_lucros()

    # Cria a interface de consulta de lucros e exibe
    lucro_consulta = LucroConsultaStreamlit()
    lucro_consulta.exibir_lucros(lucros)

    st.sidebar.subheader('Atualizar Lucro')
    lucro_id = st.sidebar.selectbox('ID do Lucro', range(1, len(lucros)+1))
    novo_lucro = st.sidebar.number_input('Novo Lucro', value=lucros[lucro_id - 1])

    if st.sidebar.button('Atualizar'):
        if lucro_service.atualizar_lucro(lucro_id, novo_lucro):
            st.sidebar.success(f'Lucro ID {lucro_id} atualizado com sucesso!')
        else:
            st.sidebar.error(f'Lucro ID {lucro_id} não encontrado.')


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
        registros = self.dados_query.obter_registros()
        registros[dado_id - 1]["ITEM"] = novo_dado
        self.dados_query.salvar_registros(registros)

# Query para buscar e salvar os dados
class DetaDadosQuery:
    def __init__(self, db):
        self.db = db

    def obter_dados(self):
        registros = self.db.fetch().items
        dados = [registro["ITEM"] for registro in registros]
        return dados

    def obter_registros(self):
        return self.db.fetch().items

    def salvar_registros(self, registros):
        self.db.put_many(registros)

# Função principal
def atualizarPedidos():
    dados_query = DetaDadosQuery(pedidos_db)
    dados_service = DadosService(dados_query)
    dados = dados_service.obter_dados()

    dados_interface = DadosConsultaStreamlit()
    dados_interface.exibir_dados(dados)

    st.sidebar.subheader('Atualizar Dado')
    dado_id = st.sidebar.selectbox('ID do Dado', range(1, len(dados) + 1))
    novo_dado = st.sidebar.text_input('Novo Dado', value=dados[dado_id - 1])

    if st.sidebar.button('Atualizar'):
        dados_service.atualizar_dado(dado_id, novo_dado)
        st.sidebar.success(f'Dado ID {dado_id} atualizado com sucesso!')



def __atualizar__():
    st.title('Atualizar Dados')

    # Opções de atualização
    opcoes = ['Atualizar Pedidos', 'Atualizar Lucro do Estabelecimento']
    escolha = st.sidebar.selectbox('Escolha a opção', opcoes)

    # Verifica qual opção foi escolhida
    if escolha == 'Atualizar Pedidos':
        # Executa a função principal
        atualizarPedidos()
    elif escolha == 'Atualizar Lucro do Estabelecimento':
        show_data_table()