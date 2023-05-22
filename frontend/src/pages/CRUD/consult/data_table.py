import streamlit as st
import pandas as pd


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
