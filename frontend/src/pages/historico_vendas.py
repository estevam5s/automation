import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def gerar_historico_vendas(file):
    # Carregar dados do arquivo CSV
    df = pd.read_csv(file)

    # Converter a coluna DATA para o tipo datetime
    df['DATA'] = pd.to_datetime(df['DATA'])

    # Ordenar o DataFrame pelo campo DATA
    df = df.sort_values('DATA')

    # Exibir o histórico de vendas
    st.subheader('Histórico de Vendas')
    st.dataframe(df)

    # Gráfico de vendas por item
    st.subheader('Vendas por Item')
    fig, ax = plt.subplots()
    vendas_por_item = df.groupby('ITEM')['LUCRO'].sum()
    vendas_por_item.plot(kind='bar', ax=ax)
    ax.set_xlabel('Item')
    ax.set_ylabel('Vendas')
    ax.set_title('Vendas por Item')
    st.pyplot(fig)

    # Gráfico de vendas por mês
    st.subheader('Vendas por Mês')
    fig, ax = plt.subplots()
    vendas_por_mes = df.groupby(df['DATA'].dt.to_period('M'))['LUCRO'].sum()
    vendas_por_mes.plot(kind='bar', ax=ax)
    ax.set_xlabel('Mês')
    ax.set_ylabel('Vendas')
    ax.set_title('Vendas por Mês')
    st.pyplot(fig)