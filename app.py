#                               File Name: app.py                                #
#                           Creation Date: 5 de maio, 2023                               #
#                         Source Language: Python                                          #
#         Repository:    https://github.com/                #
#                              --- Code Description ---                                    #
#         Streamlit app designed for visualizing U.S. real estate data and market trends   #
############################################################################################
# e0zg3sgc85x_ceEEmEgJp3ivsXKEsU12aG9scwQFSKWg


from PIL import Image
from deta import Deta
import streamlit as st
from frontend.src.pages.generate_insights import rentabilidade
from frontend.src.pages.gerenciamento_estoque import gerenciamento_estoque
from frontend.src.pages.historico_vendas import gerar_historico_vendas
from frontend.src.pages.home import homePage
from frontend.src.pages.developer import developers
from frontend.src.pages.marmitas import listar_tipos_marmita
from frontend.src.pages.login import authenticate
from frontend.src.pages.estatisticaVendas import calcular_estatisticas_vendas
from frontend.src.pages.CRUD.delete.deletar import __delete__
from frontend.src.pages.CRUD.insert.inserir import __insert__
from frontend.src.pages.analise_de_rentabilidade import analise
from frontend.src.pages.CRUD.consult.consultar import __consult__
from frontend.src.pages.CRUD.update.atualizar import __atualizar__
from frontend.src.pages.gráficos.bolha.bubble import generate_chart
from frontend.src.pages.pedidosSemana import analise_pedidos_semana
from frontend.src.pages.marmitaMaisVendidas import __main__Marmitas__
from frontend.src.pages.relatorioFinanceiro import gerar_relatorios_financeiros



# Load environment variables
DETA_KEY = "e0u31gqkqju_2Ps7fJD5a1kAKF2Rr4Y31ASSdvUUeX8Y"

# Initialize Deta
deta = Deta(DETA_KEY)

db = deta.Base("users")


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