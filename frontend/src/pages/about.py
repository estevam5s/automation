import streamlit as st
from abc import ABC, abstractmethod


# Interface para o serviço de informações do sistema
class SystemInfoService(ABC):
    @abstractmethod
    def get_system_info(self) -> dict:
        pass


# Implementação concreta do serviço de informações do sistema
class SystemInfoServiceImpl(SystemInfoService):
    def get_system_info(self) -> dict:
        system_info = {
            "name": "Sistema de Gestão Empresarial",
            "version": "1.0.0",
            "description": "Um sistema abrangente para gerenciar todos os aspectos do seu negócio.",
            "features": [
                "Gestão de pedidos",
                "Controle de estoque",
                "Relatórios financeiros",
                "Suporte ao cliente",
                "E muito mais..."
            ],
            "team": [
                "Desenvolvedor 1",
                "Desenvolvedor 2",
                "Desenvolvedor 3"
            ]
        }

        return system_info


# Interface para a interface do usuário
class UserInterface(ABC):
    @abstractmethod
    def display_system_info(self):
        pass


# Implementação concreta da interface do usuário utilizando Streamlit
class StreamlitUserInterface(UserInterface):
    def __init__(self, system_info_service):
        self.system_info_service = system_info_service

    def display_system_info(self):
        system_info = self.system_info_service.get_system_info()

        st.title("Sobre o Sistema")
        st.markdown(f"**Nome:** {system_info['name']}")
        st.markdown(f"**Versão:** {system_info['version']}")
        st.markdown(f"**Descrição:** {system_info['description']}")

        st.subheader("Recursos Principais:")
        for feature in system_info['features']:
            st.markdown(f"- {feature}")

        st.subheader("Equipe de Desenvolvimento:")
        for team_member in system_info['team']:
            st.markdown(f"- {team_member}")


# Configuração da injeção de dependência
def configure_dependency_injection():
    system_info_service = SystemInfoServiceImpl()
    user_interface = StreamlitUserInterface(system_info_service)

    return user_interface


def about__():
    user_interface = configure_dependency_injection()
    user_interface.display_system_info()