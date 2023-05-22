#                               File Name: app.py                                #
#                           Creation Date: 5 de maio, 2023                               #
#                         Source Language: Python                                          #
#         Repository:    https://github.com/                #
#                              --- Code Description ---                                    #
#         Streamlit app designed for visualizing U.S. real estate data and market trends   #
############################################################################################
# e0zg3sgc85x_ceEEmEgJp3ivsXKEsU12aG9scwQFSKWg


from PIL import Image
import streamlit as st
from frontend.src.pages.home import homePage
from frontend.src.pages.developer import developers
from frontend.src.pages.lucroCSV import calcular_lucro
from frontend.src.pages.marmitas import listar_tipos_marmita
from frontend.src.pages.CRUD.delete.deletar import __delete__
from frontend.src.pages.CRUD.consult.consultar import __consult__
from frontend.src.pages.analise_de_rentabilidade import analise
from frontend.src.pages.CRUD.update.atualizar import __atualizar__
from frontend.src.pages.gráficos.bolha.bubble import generate_chart
from frontend.src.pages.pedidosSemana import analise_pedidos_semana
from frontend.src.pages.marmitaMaisVendidas import __main__Marmitas__


def autenticar_usuario(senha):
    # Lógica de autenticação aqui
    # Se a autenticação for bem-sucedida, redireciona para a página principal
    st.experimental_set_query_params()
    st.experimental_rerun()

