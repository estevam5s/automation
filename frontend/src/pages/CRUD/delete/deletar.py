import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from deta import Deta
import streamlit as st
import pandas as pd

DETA_KEY = "e0zg3sgc85x_rLjU5Zy93MAHEY8UaoCnMGDJSNZiiHNR"

# Initialize Deta
deta = Deta(DETA_KEY)

pedidos_db = deta.Base("pedidos")
lucro_db = deta.Base("analiseLucro")


# Função para exibir a tabela de pedidos
def exibir_tabela_pedidos(df):
    st.subheader('Tabela de Pedidos')
    st.dataframe(df)

# Função principal
def deletePedidos():
    # Consultar todos os registros no banco de dados
    registros = pedidos_db.fetch().items

    # Criar listas vazias para cada coluna
    ids = []
    datas = []
    itens = []
    anotacoes = []

    # Extrair os dados de cada registro e armazenar nas listas correspondentes
    for registro in registros:
        ids.append(registro["ID"])
        datas.append(registro["DATA"])
        itens.append(registro["ITEM"])
        anotacoes.append(registro["ANOTAÇÕES"])

    # Criar um DataFrame com os dados
    data = {
        "ID": ids,
        "DATA": datas,
        "ITEM": itens,
        "ANOTAÇÕES": anotacoes
    }
    df = pd.DataFrame(data)

    # Exibição inicial da tabela de pedidos
    exibir_tabela_pedidos(df)

    st.sidebar.subheader('Excluir Pedido')
    pedido_id = st.sidebar.selectbox('ID do Pedido', df['ID'].tolist())

    if st.sidebar.button('Excluir'):
        # Remover o registro correspondente ao ID selecionado
        pedidos_db.delete(pedido_id)

        # Atualizar a tabela de pedidos
        registros = pedidos_db.fetch().items
        ids = []
        datas = []
        itens = []
        anotacoes = []

        # Extrair os dados atualizados de cada registro e armazenar nas listas correspondentes
        for registro in registros:
            ids.append(registro["ID"])
            datas.append(registro["DATA"])
            itens.append(registro["ITEM"])
            anotacoes.append(registro["ANOTAÇÕES"])

        # Criar um DataFrame com os dados atualizados
        data = {
            "ID": ids,
            "DATA": datas,
            "ITEM": itens,
            "ANOTAÇÕES": anotacoes
        }
        df = pd.DataFrame(data)

        exibir_tabela_pedidos(df)
        st.sidebar.success(f'Pedido ID {pedido_id} excluído com sucesso!')



# Interface para consulta de lucros
class LucroConsultaInterface:
    def exibir_lucros(self, lucros):
        raise NotImplementedError

# Implementação da interface utilizando Streamlit
class LucroConsultaStreamlit(LucroConsultaInterface):
    def exibir_lucros(self, lucros):
        st.subheader('Tabela de Lucros')
        df_lucros = pd.DataFrame({'ID': range(1, len(lucros)+1), 'LUCRO': lucros})
        st.dataframe(df_lucros)

        st.subheader('Gráfico de Lucros')
        fig, ax = plt.subplots()
        ax.plot(np.arange(len(lucros)), lucros)
        ax.set_xlabel('Período')
        ax.set_ylabel('LUCRO')
        ax.set_title('Lucros ao longo do tempo')
        st.pyplot(fig)

# Serviço para obter, atualizar e excluir os lucros
class LucroService:
    def __init__(self, lucro_query):
        self.lucro_query = lucro_query

    def obter_lucros(self):
        return self.lucro_query.obter_lucros()

    def atualizar_lucro(self, lucro_id, novo_lucro):
        self.lucro_query.salvar_lucro(lucro_id, novo_lucro)

    def excluir_lucro(self, lucro_id):
        self.lucro_query.excluir_lucro(lucro_id)

# Query para buscar, salvar e excluir os lucros
class DetaLucroQuery:
    def __init__(self, deta, base_name):
        self.base = deta.Base(base_name)

    def obter_lucros(self):
        lucros = []
        response = self.base.fetch()
        for item in response.items:
            lucros.append(item["LUCRO"])
        return lucros

    def salvar_lucro(self, lucro_id, novo_lucro):
        lucros = self.base.fetch()
        if 0 < lucro_id <= len(lucros):
            lucro = lucros[lucro_id - 1]
            lucro["LUCRO"] = novo_lucro
            self.base.put(lucro)
        else:
            raise ValueError("ID de lucro inválido.")

    def excluir_lucro(self, lucro_id):
        lucros = self.base.fetch()
        if 0 < lucro_id <= len(lucros):
            lucro = lucros[lucro_id - 1]
            self.base.delete(lucro["key"])
        else:
            raise ValueError("ID de lucro inválido.")

# Função principal
def deleteLucro():
    # Initialize Deta
    deta = Deta(DETA_KEY)

    lucro_query = DetaLucroQuery(deta, "lucro")
    lucro_service = LucroService(lucro_query)
    lucros = lucro_service.obter_lucros()

    lucro_interface = LucroConsultaStreamlit()
    lucro_interface.exibir_lucros(lucros)

    st.sidebar.subheader('Atualizar Lucro')
    lucro_id = st.sidebar.selectbox('ID do Lucro', range(1, len(lucros)+1))
    novo_lucro = st.sidebar.number_input('Novo Lucro', value=lucros[lucro_id - 1])

    if st.sidebar.button('Atualizar'):
        lucro_service.atualizar_lucro(lucro_id, novo_lucro)
        st.sidebar.success(f'Lucro ID {lucro_id} atualizado com sucesso!')

    st.sidebar.subheader('Excluir Lucro')
    lucro_id = st.sidebar.selectbox('ID do Lucro', range(1, len(lucros) + 1), key="excluir_lucro")

    if st.sidebar.button('Excluir'):
        lucro_service.excluir_lucro(lucro_id)
        st.sidebar.success(f'Lucro ID {lucro_id} excluído com sucesso!')






def __delete__():
    st.title("Deletar Dados")
    opcoes = ["Estabelecimento", "Lucro do Estabelecimento"]
    escolha = st.radio("Selecione o tipo de dado a ser deletado:", opcoes)

    if escolha == "Estabelecimento":
        deletePedidos()
    elif escolha == "Lucro do Estabelecimento":
        deleteLucro()