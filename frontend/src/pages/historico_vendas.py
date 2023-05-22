from deta import Deta
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


DETA_KEY = "e0zg3sgc85x_rLjU5Zy93MAHEY8UaoCnMGDJSNZiiHNR"


# Initialize Deta
deta = Deta(DETA_KEY)

lucro_db = deta.Base("analiseLucro")


def main():
    # Consultar dados do banco
    registros = lucro_db.fetch().items

    # Criar listas vazias para cada coluna
    datas = []
    itens = []
    lucros = []

    # Extrair os dados de cada registro e armazenar nas listas correspondentes
    for registro in registros:
        datas.append(registro["DATA"])
        itens.append(registro["ITEM"])
        lucros.append(registro["LUCRO"])

    # Criar DataFrame com os dados
    data = {
        "DATA": datas,
        "ITEM": itens,
        "LUCRO": lucros
    }
    df = pd.DataFrame(data)

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


def gerar_historico_vendas():
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

    # Gerar histórico de vendas
    main()
