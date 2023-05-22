#                               File Name: app.py                                #
#                           Creation Date: 5 de maio, 2023                               #
#                         Source Language: Python                                          #
#         Repository:    https://github.com/                #
#                              --- Code Description ---                                    #
#         Streamlit app designed for visualizing U.S. real estate data and market trends   #
############################################################################################


import numpy as np
import pandas as pd
from PIL import Image
from deta import Deta
import streamlit as st
from frontend.src.pages.home import homePage
from frontend.src.pages.login import authenticate
from frontend.src.pages.developer import developers
from frontend.src.pages.marmitas import listar_tipos_marmita
from frontend.src.pages.CRUD.delete.deletar import __delete__
from frontend.src.pages.CRUD.insert.inserir import __insert__, insert_data_lucro, insert_data_pedidos
from frontend.src.pages.generate_insights import rentabilidade
from frontend.src.pages.analise_de_rentabilidade import analise
from frontend.src.pages.CRUD.consult.consultar import __consult__, consultar_dados_lucro, consultar_pedidos
from frontend.src.pages.CRUD.update.atualizar import __atualizar__
from frontend.src.pages.gráficos.bolha.bubble import generate_chart
from frontend.src.pages.pedidosSemana import analise_pedidos_semana
from frontend.src.pages.marmitaMaisVendidas import __main__Marmitas__
from frontend.src.pages.historico_vendas import gerar_historico_vendas
from frontend.src.pages.gerenciamento_estoque import gerenciamento_estoque
from frontend.src.pages.estatisticaVendas import calcular_estatisticas_vendas
from frontend.src.pages.relatorioFinanceiro import gerar_relatorios_financeiros


# Load environment variables
DETA_KEY = "e0u31gqkqju_2Ps7fJD5a1kAKF2Rr4Y31ASSdvUUeX8Y"

# Initialize Deta
deta = Deta(DETA_KEY)

db = deta.Base("users")
db_analysis = deta.Base("analysis")
lucro_db = deta.Base("lucro")
pedidos_db = deta.Base("pedidos")
rentabilidade_db = deta.Base("rentabilidade")


def logout():
    # Clear the authenticated session state
    st.session_state.pop('authenticated', None)
    # Rerun the script to replace the main page with the login page
    st.experimental_rerun()


