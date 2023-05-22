from deta import Deta
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

DETA_KEY = "e0zg3sgc85x_rLjU5Zy93MAHEY8UaoCnMGDJSNZiiHNR"

# Initialize Deta
deta = Deta(DETA_KEY)

pedidos_db = deta.Base("pedidos")

def listar_tipos_marmita():
    try:
        # Consultar todos os registros no banco de dados
        registros = pedidos_db.fetch().items

        # Verificar se a coluna 'ITEM' existe nos registros
        tipos_marmita = set()
        for registro in registros:
            if 'ITEM' in registro:
                item = registro['ITEM']
                tipo_marmita = item.split(' ')[1]
                tipos_marmita.add(tipo_marmita)

        # Imprimir os tipos de marmita
        st.text("Tipos de Marmita:")
        for tipo in tipos_marmita:
            st.text(tipo)

        # Gerar gráfico de contagem de marmitas por tipo
        counts = {}
        for registro in registros:
            if 'ITEM' in registro:
                item = registro['ITEM']
                tipo_marmita = item.split(' ')[1]
                counts[tipo_marmita] = counts.get(tipo_marmita, 0) + 1

        fig, ax = plt.subplots()
        ax.bar(counts.keys(), counts.values())
        ax.set_xlabel('Tipo de Marmita')
        ax.set_ylabel('Quantidade')
        ax.set_title('Tipos de Marmita Vendidos')
        ax.set_xticklabels(counts.keys(), rotation=45)
        st.pyplot(fig)

    except Exception as e:
        st.error("Ocorreu um erro ao consultar os dados do banco de dados.")
        st.error(str(e))

def show_data_table_marmita():
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

    listar_tipos_marmita()
