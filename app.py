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
from frontend.src.pages.help import help__
from frontend.src.pages.home import homePage
from frontend.src.pages.about import about__
from frontend.src.pages.documentacao import doc__
from frontend.src.pages.login import authenticate
from frontend.src.pages.developer import developers
from frontend.src.pages.suporte import suporteCliente
from frontend.src.pages.CRUD.delete.deletar import __delete__
from frontend.src.pages.gerenciamento_estoque import show_data
from frontend.src.pages.marmitas import show_data_table_marmita
from frontend.src.pages.CRUD.consult.consultar import __consult__
from frontend.src.pages.marmitaMaisVendidas import show_data_table
from frontend.src.pages.CRUD.update.atualizar import __atualizar__
from frontend.src.pages.gráficos.bolha.bubble import generate_chart
from frontend.src.pages.pedidosSemana import analise_pedidos_semana
from frontend.src.pages.analise_de_rentabilidade import show_analysis
from frontend.src.pages.historico_vendas import gerar_historico_vendas
from frontend.src.pages.estatisticaVendas import calcular_estatisticas_vendas
from frontend.src.pages.relatorioFinanceiro import gerar_relatorios_financeiros
from frontend.src.pages.CRUD.insert.inserir import __insert__, insert_data_lucro, insert_data_pedidos
from frontend.src.pages.traducao import translate_page


# Load environment variables
DETA_KEY = "e0zg3sgc85x_rLjU5Zy93MAHEY8UaoCnMGDJSNZiiHNR"

# Initialize Deta
deta = Deta(DETA_KEY)

db = deta.Base("database")
db_analysis = deta.Base("analysis")
lucro_db = deta.Base("analiseLucro")
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
        pass
    else:
        # Authenticate the user
        if 'authenticated' in st.session_state and st.session_state.authenticated:
            
            top_image = Image.open('frontend/src/pages/public/images/banner_top.png')
            bottom_image = Image.open('frontend/src/pages/public/images/banner_bottom.png')
            main_image = Image.open('frontend/src/pages/public/images/main_banner.png')
            st.image(main_image,use_column_width='auto')

            # Adiciona um sidebar
            st.sidebar.title("Opções de Consulta")
            selecionar = st.sidebar.selectbox("Selecione a página", 
                [
                    "🏠 Home",
                    "📲 Consult Analysis",
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
                    "🎆 Tipo de marmita menos vendido",
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

            if selecionar == "🧑🏻‍🦱 Suporte ao cliente":
                suporteCliente()

            if selecionar == "💾 Documentação":
                doc__()

            if selecionar == "🪖 Ajuda e suporte":
                help__()

            if selecionar == "Traduzir":
                translate_page()

            if selecionar == "⚠️ About":
                about__()

            if selecionar == "insert":
                # Inserir senha no banco de dados
                db.put({"password": "user"}, "user")

            if selecionar == "📲 Consult Analysis":
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

            if selecionar == "consult":
                result = db.get("user")

                if result:
                    password = result["password"]
                    st.title("Senha do usuário")
                    st.write(f"A senha do usuário é: {password}")
                else:
                    st.title("Usuário não encontrado")
                    st.write("Não foi possível encontrar a senha do usuário.")

            if selecionar == "📊 Gráfico":
                st.title("Análise de Dados de Pedidos - Gráficos")

                st.markdown("Bem-vindo à nossa ferramenta de análise de dados de pedidos!")
                st.markdown("Aqui você pode explorar e obter insights valiosos sobre os dados de pedidos da sua empresa.")

                chart_type = st.selectbox('Escolha o tipo de gráfico', ['bolha', 'bolha_modificado', 'dist', 'barra', 'linha', 'pizza', 'histograma', 'dispersao', 'matriz', 'funil', 'radar', 'area', 'torta', 'dendrograma', 'correlacao', 'waffle', 'calendario', 'radial'])
                generate_chart(pedidos_db, chart_type)

            if selecionar == "📈 Gerenciamento de estoque":
                show_data()

            if selecionar == "📋 Análise de Rentabilidade":
                show_analysis()

            if selecionar == "💼 Consultar":
                __consult__()

            if selecionar == "💻 Developers":
                developers()

            if selecionar == "🚫 Sair":
                logout()

            if selecionar == "📆 Histórico de vendas":
                gerar_historico_vendas()

            if selecionar == "🔮 Pedidos por Semana":
                analise_pedidos_semana()

            if selecionar == "📉 Estatísticas de vendas":
                calcular_estatisticas_vendas()

            if selecionar == "🎃 Tipo de marmita mais vendido":
                show_data_table()

            if selecionar == "📐 Relatórios financeiros":
                gerar_relatorios_financeiros()

            if selecionar == "🪀 Tipo de marita que saiu":
                st.title("Análise de Marmitas")
                show_data_table_marmita()

            if selecionar == "🔏 Inserir":
                __insert__()

            if selecionar == "🧨 Deletar":
                __delete__()

            if selecionar == "🖨️ Atualizar":
                __atualizar__()

            st.sidebar.image(top_image,use_column_width='auto')
            st.sidebar.image(bottom_image,use_column_width='auto')

        else:
            # Display login message if the user is not authenticated
            st.info("Please log in to access the system.")


if __name__ == "__main__":
    main()