def main() -> any:
    # Check if the user is authenticated
    if 'authenticated' not in st.session_state:
        # Authenticate the user
        authenticate()
    else:
        # Authenticate the user
        if 'authenticated' in st.session_state and st.session_state.authenticated:
            top_image = Image.open('frontend/src/pages/public/images/banner_top.png')
            bottom_image = Image.open('frontend/src/pages/public/images/banner_bottom.png')
            main_image = Image.open('frontend/src/pages/public/images/main_banner.png')
            st.image(main_image,use_column_width='auto')

            # Adiciona um sidebar
            st.sidebar.title("Opções de Consulta")
            selecionar = st.sidebar.selectbox("Selecione a página", [
                            "🏠 Home",
                            "insert",
                            "consult",
                            "insert Analysis",
                            "consult Analysis",
                            "Insert Dados importantes",
                            "Consult Dados importantes",
                            "📊 Gráfico",
                            "💼 Consultar",
                            "🔏 Inserir",
                            "🖨️ Atualizar",
                            "🧨 Deletar",
                            "📉 Estatísticas de vendas",
                            "📐 Relatórios financeiros",
                            "📌 Análise de tendências",
                            "📆 Histórico de vendas",
                            "📈 Gerenciamento de estoque",
                            "🎃 Tipo de marmita mais vendido",
                            "🎆 Tipo de marmita menos vendido".capitalize(),
                            "🎑 Tipo de marmita mais lucrativo",
                            "🧸 Tipo de marmita menos lucrativo",
                            "🪀 Tipo de marita que saiu",
                            "🔮 Pedidos por Semana",
                            "📋 Análise de Rentabilidade",
                            "💻 Developers",
                            "⚠️ About",
                            "🧑🏻‍🦱 Suporte ao cliente",
                            "💾 Documentação",
                            "🪖 Ajuda e suporte",
                            "🚫 Sair"
                            ]
                        )
            
            # Add restaurant information to the sidebar
            st.sidebar.title("Informações do Restaurante")
            st.sidebar.markdown("Este é um restaurante que oferece comida em marmitex.")
            st.sidebar.markdown("Faça uma análise de rentabilidade com base nos dados fornecidos.")

            # Executa a função correspondente com base na opção selecionada
            if selecionar == "🏠 Home":
                homePage()

            if selecionar == "insert":
                pass
                # Inserir senha no banco de dados
                db.put({"password": "user"}, "user")

            if selecionar == "consult Analysis":
                def query_data():
                    # Consulta os dados do banco 'analysis'
                    data = db_analysis.fetch().items

                    # Cria um DataFrame pandas com os dados consultados
                    df = pd.DataFrame(data, columns=['ID', 'DATA', 'ITEM', 'ANOTAÇÕES', 'Custo Total', 'Receita', 'Rentabilidade'])

                    # Exibe a tabela com pandas e numpy
                    st.title("Consulta de Dados")
                    st.dataframe(df)

                    # Exibe informações adicionais com numpy
                    st.subheader("Informações adicionais:")
                    st.write("Média da Receita:", np.mean(df['Receita']))
                    st.write("Máximo de Rentabilidade:", np.max(df['Rentabilidade']))
                    st.write("Mínimo de Custo Total:", np.min(df['Custo Total']))
                    st.write("Total de Itens:", np.sum(df['ITEM']))
                query_data()

            if selecionar == "Insert Dados importantes":
                insert_data_lucro()
                insert_data_pedidos()

            if selecionar == "Consult Dados importantes":
                pass
                # Chamada da função para consultar os pedidos
                consultar_pedidos()
                # Executar a função para exibir os dados
                consultar_dados_lucro()

            if selecionar == "insert Analysis":
                # Define a function to insert data into the 'analysis' database
                def insert_data():
                    data = [
                        {
                        "ID": 1,
                        "DATA": "2023-02-06 00:00:00",
                        "ITEM": 20,
                        "ANOTAÇÕES": 8,
                        "Custo Total": 160,
                        "Receita": 200,
                        "Rentabilidade": 25.0
                    },
                    {
                        "ID": 2,
                        "DATA": "2023-02-13 00:00:00",
                        "ITEM": 30,
                        "ANOTAÇÕES": 8,
                        "Custo Total": 240,
                        "Receita": 300,
                        "Rentabilidade": 25.0
                    },
                    {
                        "ID": 3,
                        "DATA": "2023-02-20 00:00:00",
                        "ITEM": 30,
                        "ANOTAÇÕES": 8,
                        "Custo Total": 240,
                        "Receita": 300,
                        "Rentabilidade": 25.0
                    },
                    {
                        "ID": 4,
                        "DATA": "2023-02-27 00:00:00",
                        "ITEM": 40,
                        "ANOTAÇÕES": 10,
                        "Custo Total": 400,
                        "Receita": 400,
                        "Rentabilidade": 0.0
                    },
                    {
                        "ID": 5,
                        "DATA": "2023-03-06 00:00:00",
                        "ITEM": 60,
                        "ANOTAÇÕES": 14,
                        "Custo Total": 840,
                        "Receita": 600,
                        "Rentabilidade": -28.57142857142857
                    },
                    {
                        "ID": 6,
                        "DATA": "2023-03-13 00:00:00",
                        "ITEM": 80,
                        "ANOTAÇÕES": 18,
                        "Custo Total": 1440,
                        "Receita": 800,
                        "Rentabilidade": -44.44444444444444
                    },
                    {
                        "ID": 7,
                        "DATA": "2023-03-20 00:00:00",
                        "ITEM": 70,
                        "ANOTAÇÕES": 18,
                        "Custo Total": 1260,
                        "Receita": 700,
                        "Rentabilidade": -44.44444444444444
                    },
                    {
                        "ID": 8,
                        "DATA": "2023-03-27 00:00:00",
                        "ITEM": 70,
                        "ANOTAÇÕES": 18,
                        "Custo Total": 1260,
                        "Receita": 700,
                        "Rentabilidade": -44.44444444444444
                    },
                    {
                        "ID": 9,
                        "DATA": "2023-04-03 00:00:00",
                        "ITEM": 90,
                        "ANOTAÇÕES": 24,
                        "Custo Total": 2160,
                        "Receita": 900,
                        "Rentabilidade": -58.333333333333336
                    },
                    {
                        "ID": 10,
                        "DATA": "2023-04-10 00:00:00",
                        "ITEM": 100,
                        "ANOTAÇÕES": 30,
                        "Custo Total": 3000,
                        "Receita": 1000,
                        "Rentabilidade": -66.66666666666666
                    },
                    {
                        "ID": 11,
                        "DATA": "2023-04-17 00:00:00",
                        "ITEM": 120,
                        "ANOTAÇÕES": 30,
                        "Custo Total": 3600,
                        "Receita": 1200,
                        "Rentabilidade": -66.66666666666666
                    },
                    {
                        "ID": 12,
                        "DATA": "2023-04-24 00:00:00",
                        "ITEM": 100,
                        "ANOTAÇÕES": 28,
                        "Custo Total": 2800,
                        "Receita": 1000,
                        "Rentabilidade": -64.28571428571429
                    },
                    {
                        "ID": 13,
                        "DATA": "2023-05-01 00:00:00",
                        "ITEM": 110,
                        "ANOTAÇÕES": 30,
                        "Custo Total": 3300,
                        "Receita": 1100,
                        "Rentabilidade": -66.66666666666666
                    },
                    {
                        "ID": 14,
                        "DATA": "2023-05-08 00:00:00",
                        "ITEM": 130,
                        "ANOTAÇÕES": 34,
                        "Custo Total": 4420,
                        "Receita": 1300,
                        "Rentabilidade": -70.58823529411765
                    },
                    {
                        "ID": 15,
                        "DATA": "2023-05-15 00:00:00",
                        "ITEM": 130,
                        "ANOTAÇÕES": 38,
                        "Custo Total": 4940,
                        "Receita": 1300,
                        "Rentabilidade": -73.68421052631578
                    }
                ]

                    # Insert the data into the 'analysis' database
                    db_analysis.put_many(data)

                # Call the insert_data function to insert the data into the 'analysis' database
                insert_data()

            
            if selecionar == "consult":# Consultar senha do banco de dados
                result = db.get("user")

                if result:
                    password = result["password"]
                    st.title("Senha do usuário")
                    st.write(f"A senha do usuário é: {password}")
                else:
                    st.title("Usuário não encontrado")
                    st.write("Não foi possível encontrar a senha do usuário.")

            if selecionar == "📊 Gráfico":
                csv_file = 'app/data/pedidos.csv'  # Caminho relativo para o arquivo .csv
                # Exemplo de uso
                chart_type = st.selectbox('Escolha o tipo de gráfico', ['bolha', 'barra', 'linha', 'pizza', 'histograma', 'dispersao', 'matriz', 'funil', 'radar', 'area', 'torta', 'dendrograma', 'correlacao', 'waffle', 'calendario', 'radial'])
                generate_chart(csv_file, chart_type)

            if selecionar == "🔮 Pedidos por Semana":
                csv_file = 'app/data/pedidos.csv'
                # Perform analysis on the weekly orders
                analise_pedidos_semana(csv_file)

            if selecionar == "🎃 Tipo de marmita mais vendido":
                csv_file = 'app/data/pedidos.csv'
                __main__Marmitas__(csv_file)

            if selecionar == "📈 Gerenciamento de estoque":
                lucro = 'app/data/lucro.csv'
                # Chamar a função
                gerenciamento_estoque(lucro)

            if selecionar == "📋 Análise de Rentabilidade":
                lucro = 'app/data/lucro.csv'
                rentabilidadeCSV = 'app/data/rentabilidade.csv'
                rentabilidade(lucro, rentabilidadeCSV)

            if selecionar == "📆 Histórico de vendas":
                # Chamar a função
                gerar_historico_vendas(lucro)

            if selecionar == "📉 Estatísticas de vendas":
                lucro = 'app/data/lucro.csv'
                # Chamar a função
                calcular_estatisticas_vendas(lucro)

            if selecionar == "📐 Relatórios financeiros":
                csv_file = 'app/data/lucro.csv'
                # Check if a file is uploaded
                if csv_file is not None:
                    # Perform analysis and display the results
                    gerar_relatorios_financeiros(csv_file)

            if selecionar == "💼 Consultar":
                __consult__()

            if selecionar == "🖨️ Atualizar":
                pedido = 'app/data/pedidos.csv'
                lucro = 'app/data/lucro.csv'
                __atualizar__(lucro, pedido)

            if selecionar == "🧨 Deletar":
                lucro = 'app/data/lucro.csv'
                pedido = 'app/data/pedidos.csv'
                __delete__(lucro, pedido)

            if selecionar == "🔏 Inserir":
                lucro = 'app/data/lucro.csv'
                pedido = 'app/data/pedidos.csv'
                __insert__(lucro, pedido)

            if selecionar == "🪀 Tipo de marita que saiu":
                csv_file = 'app/data/pedidos.csv'
                st.title("Análise de Marmitas")

                # Selecionar arquivo CSV
                # csv_file = st.file_uploader("Carregar arquivo CSV", type=['csv'])

                if csv_file is not None:
                    # Chamar função para listar tipos de marmita e gerar gráfico
                    listar_tipos_marmita(csv_file)

            if selecionar == "💻 Developers":
                developers()

            if selecionar == "🚫 Sair":
                logout()

            st.sidebar.image(top_image,use_column_width='auto')
            st.sidebar.image(bottom_image,use_column_width='auto')

        else:
            # Display login message if the user is not authenticated
            st.info("Please log in to access the system.")


if __name__ == "__main__":
    main()