import streamlit as st
from abc import ABC, abstractmethod


# Interface para o serviço de Ajuda e Suporte
class HelpSupportService(ABC):
    @abstractmethod
    def get_help_topics(self) -> list:
        pass

    @abstractmethod
    def get_article(self, article_id: str) -> str:
        pass


# Implementação concreta do serviço de Ajuda e Suporte
class HelpSupportServiceImpl(HelpSupportService):
    def __init__(self, article_repository):
        self.article_repository = article_repository

    def get_help_topics(self) -> list:
        # Lógica para obter os tópicos de ajuda disponíveis
        help_topics = self.article_repository.get_help_topics()

        return help_topics

    def get_article(self, article_id: str) -> str:
        # Lógica para obter o conteúdo do artigo de ajuda
        article_content = self.article_repository.get_article(article_id)

        return article_content


# Interface para o repositório de artigos de ajuda
class ArticleRepository(ABC):
    @abstractmethod
    def get_help_topics(self) -> list:
        pass

    @abstractmethod
    def get_article(self, article_id: str) -> str:
        pass


# Implementação concreta do repositório de artigos de ajuda
class CSVArticleRepository(ArticleRepository):
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def get_help_topics(self) -> list:
        # Lógica para obter os tópicos de ajuda do arquivo CSV
        help_topics = []

        # ...

        return help_topics

    def get_article(self, article_id: str) -> str:
        # Lógica para obter o conteúdo do artigo de ajuda do arquivo CSV
        article_content = ""

        # ...

        return article_content


# Interface para a interface do usuário
class UserInterface(ABC):
    @abstractmethod
    def display_help_topics(self, help_topics: list):
        pass

    @abstractmethod
    def display_article(self, article_content: str):
        pass


# Implementação concreta da interface do usuário utilizando Streamlit
class StreamlitUserInterface(UserInterface):
    def display_help_topics(self, help_topics: list):
        st.title("Ajuda e Suporte do Sistema")
        st.markdown("Selecione um tópico de ajuda abaixo:")

        selected_topic = st.selectbox("Tópicos de Ajuda", help_topics)

        return selected_topic

    def display_article(self, article_content: str):
        st.markdown(article_content)


# Configuração da injeção de dependência
def configure_dependency_injection():
    article_repository = CSVArticleRepository("articles.csv")
    support_service = HelpSupportServiceImpl(article_repository)
    user_interface = StreamlitUserInterface()

    return support_service, user_interface


def help__():
    support_service, user_interface = configure_dependency_injection()

    # Obtém os tópicos de ajuda disponíveis
    help_topics = support_service.get_help_topics()

    # Exibe a lista de tópicos de ajuda
    selected_topic = user_interface.display_help_topics(help_topics)

    if selected_topic:
        # Obtém o conteúdo do artigo selecionado
        article_content = support_service.get_article(selected_topic)

        # Exibe o conteúdo do artigo
        user_interface.display_article(article_content)
