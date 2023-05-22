from deta import Deta
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


DETA_KEY = "e0zg3sgc85x_rLjU5Zy93MAHEY8UaoCnMGDJSNZiiHNR"

# Initialize Deta
deta = Deta(DETA_KEY)

lucro_db = deta.Base("analiseLucro")


def main():
    # Consultar dados do banco "lucro"
    registros = lucro_db.fetch().items

    # Criar DataFrame com os dados
    df = pd.DataFrame(registros)

    # Converter coluna "DATA" para formato de data
    df['DATA'] = pd.to_datetime(df['DATA'])

    # Total de vendas
    vendas_totais = df['LUCRO'].sum()

    # Relatório financeiro
    relatorio_financeiro = {
        'Total de Vendas': vendas_totais,
        'Média de Vendas': df['LUCRO'].mean(),
        'Maior Venda': df['LUCRO'].max(),
        'Menor Venda': df['LUCRO'].min(),
    }

    # Exibir relatório financeiro
    st.subheader('Relatório Financeiro')
    st.write(pd.DataFrame.from_dict(relatorio_financeiro, orient='index', columns=['Valor']))

    # Gráfico de vendas ao longo do tempo
    st.subheader('Gráfico de Vendas ao Longo do Tempo')
    fig, ax = plt.subplots()
    vendas_por_data = df.groupby(df['DATA'].dt.date)['LUCRO'].sum()
    vendas_por_data.plot(kind='line', ax=ax)
    ax.set_xlabel('Data')
    ax.set_ylabel('Vendas')
    ax.set_title('Vendas ao Longo do Tempo')
    st.pyplot(fig)


def gerar_relatorios_financeiros():
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

    # Título e descrição
    st.title("Relatórios Financeiros")
    st.markdown("Bem-vindo ao sistema de relatórios financeiros!")
    st.markdown("Aqui você pode gerar insights valiosos com base nos dados de lucro da empresa.")

    # Gerar relatórios financeiros
    main()