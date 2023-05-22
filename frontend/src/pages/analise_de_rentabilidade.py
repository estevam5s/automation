from deta import Deta
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

DETA_KEY = "e0zg3sgc85x_rLjU5Zy93MAHEY8UaoCnMGDJSNZiiHNR"

# Initialize Deta
deta = Deta(DETA_KEY)

analysis_db = deta.Base("analysis")

def analise():
    # Consultar todos os registros no banco de dados
    registros = analysis_db.fetch().items

    # Criar listas vazias para cada coluna
    ids = []
    datas = []
    itens = []
    anotacoes = []
    custo_total = []
    receita = []
    rentabilidade = []

    # Extrair os dados de cada registro e armazenar nas listas correspondentes
    for registro in registros:
        ids.append(registro["ID"])
        datas.append(registro["DATA"])
        itens.append(registro["ITEM"])
        anotacoes.append(registro["ANOTAÇÕES"])
        custo_total.append(registro["Custo Total"])
        receita.append(registro["Receita"])
        rentabilidade.append(registro["Rentabilidade"])

    # Criar um DataFrame com os dados
    data = {
        "ID": ids,
        "DATA": datas,
        "ITEM": itens,
        "ANOTAÇÕES": anotacoes,
        "Custo Total": custo_total,
        "Receita": receita,
        "Rentabilidade": rentabilidade
    }
    df = pd.DataFrame(data)

    # Create a bar chart for the profitability analysis
    fig, ax = plt.subplots()
    ax.bar(df['ID'], df['Rentabilidade'])
    ax.set_title('Análise de Rentabilidade')
    ax.set_xlabel('ID')
    ax.set_ylabel('Rentabilidade')

    # Display the chart in Streamlit
    st.pyplot(fig)


def show_analysis():
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
    st.title("Análise de Rentabilidade")

    st.markdown("Bem-vindo à nossa ferramenta de análise de rentabilidade!")
    st.markdown("Aqui você pode explorar e obter insights valiosos sobre a rentabilidade dos seus dados de análise.")

    # Exibir a análise
    analise()
