import streamlit as st
import pandas as pd

# Função para exibir a tabela de lucros
def exibir_tabela_lucros(df):
    st.subheader('Tabela de Lucros')
    st.dataframe(df)

# Função principal
def deletePedidos(file):
    csv_file = file
    df = pd.read_csv(csv_file)

    # Exibição inicial da tabela de lucros
    exibir_tabela_lucros(df)

    st.sidebar.subheader('Excluir Lucro')
    lucro_id = st.sidebar.selectbox('ID do Lucro', df['ID'].tolist())

    if st.sidebar.button('Excluir'):
        df = df[df['ID'] != lucro_id]
        df.reset_index(drop=True, inplace=True)
        df.to_csv(csv_file, index=False)
        exibir_tabela_lucros(df)
        st.sidebar.success(f'Lucro ID {lucro_id} excluído com sucesso!')