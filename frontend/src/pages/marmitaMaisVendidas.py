from deta import Deta
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

DETA_KEY = "e0zg3sgc85x_rLjU5Zy93MAHEY8UaoCnMGDJSNZiiHNR"

# Initialize Deta
deta = Deta(DETA_KEY)

pedidos_db = deta.Base("pedidos")

class MarmitaService:
    def __init__(self, db):
        self.db = db
    
    def carregar_dados(self):
        registros = self.db.fetch().items
        df = pd.DataFrame(registros)
        return df
    
    def listar_tipos_marmita(self, df):
        if 'ITEM' not in df.columns:
            st.error("A coluna 'ITEM' não foi encontrada nos dados.")
            return
        
        tipos_marmita = df['ITEM'].str.split(' ').str[1].unique()
        return tipos_marmita
    
    def obter_tipo_marmita_mais_vendido(self, df):
        if 'ITEM' not in df.columns:
            st.error("A coluna 'ITEM' não foi encontrada nos dados.")
            return
        
        tipo_mais_vendido = df['ITEM'].str.split(' ').str[1].value_counts().idxmax()
        return tipo_mais_vendido

def show_data_table():
    st.set_option('deprecation.showPyplotGlobalUse', False)  # Desabilitar aviso de depreciação
    st.title("Análise de Marmitas")
    st.sidebar.title("Informações Úteis")
    
    # Cria o serviço de marmitas
    marmita_service = MarmitaService(pedidos_db)

    # Carrega os dados dos pedidos
    df = marmita_service.carregar_dados()

    # Exibir informações úteis no sidebar
    st.sidebar.subheader("Resumo dos Dados")
    st.sidebar.text(f"Número de Registros: {len(df)}")
    st.sidebar.text(f"Número de Colunas: {df.shape[1]}")
    
    # Listar tipos de marmita
    tipos_marmita = marmita_service.listar_tipos_marmita(df)
    
    if tipos_marmita is not None:
        st.subheader("Tipos de Marmita")
        for tipo in tipos_marmita:
            st.text(tipo)
        
        # Exibir tipo de marmita mais vendido
        tipo_mais_vendido = marmita_service.obter_tipo_marmita_mais_vendido(df)
        st.subheader("Tipo de Marmita Mais Vendido")
        st.text(tipo_mais_vendido)
        
        # Gerar gráfico de contagem de marmitas por tipo
        counts = df['ITEM'].str.split(' ').str[1].value_counts()
        fig, ax = plt.subplots()
        ax.bar(counts.index, counts.values)
        ax.set_xlabel('Tipo de Marmita')
        ax.set_ylabel('Quantidade')
        ax.set_title('Tipos de Marmita Vendidos')
        ax.set_xticklabels(counts.index, rotation=45)
        st.pyplot(fig)
