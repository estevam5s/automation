import streamlit as st


def __menu__():
    # Adiciona um sidebar
    st.sidebar.title("Opções de Consulta")
    st.sidebar.selectbox("Selecione a página", [
        "🏠 Home",
        "consult",
        "consult Analysis",
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