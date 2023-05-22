import csv
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
db_analysis = deta.Base("analysis")


class Pedido:
    def __init__(self, id, data, item, anotacoes):
        self.id = id
        self.data = data
        self.item = item
        self.anotacoes = anotacoes

    def to_dict(self):
        return {
            "ID": self.id,
            "DATA": self.data,
            "ITEM": self.item,
            "ANOTAÇÕES": self.anotacoes
        }


def insertPedidos():
    ID = st.text_input("ID:")
    DATA = st.text_input("DATA:")
    ITEM = st.text_input("ITEM:")
    anotacoes = st.text_input("ANOTAÇÕES:")

    pedido = Pedido(ID, DATA, ITEM, anotacoes)

    if st.button("Visualizar Dados"):
        # Cria um dataframe com os dados inseridos
        df = pd.DataFrame([pedido.to_dict()])
        
        # Exibe a tabela com os dados usando pandas
        st.write(df)
        
        # Cria um gráfico de barras simples com o ID e o ITEM
        plt.bar(df['ID'], df['ITEM'])
        plt.xlabel('ID')
        plt.ylabel('ITEM')
        plt.title('Gráfico de Itens por ID')
        
        # Exibe o gráfico usando matplotlib
        st.pyplot(plt)

    if st.button("Enviar"):
        pedidos_db.put(pedido.to_dict())
        st.write("Dados inseridos com sucesso!")


class Lucro:
    def __init__(self, id, data, item, anotacoes, lucro):
        self.id = id
        self.data = data
        self.item = item
        self.anotacoes = anotacoes
        self.lucro = lucro

    def to_dict(self):
        return {
            "ID": self.id,
            "DATA": self.data,
            "ITEM": self.item,
            "ANOTAÇÕES": self.anotacoes,
            "LUCRO": self.lucro
        }

def insertLucro():
    ID = st.text_input("ID:")
    DATA = st.text_input("DATA:")
    ITEM = st.text_input("ITEM:")
    ANOTACOES = st.text_input("ANOTAÇÕES:")
    LUCRO = st.text_input("LUCRO:")

    if LUCRO:
        try:
            lucro_float = float(LUCRO)
        except ValueError:
            st.error("O valor de LUCRO deve ser um número válido.")
            return
    else:
        st.error("O valor de LUCRO não pode estar vazio.")
        return

    lucro = Lucro(ID, DATA, ITEM, ANOTACOES, lucro_float)
    data_to_insert = lucro.to_dict()

    # Exibir tabela de dados
    st.subheader('Dados inseridos')
    df = pd.DataFrame([data_to_insert], columns=['ID', 'DATA', 'ITEM', 'ANOTAÇÕES', 'LUCRO'])
    st.dataframe(df)

    # Exibir gráfico de lucro
    st.subheader('Gráfico de Lucro')
    lucros = [lucro_float]
    fig, ax = plt.subplots()
    ax.plot(np.arange(len(lucros)), lucros)
    ax.set_xlabel('Período')
    ax.set_ylabel('LUCRO')
    ax.set_title('Lucros ao longo do tempo')
    st.pyplot(fig)

    if st.button("Salvar"):
        lucro_db.put(data_to_insert)
        st.write("Dados inseridos com sucesso!")


def __insert__():
    st.title("Inserir Dados")
    opcoes = ["Pedidos", "Lucro do Estabelecimento"]
    escolha = st.radio("Selecione o tipo de dado a ser inserido:", opcoes)

    if escolha == "Pedidos":
        insertPedidos()
    elif escolha == "Lucro do Estabelecimento":
        insertLucro()


