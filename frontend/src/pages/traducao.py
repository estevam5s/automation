import streamlit as st
from googletrans import Translator

def translate_page():
    # Selecionar idioma para tradução
    languages = {
        'en': 'English',
        'es': 'Spanish',
        'fr': 'French',
        # Adicione mais idiomas se necessário
    }
    selected_language = st.selectbox('Selecione o idioma', list(languages.keys()))

    # Criar objeto de tradução
    translator = Translator()

    # Traduzir página inteira
    st.title(translator.translate("Bem-vindo ao meu aplicativo", dest=selected_language).text)
    st.markdown(translator.translate("Aqui está o conteúdo traduzido do meu aplicativo.", dest=selected_language).text)

    user_input = st.text_input(translator.translate("Digite algo", dest=selected_language).text)

    # Exibir mensagem de feedback traduzida
    st.success(translator.translate("Operação concluída com sucesso!", dest=selected_language).text)
    st.error(translator.translate("Ocorreu um erro durante a execução.", dest=selected_language).text)
