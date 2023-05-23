import streamlit as st
from abc import ABC, abstractmethod


# Interface para o serviço de Suporte ao Cliente
class CustomerSupportService(ABC):
    @abstractmethod
    def submit_ticket(self, ticket: dict):
        pass


# Implementação concreta do serviço de Suporte ao Cliente
class CustomerSupportServiceImpl(CustomerSupportService):
    def __init__(self, notification_service):
        self.notification_service = notification_service

    def submit_ticket(self, ticket: dict):
        # Lógica para criar e salvar o ticket no banco de dados
        ticket_id = self.save_ticket(ticket)

        # Notificar o cliente sobre a submissão do ticket
        self.notify_customer(ticket_id)

    def save_ticket(self, ticket: dict) -> str:
        # Lógica para salvar o ticket no banco de dados e retornar o ID gerado
        ticket_id = "TCK12345"
        # ...

        return ticket_id

    def notify_customer(self, ticket_id: str):
        # Lógica para notificar o cliente sobre a submissão do ticket
        message = f"Seu ticket {ticket_id} foi submetido com sucesso!"
        self.notification_service.send_notification(message)


# Interface para o serviço de Notificação
class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message: str):
        pass


# Implementação concreta do serviço de Notificação utilizando Streamlit
class StreamlitNotificationService(NotificationService):
    def send_notification(self, message: str):
        st.info(message)


# Interface para a interface do usuário
class UserInterface(ABC):
    @abstractmethod
    def display_form(self):
        pass


# Implementação concreta da interface do usuário utilizando Streamlit
class StreamlitUserInterface(UserInterface):
    def __init__(self, support_service):
        self.support_service = support_service

    def display_form(self):
        st.title("Sistema de Suporte ao Cliente")
        st.markdown("Preencha o formulário abaixo para submeter um ticket de suporte:")

        name = st.text_input("Nome:")
        email = st.text_input("Email:")
        subject = st.text_input("Assunto:")
        message = st.text_area("Mensagem:")

        if st.button("Submeter"):
            ticket = {
                "name": name,
                "email": email,
                "subject": subject,
                "message": message
            }

            self.support_service.submit_ticket(ticket)
            st.success("Ticket submetido com sucesso!")


# Configuração da injeção de dependência
def configure_dependency_injection():
    notification_service = StreamlitNotificationService()
    support_service = CustomerSupportServiceImpl(notification_service)
    user_interface = StreamlitUserInterface(support_service)

    return user_interface


def suporteCliente():
    user_interface = configure_dependency_injection()
    user_interface.display_form()