def insert_data_lucro():
    data = [
        {
            "ID": 1,
            "DATA": "2023-02-06 00:00:00",
            "ITEM": "200 Marmitas",
            "ANOTAÇÕES": "8 Panqueca bolonhesa, 4 Estrogonofe de frango, 4 File de peito de frango, 4 Sobrecoxa de desossada grelhada, 0 Sobrecoxa desossada ensopada",
            "LUCRO": 2000
        },
        {
            "ID": 2,
            "DATA": "2023-02-13 00:00:00",
            "ITEM": "30 Marmitas",
            "ANOTAÇÕES": "8 Panqueca bolonhesa, 8 Estrogonofe de frango, 4 File de peito de frango, 6 Sobrecoxa de desossada grelhada, 4 Sobrecoxa desossada ensopada",
            "LUCRO": 300
        },
        {
            "ID": 3,
            "DATA": "2023-02-20 00:00:00",
            "ITEM": "30 Marmitas",
            "ANOTAÇÕES": "8 Panqueca bolonhesa, 8 Estrogonofe de frango, 6 File de peito de frango, 4 Sobrecoxa de desossada grelhada, 4 Sobrecoxa desossada ensopada",
            "LUCRO": 300
        },
        {
            "ID": 4,
            "DATA": "2023-02-27 00:00:00",
            "ITEM": "40 Marmitas",
            "ANOTAÇÕES": "10 Panqueca bolonhesa, 8 Estrogonofe de frango, 8 File de peito de frango, 8 Sobrecoxa de desossada grelhada, 6 Sobrecoxa desossada ensopada",
            "LUCRO": 400
        },
        {
            "ID": 5,
            "DATA": "2023-03-06 00:00:00",
            "ITEM": "60 Marmitas",
            "ANOTAÇÕES": "14 Panqueca bolonhesa, 12 Estrogonofe de frango, 12 File de peito de frango, 12 Sobrecoxa de desossada grelhada, 10 Sobrecoxa desossada ensopada",
            "LUCRO": 600
        },
        {
            "ID": 6,
            "DATA": "2023-03-13 00:00:00",
            "ITEM": "80 Marmitas",
                        "ANOTAÇÕES": "18 Panqueca bolonhesa, 16 Estrogonofe de frango, 12 File de peito de frango, 20 Sobrecoxa de desossada grelhada, 14 Sobrecoxa desossada ensopada",
            "LUCRO": 800
        },
        {
            "ID": 7,
            "DATA": "2023-03-20 00:00:00",
            "ITEM": "70 Marmitas",
            "ANOTAÇÕES": "18 Panqueca bolonhesa, 16 Estrogonofe de frango, 14 File de peito de frango, 10 Sobrecoxa de desossada grelhada, 12 Sobrecoxa desossada ensopada",
            "LUCRO": 700
        },
        {
            "ID": 8,
            "DATA": "2023-03-27 00:00:00",
            "ITEM": "70 Marmitas",
            "ANOTAÇÕES": "18 Panqueca bolonhesa, 12 Estrogonofe de frango, 10 File de peito de frango, 14 Sobrecoxa de desossada grelhada, 16 Sobrecoxa desossada ensopada",
            "LUCRO": 700
        },
        {
            "ID": 9,
            "DATA": "2023-04-03 00:00:00",
            "ITEM": "90 Marmitas",
            "ANOTAÇÕES": "24 Panqueca bolonhesa, 18 Estrogonofe de frango, 16 File de peito de frango, 16 Sobrecoxa de desossada grelhada, 16 Sobrecoxa desossada ensopada",
            "LUCRO": 900
        },
        {
            "ID": 10,
            "DATA": "2023-04-10 00:00:00",
            "ITEM": "100 Marmitas",
            "ANOTAÇÕES": "30 Panqueca bolonhesa, 18 Estrogonofe de frango, 20 File de peito de frango, 16 Sobrecoxa de desossada grelhada, 16 Sobrecoxa desossada ensopada",
            "LUCRO": 1000
        },
        {
            "ID": 11,
            "DATA": "2023-04-17 00:00:00",
            "ITEM": "120 Marmitas",
            "ANOTAÇÕES": "30 Panqueca bolonhesa, 18 Estrogonofe de frango, 26 File de peito de frango, 24 Sobrecoxa de desossada grelhada, 22 Sobrecoxa desossada ensopada",
            "LUCRO": 1200
        },
        {
            "ID": 12,
            "DATA": "2023-04-24 00:00:00",
            "ITEM": "100 Marmitas",
            "ANOTAÇÕES": "28 Panqueca bolonhesa, 20 Estrogonofe de frango, 18 File de peito de frango, 18 Sobrecoxa de desossada grelhada, 16 Sobrecoxa desossada ensopada",
            "LUCRO": 1000
        },
        {
            "ID": 13,
            "DATA": "2023-05-01 00:00:00",
            "ITEM": "110 Marmitas",
            "ANOTAÇÕES": "30 Panqueca bolonhesa, 22 Estrogonofe de frango, 20 File de peito de frango, 20 Sobrecoxa de desossada grelhada, 18 Sobrecoxa desossada ensopada",
            "LUCRO": 1100
        },
        {
            "ID": 14,
            "DATA": "2023-05-08 00:00:00",
            "ITEM": "130 Marmitas",
            "ANOTAÇÕES": "34 Panqueca bolonhesa, 26 Estrogonofe de frango, 24 File de peito de frango, 24 Sobrecoxa de desossada grelhada, 22 Sobrecoxa desossada ensopada",
            "LUCRO": 1300
        },
        {
            "ID": 15,
            "DATA": "2023-05-15 00:00:00",
            "ITEM": "130 Marmitas",
            "ANOTAÇÕES": "38 Panqueca bolonhesa, 30 Estrogonofe de frango, 20 File de peito de frango, 22 Sobrecoxa de desossada grelhada, 20 Sobrecoxa desossada ensopada",
            "LUCRO": 1300
        }
    ]

    # Insert the data into the 'analysis' database
    lucro_db.put_many(data)


