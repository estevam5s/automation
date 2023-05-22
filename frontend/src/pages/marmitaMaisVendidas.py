import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

class MarmitaService:
    def __init__(self, csv_file):
        self.csv_file = csv_file
    
    def carregar_dados(self):
        try:
            return pd.read_csv(self.csv_file)
        except FileNotFoundError:
            st.error("Arquivo CSV não encontrado.")
    
    def listar_tipos_marmita(self, df):
        if 'ITEM' not in df.columns:
            st.error("A coluna 'ITEM' não foi encontrada no arquivo CSV.")
            return
        
        tipos_marmita = df['ITEM'].str.split(' ').str[1].unique()
        return tipos_marmita
    
    def obter_tipo_marmita_mais_vendido(self, df):
        if 'ITEM' not in df.columns:
            st.error("A coluna 'ITEM' não foi encontrada no arquivo CSV.")
            return
        
        tipo_mais_vendido = df['ITEM'].str.split(' ').str[1].value_counts().idxmax()
        return tipo_mais_vendido

def __main__Marmitas__(csv_file_methodo=None):
    st.set_option('deprecation.showPyplotGlobalUse', False)  # Desabilitar aviso de depreciação
    st.title("Análise de Marmitas")
    st.sidebar.title("Informações Úteis")
    
    # Selecionar arquivo CSV
    csv_file = csv_file_methodo

    if csv_file is not None:
        marmita_service = MarmitaService(csv_file)
        df = marmita_service.carregar_dados()
        
        # Exibir informações úteis no sidebar
        st.sidebar.subheader("Resumo do Arquivo")
        st.sidebar.text(f"Número de Linhas: {df.shape[0]}")
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