def authenticate():
    # Define a password for authentication
    password = "user"

    # Check if the session state has already been set
    if 'authenticated' not in st.session_state:
        # Display login form
        st.title("Authentication")
        password_input = st.text_input("Enter password", type="password")
        login_button = st.button("Log In")
        if login_button and password_input == password:
            st.session_state.authenticated = True
            with st.spinner("Carregando..."):
                st.success("Login efetuado com sucesso!")
                st.balloons()

            # Rerun the script to replace the login page with the main page
            st.experimental_rerun()

        elif login_button and password_input != password:
            st.error("Nome de usuário ou senha incorretos.")
            st.info("Se você esqueceu sua senha, entre em contato com o administrador.")

            st.markdown("""
            <style>
                .container {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                padding: 2rem;
                }

                .form-group {
                width: 100%;
                margin-bottom: 1rem;
                }

                .form-control {
                width: 100%;
                padding: 0.75rem;
                font-size: 1rem;
                border-radius: 0.25rem;
                border: 1px solid #ced4da;
                }

                .form-control:focus {
                outline: none;
                box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
                border-color: #80bdff;
                }

                .btn {
                display: inline-block;
                font-weight: 400;
                color: #212529;
                text-align: center;
                vertical-align: middle;
                user-select: none;
                background-color: transparent;
                border: 1px solid transparent;
                padding: 0.375rem 0.75rem;
                font-size: 1rem;
                line-height: 1.5;
                border-radius: 0.25rem;
                transition: color 0.15s ease-in-out,
                            background-color 0.15s ease-in-out,
                            border-color 0.15s ease-in-out,
                            box-shadow 0.15s ease-in-out;
                }

                .btn-primary {
                    color: #fff;
                    background-color: #007bff;
                    border-color: #007bff;
                }

                .btn-primary:hover {
                    color: #fff;
                    background-color: #0069d9;
                    border-color: #0062cc;
                }

                .btn-primary:focus {
                    color: #fff;
                    background-color: #0069d9;
                    border-color: #0062cc;
                    box-shadow: 0 0 0 0.2rem rgba(38, 143, 255, 0.5);
                }
            </style>
            """, unsafe_allow_html=True)

            st.header("Contact")

            contact_form = """
            <div class="container">
                <form id="contact-form" action="https://formsubmit.co/{}" method="POST">
                <div class="form-group">
                    <input class="form-control" type="text" name="name" placeholder="Your name" required>
                </div>
                <div class="form-group">
                    <input class="form-control" type="email" name="email" placeholder="Your email" required>
                </div>
                <div class="form-group">
                    <textarea class="form-control" name="message" placeholder="Your message here"></textarea>
                </div>
                <div class="form-group">
                    <button class="btn btn-primary" type="submit" onclick="validateForm(event)">Send</button>
                </div>
                </form>
            </div>
            """.format("estevamsouzalaureth@gmail.com")  # Substitua o endereço de e-mail aqui

            javascript_code = """
            <script>
                function validateForm(event) {
                var form = document.getElementById('contact-form');
                var nameInput = form.elements['name'];
                var emailInput = form.elements['email'];
                var messageInput = form.elements['message'];

                if (nameInput.value.trim() === '' || emailInput.value.trim() === '' || messageInput.value.trim() === '') {
                    event.preventDefault();
                    alert('Por favor, preencha todos os campos do formulário.');
                } else {
                    animateSubmitButton();
                }
                }

                function animateSubmitButton() {
                var submitButton = document.querySelector('.btn-primary');
                submitButton.innerHTML = 'Sending...';
                submitButton.classList.add('animate__animated', 'animate__fadeOut');

                setTimeout(function() {
                    submitButton.innerHTML = 'Sent!';
                    submitButton.classList.remove('animate__fadeOut');
                    submitButton.classList.add('animate__zoomIn');
                }, 2000);
                }
            </script>
            """

            st.markdown(contact_form + javascript_code, unsafe_allow_html=True)


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
                            "📊 Gráfico",
                            "Calcular Lucro",
                            "Consultar",
                            "Inserir",
                            "Atualizar",
                            "Deletar",
                            "Estatísticas de vendas",
                            "Relatórios financeiros",
                            "Análise de tendências",
                            "Histórico de vendas",
                            "Gerenciamento de estoque",
                            "Tipo de marmita mais vendido",
                            "Tipo de marmita menos vendido".capitalize(),
                            "Tipo de marmita mais lucrativo",
                            "Tipo de marmita menos lucrativo",
                            "Tipo de marita que saiu",
                            "Pedidos por Semana",
                            "Análise de Rentabilidade",
                            "Developers",
                            "About",
                            "Suporte ao cliente",
                            "Documentação",
                            "Ajuda e suporte",
                            "Sair"
                            ]
                        )
            
            # Add restaurant information to the sidebar
            st.sidebar.title("Informações do Restaurante")
            st.sidebar.markdown("Este é um restaurante que oferece comida em marmitex.")
            st.sidebar.markdown("Faça uma análise de rentabilidade com base nos dados fornecidos.")

            # Executa a função correspondente com base na opção selecionada
            if selecionar == "🏠 Home":
                homePage()

            if selecionar == "📊 Gráfico":
                csv_file = 'app/data/pedidos.csv'  # Caminho relativo para o arquivo .csv
                # Exemplo de uso
                chart_type = st.selectbox('Escolha o tipo de gráfico', ['bolha', 'barra', 'linha', 'pizza', 'histograma', 'dispersao', 'matriz', 'funil', 'radar', 'area', 'torta', 'dendrograma', 'correlacao', 'waffle', 'calendario', 'radial'])
                generate_chart(csv_file, chart_type)

            if selecionar == "Pedidos por Semana":
                csv_file = 'app/data/pedidos.csv'
                # Perform analysis on the weekly orders
                analise_pedidos_semana(csv_file)

            if selecionar == "Tipo de marmita mais vendido":
                csv_file = 'app/data/pedidos.csv'
                __main__Marmitas__(csv_file)

            if selecionar == "Consultar":
                __consult__()

            if selecionar == "Atualizar":
                pedido = 'app/data/pedidos.csv'
                lucro = 'app/data/lucro.csv'
                __atualizar__(lucro, pedido)

            if selecionar == "Deletar":
                lucro = 'app/data/lucro.csv'
                pedido = 'app/data/pedidos.csv'
                __delete__(lucro, pedido)

            if selecionar == "Tipo de marita que saiu":
                csv_file = 'app/data/pedidos.csv'
                st.title("Análise de Marmitas")

                # Selecionar arquivo CSV
                # csv_file = st.file_uploader("Carregar arquivo CSV", type=['csv'])

                if csv_file is not None:
                    # Chamar função para listar tipos de marmita e gerar gráfico
                    listar_tipos_marmita(csv_file)

            if selecionar == "Developers":
                developers()

            if selecionar == "Sair":
                logout()

            if selecionar == "Análise de Rentabilidade":
                csv_file = 'app/data/pedidos.csv'
                # Check if a file is uploaded
                if csv_file is not None:
                    # Perform analysis and display the results
                    analise(csv_file)
            if selecionar == "Calcular Lucro":
                csv_file = 'app/data/pedidos.csv'
                # Check if a file is uploaded
                if csv_file is not None:
                    # Perform analysis and display the results
                    calcular_lucro(csv_file, 'app/data/lucro.csv')

            st.sidebar.image(top_image,use_column_width='auto')
            st.sidebar.image(bottom_image,use_column_width='auto')

        else:
            # Display login message if the user is not authenticated
            st.info("Please log in to access the system.")


if __name__ == "__main__":
    main()