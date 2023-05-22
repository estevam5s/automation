import csv
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class CsvWriter:
    def __init__(self, filename):
        self.filename = filename

    def write_data(self, data):
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
# perfeito, só que mostra os dados em forma de tabela com pandas e numpy e com gráficos antes de enviar os dados
class Pedido:
    def __init__(self, id, data, item, anotacoes):
        self.id = id
        self.data = data
        self.item = item
        self.anotacoes = anotacoes

    def to_list(self):
        return [self.id, self.data, self.item, self.anotacoes]

def insertPedidos(file):
    filename = file
    writer = CsvWriter(filename)

    ID = st.text_input("ID:")
    DATA = st.text_input("DATA:")
    ITEM = st.text_input("ITEM:")
    anotacoes = st.text_input("ANOTAÇÕES:")

    pedido = Pedido(ID, DATA, ITEM, anotacoes)
    data_to_write = pedido.to_list()

    if st.button("Visualizar Dados"):
        # Cria um dataframe com os dados inseridos
        df = pd.DataFrame([data_to_write], columns=['ID', 'DATA', 'ITEM', 'ANOTAÇÕES'])
        
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
        writer.write_data(data_to_write)
        st.write("Dados inseridos com sucesso!")



# lucro

class Lucro:
    def __init__(self, id, data, item, anotacoes, lucro):
        self.id = id
        self.data = data
        self.item = item
        self.anotacoes = anotacoes
        self.lucro = lucro

    def to_list(self):
        return [self.id, self.data, self.item, self.anotacoes, self.lucro]

def insertLucro(file):
    filename = file
    writer = CsvWriter(filename)

    ID = st.text_input("ID:")
    DATA = st.text_input("DATA:")
    item = st.text_input("ITEM:")
    anotacoes = st.text_input("ANOTAÇÕES:")
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

    lucro_obj = Lucro(ID, DATA, item, anotacoes, lucro_float)
    data_to_write = lucro_obj.to_list()

    # Exibir tabela de dados
    st.subheader('Dados inseridos')
    df = pd.DataFrame([data_to_write], columns=['ID', 'DATA', 'ITEM', 'ANOTAÇÕES', 'LUCRO'])
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
        writer.write_data(data_to_write)
        st.write("Dados inseridos com sucesso!")



def __insert__(lucro, pedidos):
    st.title("Inserir Dados")
    opcoes = ["Pedidos", "Lucro do Estabelecimento"]
    escolha = st.radio("Selecione o tipo de dado a ser inserido:", opcoes)

    if escolha == "Pedidos":
        insertPedidos(pedidos)
    elif escolha == "Lucro do Estabelecimento":
        insertLucro(lucro)