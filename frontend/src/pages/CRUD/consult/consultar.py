import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Interface para consulta de lucros
class LucroConsultaInterface:
    def exibir_lucros(self, lucros):
        raise NotImplementedError

# Implementação da interface utilizando Streamlit
class LucroConsultaStreamlit(LucroConsultaInterface):
    def exibir_lucros(self, lucros):
        st.subheader('Tabela de Lucros')
        df_lucros = pd.DataFrame({'LUCRO': lucros})
        st.dataframe(df_lucros)

        st.subheader('Gráfico de Lucros')
        fig, ax = plt.subplots()
        ax.plot(np.arange(len(lucros)), lucros)
        ax.set_xlabel('Período')
        ax.set_ylabel('LUCRO')
        ax.set_title('Lucros ao longo do tempo')
        st.pyplot(fig)


# Serviço para obter os lucros
class LucroService:
    def __init__(self, lucro_query):
        self.lucro_query = lucro_query

    def obter_lucros(self):
        return self.lucro_query.obter_lucros()

# Query para buscar os lucros
class CsvLucroQuery:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def obter_lucros(self):
        df = pd.read_csv(self.csv_file)
        lucros = df['LUCRO'].tolist()
        return lucros
    

class Menu:
    def __init__(self):
        self.options = ["DATA", "ITEM", "ANOTAÇÕES"]
        self.selected_option = None
    
    def show(self):
        st.sidebar.title("Menu")
        self.selected_option = st.sidebar.selectbox("Selecione a coluna:", self.options)


class DataTable:
    def __init__(self, csv_file):
        self.csv_file = csv_file
    
    def load_data(self):
        return pd.read_csv(self.csv_file)
    
    def show_table(self, column):
        df = self.load_data()
        if column in df.columns:
            st.dataframe(df[column])
            
            # Insights Profissionais
            if column == "DATA":
                st.markdown("Essa coluna exibe a data em que os pedidos foram realizados.")
                st.markdown("Podemos observar os padrões de venda ao longo do tempo e identificar tendências sazonais.")
                
            elif column == "ITEM":
                st.markdown("Essa coluna exibe o tipo de item presente em cada pedido.")
                st.markdown("Podemos analisar quais tipos de marmitas são mais populares e ajustar o estoque e produção de acordo.")
                
            elif column == "ANOTAÇÕES":
                st.markdown("Essa coluna contém anotações adicionais relacionadas aos pedidos.")
                st.markdown("Podemos extrair informações úteis, como preferências dos clientes ou pedidos especiais, para melhorar a experiência do cliente.")
                
        else:
            st.error("A coluna selecionada não existe no conjunto de dados.")


def show_data_table():
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

    # Cria o menu e exibe
    menu = Menu()
    menu.show()

    # Cria a tabela de dados e exibe
    data_table = DataTable("app/data/pedidos.csv")
    data_table.show_table(menu.selected_option)


def __consult__():
    st.title("Consultar Dados")
    opcoes = ["Pedidos", "Lucro do Estabelecimento"]
    escolha = st.radio("Selecione o tipo de dado a ser consultado:", opcoes)

    if escolha == "Pedidos":
        show_data_table()
    elif escolha == "Lucro do Estabelecimento":
        st.title('Consulta de Lucros')
        csv_file = 'app/data/lucro.csv'
        # Check if a file is uploaded
        # Dependências
        lucro_query = CsvLucroQuery(csv_file)
        lucro_service = LucroService(lucro_query)
        lucro_interface = LucroConsultaStreamlit()
        lucros = lucro_service.obter_lucros()
        lucro_interface.exibir_lucros(lucros)