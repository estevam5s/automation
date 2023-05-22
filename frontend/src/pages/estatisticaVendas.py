from deta import Deta
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


DETA_KEY = "e0zg3sgc85x_rLjU5Zy93MAHEY8UaoCnMGDJSNZiiHNR"

# Initialize Deta
deta = Deta(DETA_KEY)

lucro_db = deta.Base("analiseLucro")


def main():
    # Consultar dados do banco Deta
    registros = lucro_db.fetch().items
    df = pd.DataFrame(registros)

    # Estatísticas gerais
    vendas_totais = df['LUCRO'].sum()
    vendas_por_categoria = df.groupby('ITEM')['LUCRO'].sum()
    vendas_por_anotacoes = df.groupby('ANOTAÇÕES')['LUCRO'].sum()

    # Exibir estatísticas gerais
    st.subheader('Estatísticas de Vendas')
    st.write('Vendas Totais:', vendas_totais)

    st.subheader('Vendas por Categoria')
    st.dataframe(vendas_por_categoria)

    st.subheader('Vendas por Anotações')
    st.dataframe(vendas_por_anotacoes)

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
    vendas_por_anotacoes.plot(kind='bar', ax=ax)
    ax.set_xlabel('Anotações')
    ax.set_ylabel('Vendas')
    ax.set_title('Vendas por Anotações')
    st.pyplot(fig)


def calcular_estatisticas_vendas():
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

    main()