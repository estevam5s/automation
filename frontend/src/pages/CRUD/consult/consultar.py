import numpy as np
import pandas as pd
from deta import Deta
import streamlit as st
import matplotlib.pyplot as plt


DETA_KEY = "e0zg3sgc85x_rLjU5Zy93MAHEY8UaoCnMGDJSNZiiHNR"
# Initialize Deta
deta = Deta(DETA_KEY)

pedidos_db = deta.Base("pedidos")
lucro_db = deta.Base("analiseLucro")


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
class DetaLucroQuery:
    def __init__(self, db):
        self.db = db

    def obter_lucros(self):
        registros = self.db.fetch().items
        lucros = [registro["LUCRO"] for registro in registros]
        return lucros
    

class Menu:
    def __init__(self):
        self.options = ["DATA", "ITEM", "ANOTAÇÕES"]
        self.selected_option = None
    
    def show(self):
        st.sidebar.title("Menu")
        self.selected_option = st.sidebar.selectbox("Selecione a coluna:", self.options)


def show_data_table_lucro():
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

    # Cria o menu e exibe
    menu = Menu()
    menu.show()

    # Cria o serviço de lucro
    lucro_query = DetaLucroQuery(lucro_db)
    lucro_service = LucroService(lucro_query)

    # Obtém os lucros
    lucros = lucro_service.obter_lucros()

    # Cria a interface de consulta de lucros e exibe
    lucro_consulta = LucroConsultaStreamlit()
    lucro_consulta.exibir_lucros(lucros)


class DataTable:
    def __init__(self, db):
        self.db = db
    
    def load_data(self):
        # Consultar todos os registros no banco de dados
        registros = self.db.fetch().items

        # Criar listas vazias para cada coluna
        ids = []
        datas = []
        itens = []
        anotacoes = []

        # Extrair os dados de cada registro e armazenar nas listas correspondentes
        for registro in registros:
            ids.append(registro["ID"])
            datas.append(registro["DATA"])
            itens.append(registro["ITEM"])
            anotacoes.append(registro["ANOTAÇÕES"])

        # Criar um DataFrame com os dados
        data = {
            "ID": ids,
            "DATA": datas,
            "ITEM": itens,
            "ANOTAÇÕES": anotacoes
        }
        df = pd.DataFrame(data)
        return df
    
    def show_table(self, column):
        df = self.load_data()
        if column in df.columns:
            st.dataframe(df[column])
            
            # Insights Profissionais
            if column == "DATA":
                st.markdown("Essa coluna exibe a data em que os pedidos foram realizados.")
                st.markdown("Podemos observar os padrões de venda ao longo do tempo e identificar tendências sazonais.")
                
            elif column == "ITEM":
                st.markdown("Essa coluna exibe o tipo de item presente em cada pedido.")
                st.markdown("Podemos analisar quais tipos de marmitas são mais populares e ajustar o estoque e produção de acordo.")
                
            elif column == "ANOTAÇÕES":
                st.markdown("Essa coluna contém anotações adicionais relacionadas aos pedidos.")
                st.markdown("Podemos extrair informações úteis, como preferências dos clientes ou pedidos especiais, para melhorar a experiência do cliente.")
                
        else:
            st.error("A coluna selecionada não existe no conjunto de dados.")


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
    st.title("Análise de Dados de Pedidos")

    st.markdown("Bem-vindo à nossa ferramenta de análise de dados de pedidos!")
    st.markdown("Aqui você pode explorar e obter insights valiosos sobre os dados de pedidos da sua empresa.")

    # Cria o menu e exibe
    menu = Menu()
    menu.show()

    # Cria a tabela de dados e exibe
    data_table = DataTable(pedidos_db)
    data_table.show_table(menu.selected_option)


def __consult__():
    st.title("Consultar Dados")
    opcoes = ["Pedidos", "Lucro do Estabelecimento"]
    escolha = st.radio("Selecione o tipo de dado a ser consultado:", opcoes)

    if escolha == "Pedidos":
        show_data_table()
    elif escolha == "Lucro do Estabelecimento":
        st.title('Consulta de Lucros')
        show_data_table_lucro()


def consultar_pedidos():
    # Consultar todos os pedidos
    pedidos = pedidos_db.fetch().items

    # Criar uma lista vazia para armazenar os dados dos pedidos
    lista_pedidos = []

    # Preencher a lista com os dados dos pedidos
    for pedido in pedidos:
        lista_pedidos.append(pedido)

    # Criar um DataFrame a partir da lista de pedidos
    df = pd.DataFrame(lista_pedidos)

    # Reordenar as colunas do DataFrame
    df = df[['ID', 'DATA', 'ITEM', 'ANOTAÇÕES']]

    # Exibir o DataFrame usando o Streamlit
    st.title("Pedidos")
    st.dataframe(df)


def consultar_dados_lucro():
    # Consultar todos os registros no banco de dados
    registros = pedidos_db.fetch().items

    # Criar listas vazias para cada coluna
    ids = []
    datas = []
    itens = []
    anotacoes = []
    lucros = []

    # Extrair os dados de cada registro e armazenar nas listas correspondentes
    for registro in registros:
        ids.append(registro["ID"])
        datas.append(registro["DATA"])
        itens.append(registro["ITEM"])
        anotacoes.append(registro["ANOTAÇÕES"])
        if "LUCRO" in registro:
            lucros.append(registro["LUCRO"])
        else:
            lucros.append(np.nan)

    # Criar um DataFrame com os dados
    data = {
        "ID": ids,
        "DATA": datas,
        "ITEM": itens,
        "ANOTAÇÕES": anotacoes,
        "LUCRO": lucros
    }
    df = pd.DataFrame(data)

    # Exibir os dados usando o Streamlit
    st.title("Consulta de Dados - Lucro")
    st.table(df)
