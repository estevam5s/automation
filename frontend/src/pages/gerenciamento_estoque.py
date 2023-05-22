import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from deta import Deta


DETA_KEY = "e0zg3sgc85x_rLjU5Zy93MAHEY8UaoCnMGDJSNZiiHNR"

# Initialize Deta
deta = Deta(DETA_KEY)

lucro_db = deta.Base("analiseLucro")


def gerenciamento_estoque():
    # Consultar dados do banco lucro
    registros = lucro_db.fetch().items
    df = pd.DataFrame(registros)

    # Estoque total por item
    estoque_total = df.groupby('ITEM')['LUCRO'].sum()

    # Exibir estoque total por item
    st.subheader('Estoque Total por Item')
    st.write(estoque_total)

    # Estoque médio por item
    estoque_medio = df.groupby('ITEM')['LUCRO'].mean()

    # Exibir estoque médio por item
    st.subheader('Estoque Médio por Item')
    st.write(estoque_medio)

    # Estoque mínimo por item
    estoque_minimo = df.groupby('ITEM')['LUCRO'].min()

    # Exibir estoque mínimo por item
    st.subheader('Estoque Mínimo por Item')
    st.write(estoque_minimo)

    # Estoque máximo por item
    estoque_maximo = df.groupby('ITEM')['LUCRO'].max()

    # Exibir estoque máximo por item
    st.subheader('Estoque Máximo por Item')
    st.write(estoque_maximo)


def show_data():
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
    st.title("Gerenciamento de Estoque")

    st.markdown("Bem-vindo ao nosso sistema de gerenciamento de estoque!")
    st.markdown("Aqui você pode analisar os dados de lucro para realizar o gerenciamento de estoque de forma eficiente.")

    # Executa a função de gerenciamento de estoque
    gerenciamento_estoque()