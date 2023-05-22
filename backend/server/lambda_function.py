import json
import streamlit as st


def lambda_handler(event, context):
    # Configura a resposta da função Lambda como uma resposta HTTP válida
    headers = {
        "Content-Type": "application/json",
    }

    # Obtém o corpo da solicitação HTTP
    body = event.get("body")

    # Verifica se o corpo da solicitação está vazio
    if body is None:
        response = {
            "statusCode": 400,
            "headers": headers,
            "body": json.dumps({"message": "Corpo da solicitação vazio"}),
        }
        return response

    # Converte o corpo da solicitação em um objeto JSON
    try:
        request_data = json.loads(body)
    except json.JSONDecodeError:
        response = {
            "statusCode": 400,
            "headers": headers,
            "body": json.dumps({"message": "Erro ao decodificar JSON"}),
        }
        return response

    # Executa o aplicativo Streamlit
    with st.beta_container():
        # Código do arquivo home.py aqui
        st.title("Meu Aplicativo Streamlit")
        st.write("Olá, mundo!")

    # Obtém o conteúdo do aplicativo Streamlit como uma string HTML
    html_content = st._get_session_info().main

    # Configura a resposta da função Lambda com o conteúdo HTML do Streamlit
    response = {
        "statusCode": 200,
        "headers": headers,
        "body": json.dumps({"html_content": html_content}),
    }
    return response