def insert_data_pedidos():
    data = [
        {
            "ID": 1,
            "DATA": "2023-02-06 00:00:00",
            "ITEM": "200 Marmitas",
            "ANOTAÇÕES": "8 Panqueca bolonhesa, 4 Estrogonofe de frango, 4 File de peito de frango, 4 Sobrecoxa de desossada grelhada, 0 Sobrecoxa desossada ensopada"
        },
        {
            "ID": 2,
            "DATA": "2023-02-13 00:00:00",
            "ITEM": "30 Marmitas",
            "ANOTAÇÕES": "8 Panqueca bolonhesa, 8 Estrogonofe de frango, 4 File de peito de frango, 6 Sobrecoxa de desossada grelhada, 4 Sobrecoxa desossada ensopada"
        },
        {
            "ID": 3,
            "DATA": "2023-02-20 00:00:00",
            "ITEM": "30 Marmitas",
            "ANOTAÇÕES": "8 Panqueca bolonhesa, 8 Estrogonofe de frango, 6 File de peito de frango, 4 Sobrecoxa de desossada grelhada, 4 Sobrecoxa desossada ensopada"
        },
        {
            "ID": 4,
            "DATA": "2023-02-27 00:00:00",
            "ITEM": "40 Marmitas",
            "ANOTAÇÕES": "10 Panqueca bolonhesa, 8 Estrogonofe de frango, 8 File de peito de frango, 8 Sobrecoxa de desossada grelhada, 6 Sobrecoxa desossada ensopada"
        },
        {
            "ID": 5,
            "DATA": "2023-03-06 00:00:00",
            "ITEM": "60 Marmitas",
            "ANOTAÇÕES": "14 Panqueca bolonhesa, 12 Estrogonofe de frango, 12 File de peito de frango, 12 Sobrecoxa de desossada grelhada, 10 Sobrecoxa desossada ensopada"
        },
        {
            "ID": 6,
            "DATA": "2023-03-13 00:00:00",
            "ITEM": "80 Marmitas",
            "ANOTAÇÕES": "18 Panqueca bolonhesa, 16 Estrogonofe de frango, 12 File de peito de frango, 20 Sobrecoxa de desossada grelhad, 14 Sobrecoxa desossada ensopada"
        },
        {
            "ID": 7,
            "DATA": "2023-03-20 00:00:00",
            "ITEM": "70 Marmitas",
            "ANOTAÇÕES": "18 Panqueca bolonhesa, 16 Estrogonofe de frango, 14 File de peito de frango, 10 Sobrecoxa de desossada grelhada, 12 Sobrecoxa desossada ensopada"
        },
        {
            "ID": 8,
            "DATA": "2023-03-27 00:00:00",
            "ITEM": "70 Marmitas",
            "ANOTAÇÕES": "18 Panqueca bolonhesa, 12 Estrogonofe de frango, 10 File de peito de frango, 14 Sobrecoxa de desossada grelhada, 16 Sobrecoxa desossada ensopada"
        },
        {
            "ID": 9,
            "DATA": "2023-04-03 00:00:00",
            "ITEM": "90 Marmitas",
            "ANOTAÇÕES": "24 Panqueca bolonhesa, 18 Estrogonofe de frango, 16 File de peito de frango, 16 Sobrecoxa de desossada grelhada, 16 Sobrecoxa desossada ensopada"
        },
        {
            "ID": 10,
            "DATA": "2023-04-10 00:00:00",
            "ITEM": "100 Marmitas",
            "ANOTAÇÕES": "30 Panqueca bolonhesa, 18 Estrogonofe de frango, 20 File de peito de frango, 16 Sobrecoxa de desossada grelhada, 16 Sobrecoxa desossada ensopada"
        },
        {
            "ID": 11,
            "DATA": "2023-04-17 00:00:00",
            "ITEM": "120 Marmitas",
            "ANOTAÇÕES": "30 Panqueca bolonhesa, 18 Estrogonofe de frango, 26 File de peito de frango, 24 Sobrecoxa de desossada grelhada, 22 Sobrecoxa desossada ensopada"
        },
        {
            "ID": 12,
            "DATA": "2023-04-24 00:00:00",
            "ITEM": "100 Marmitas",
            "ANOTAÇÕES": "28 Panqueca bolonhesa, 20 Estrogonofe de frango, 18 File de peito de frango, 18 Sobrecoxa de desossada grelhada, 16 Sobrecoxa desossada ensopada"
        },
            {
            "ID": 13,
            "DATA": "2023-05-01 00:00:00",
            "ITEM": "110 Marmitas",
            "ANOTAÇÕES": "30 Panqueca bolonhesa, 22 Estrogonofe de frango, 20 File de peito de frango, 20 Sobrecoxa de desossada grelhada, 18 Sobrecoxa desossada ensopada"
        },
        {
            "ID": 14,
            "DATA": "2023-05-08 00:00:00",
            "ITEM": "130 Marmitas",
            "ANOTAÇÕES": "34 Panqueca bolonhesa, 26 Estrogonofe de frango, 24 File de peito de frango, 24 Sobrecoxa de desossada grelhada, 22 Sobrecoxa desossada ensopada"
        },
        {
            "ID": 15,
            "DATA": "2023-05-15 00:00:00",
            "ITEM": "130 Marmitas",
            "ANOTAÇÕES": "38 Panqueca bolonhesa, 30 Estrogonofe de frango, 20 File de peito de frango, 22 Sobrecoxa de desossada grelhada, 20 Sobrecoxa desossada ensopada"
        }
    ]

    # Insert the data into the 'analysis' database
    pedidos_db.put_many(data)


