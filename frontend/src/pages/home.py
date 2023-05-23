import streamlit as st
from streamlit_extras.buy_me_a_coffee import button
from streamlit_extras.mention import mention
from streamlit_extras.let_it_rain import rain

def homePage():

    rain(
        emoji="🎈",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )

    st.title("Bem-vindo ao Meu Web App")
    st.write("Esta é a página inicial do nosso web app. Aqui você encontrará informações e recursos para ajudá-lo a navegar pelo aplicativo.")
    
    st.header("Recursos disponíveis")
    st.write("Aqui estão alguns recursos disponíveis no nosso web app:")
    
    st.subheader("1. Visualizar Relatórios de Vendas")
    st.write("Acesse a página de relatórios de vendas para analisar o desempenho de vendas e obter insights sobre o seu negócio.")
    
    st.subheader("2. Gerenciar Produtos")
    st.write("Acesse a página de gerenciamento de produtos para adicionar, editar ou remover produtos do seu catálogo.")
    
    st.subheader("3. Configurações")
    st.write("Acesse a página de configurações para personalizar as preferências e configurações do seu web app.")
    
    st.header("Como começar")
    st.write("Para começar a utilizar o web app, siga estas etapas:")
    
    st.subheader("1. Faça login")
    st.write("Faça login na sua conta para acessar todos os recursos do web app.")
    
    st.subheader("2. Explore as funcionalidades")
    st.write("Explore as diferentes páginas e funcionalidades disponíveis no menu para aproveitar ao máximo o web app.")
    
    st.subheader("3. Entre em contato")
    st.write("Se tiver alguma dúvida ou precisar de suporte, entre em contato conosco através do formulário de contato ou pelos nossos canais de suporte.")

    st.subheader("4. Projeto Nosso")
    st.write("Este projeto foi desenvolvido por Eduaro, estudante de sistema de Informação na Estácio.")

    mention(
        label="An awesome Streamlit App",
        icon="streamlit",  # Some icons are available... like Streamlit!
        url="https://extras.streamlitapp.com",
    )

    mention(
        label="example-app-cv-model",
        icon="github",  # GitHub is also featured!
        url="https://github.com/streamlit/example-app-cv-model",
    )


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
    
    button(username="fake-username", floating=False, width=221, text= "Buy me a coffee",bg_color= "#FFDD00")

if __name__ == "__main__":
    homePage()
