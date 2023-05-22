import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def calcular_estatisticas_vendas(file):
    # Carregar dados do arquivo CSV
    df = pd.read_csv(file)

    # Estatísticas gerais
    vendas_totais = df['LUCRO'].sum()
    vendas_por_categoria = df.groupby('ITEM')['LUCRO'].sum()
    vendas_por_regiao = df.groupby('ANOTAÇÕES')['LUCRO'].sum()

    # Exibir estatísticas gerais
    st.subheader('Estatísticas de Vendas')
    st.write('Vendas Totais:', vendas_totais)

    st.subheader('Vendas por Categoria')
    st.dataframe(vendas_por_categoria)

    st.subheader('Vendas por Anotações')
    st.dataframe(vendas_por_regiao)

    # Gráfico de vendas por categoria
    st.subheader('Gráfico de Vendas por Categoria')
    fig, ax = plt.subplots()
    vendas_por_categoria.plot(kind='bar', ax=ax)
    ax.set_xlabel('Categoria')
    ax.set_ylabel('Vendas')
    ax.set_title('Vendas por Categoria')
    st.pyplot(fig)

    # Gráfico de vendas por Anotações
    st.subheader('Gráfico de Vendas por Anotações')
    fig, ax = plt.subplots()
    vendas_por_regiao.plot(kind='bar', ax=ax)
    ax.set_xlabel('Anotações')
    ax.set_ylabel('Vendas')
    ax.set_title('Vendas por Anotações')
    st.pyplot(fig)