def insert_data():
    data = [
        {
            "ID": 1,
            "DATA": "2023-02-06 00:00:00",
            "ITEM": 20,
            "ANOTAÇÕES": 8,
            "Custo Total": 160,
            "Receita": 200,
            "Rentabilidade": 25.0
        },
        {
            "ID": 2,
            "DATA": "2023-02-13 00:00:00",
            "ITEM": 30,
            "ANOTAÇÕES": 8,
            "Custo Total": 240,
            "Receita": 300,
            "Rentabilidade": 25.0
        },
        {
            "ID": 3,
            "DATA": "2023-02-20 00:00:00",
            "ITEM": 30,
            "ANOTAÇÕES": 8,
            "Custo Total": 240,
            "Receita": 300,
            "Rentabilidade": 25.0
        },
        {
            "ID": 4,
            "DATA": "2023-02-27 00:00:00",
            "ITEM": 40,
            "ANOTAÇÕES": 10,
            "Custo Total": 400,
            "Receita": 400,
            "Rentabilidade": 0.0
        },
        {
            "ID": 5,
            "DATA": "2023-03-06 00:00:00",
            "ITEM": 60,
            "ANOTAÇÕES": 14,
            "Custo Total": 840,
            "Receita": 600,
            "Rentabilidade": -28.57142857142857
        },
        {
            "ID": 6,
            "DATA": "2023-03-13 00:00:00",
            "ITEM": 80,
            "ANOTAÇÕES": 18,
            "Custo Total": 1440,
            "Receita": 800,
            "Rentabilidade": -44.44444444444444
        },
        {
            "ID": 7,
            "DATA": "2023-03-20 00:00:00",
            "ITEM": 70,
            "ANOTAÇÕES": 18,
            "Custo Total": 1260,
            "Receita": 700,
            "Rentabilidade": -44.44444444444444
        },
        {
            "ID": 8,
            "DATA": "2023-03-27 00:00:00",
            "ITEM": 70,
            "ANOTAÇÕES": 18,
            "Custo Total": 1260,
            "Receita": 700,
            "Rentabilidade": -44.44444444444444
        },
        {
            "ID": 9,
            "DATA": "2023-04-03 00:00:00",
            "ITEM": 90,
            "ANOTAÇÕES": 24,
            "Custo Total": 2160,
            "Receita": 900,
            "Rentabilidade": -58.333333333333336
        },
        {
            "ID": 10,
            "DATA": "2023-04-10 00:00:00",
            "ITEM": 100,
            "ANOTAÇÕES": 30,
            "Custo Total": 3000,
            "Receita": 1000,
            "Rentabilidade": -66.66666666666666
        },
        {
            "ID": 11,
            "DATA": "2023-04-17 00:00:00",
            "ITEM": 120,
            "ANOTAÇÕES": 30,
            "Custo Total": 3600,
            "Receita": 1200,
            "Rentabilidade": -66.66666666666666
        },
        {
            "ID": 12,
            "DATA": "2023-04-24 00:00:00",
            "ITEM": 100,
            "ANOTAÇÕES": 28,
            "Custo Total": 2800,
            "Receita": 1000,
            "Rentabilidade": -64.28571428571429
        },
        {
            "ID": 13,
            "DATA": "2023-05-01 00:00:00",
            "ITEM": 110,
            "ANOTAÇÕES": 30,
            "Custo Total": 3300,
            "Receita": 1100,
            "Rentabilidade": -66.66666666666666
        },
        {
            "ID": 14,
            "DATA": "2023-05-08 00:00:00",
            "ITEM": 130,
            "ANOTAÇÕES": 34,
            "Custo Total": 4420,
            "Receita": 1300,
            "Rentabilidade": -70.58823529411765
        },
        {
            "ID": 15,
            "DATA": "2023-05-15 00:00:00",
            "ITEM": 130,
            "ANOTAÇÕES": 38,
            "Custo Total": 4940,
            "Receita": 1300,
            "Rentabilidade": -73.68421052631578
        }
    ]

    # Insert the data into the 'analysis' database
    db_analysis.put_many(data)
