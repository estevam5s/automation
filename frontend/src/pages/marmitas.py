import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def listar_tipos_marmita(csv_file):
    try:
        # Carregar dados do arquivo CSV
        df = pd.read_csv(csv_file)

        # Verificar se a coluna 'ITEM' existe no DataFrame
        if 'ITEM' not in df.columns:
            st.error("A coluna 'ITEM' não foi encontrada no arquivo CSV.")
            return

        # Extrair os tipos de marmita da coluna 'ITEM'
        tipos_marmita = df['ITEM'].str.split(' ').str[1].unique()

        # Imprimir os tipos de marmita
        st.text("Tipos de Marmita:")
        for tipo in tipos_marmita:
            st.text(tipo)

        # Gerar gráfico de contagem de marmitas por tipo
        counts = df['ITEM'].str.split(' ').str[1].value_counts()
        fig, ax = plt.subplots()
        ax.bar(counts.index, counts.values)
        ax.set_xlabel('Tipo de Marmita')
        ax.set_ylabel('Quantidade')
        ax.set_title('Tipos de Marmita Vendidos')
        ax.set_xticklabels(counts.index, rotation=45)
        st.pyplot(fig)

    except FileNotFoundError:
        st.error("Arquivo CSV não encontrado.")