import streamlit as st
import pandas as pd

def gerenciamento_estoque(file):
    # Carregar dados do arquivo CSV
    df = pd.read_csv(file)

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