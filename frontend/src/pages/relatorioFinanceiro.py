import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def gerar_relatorios_financeiros(file):
    # Carregar dados do arquivo CSV
    df = pd.read_csv(file)

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
    df['DATA'] = pd.to_datetime(df['DATA'])
    vendas_por_data = df.groupby(df['DATA'].dt.date)['LUCRO'].sum()
    vendas_por_data.plot(kind='line', ax=ax)
    ax.set_xlabel('Data')
    ax.set_ylabel('Vendas')
    ax.set_title('Vendas ao Longo do Tempo')
    st.pyplot(fig)
