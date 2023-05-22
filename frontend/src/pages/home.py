import streamlit as st

def homePage():
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

if __name__ == "__main__":
    homePage()
