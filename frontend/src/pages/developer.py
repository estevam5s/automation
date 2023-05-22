import logging
import streamlit as st

def developers():
  st.title("Análise de sentimento de Vendas de Marmitex")
  st.sidebar.title("Análise de sentimento de Vendas de Marmitex")

  st.markdown("Este aplicativo é um painel Streamlit para analisar os dados de um Restaurante 🐦🐦")
  st.sidebar.markdown("Este aplicativo é um painel Streamlit para analisar os dados de um Restaurante 🐦🐦")

  st.title('Streamlit Tutorial')
  st.markdown('')
  st.markdown('''
  - developped by [`@eduardo`](https://github.com/eduardo/)
  - [`Github 💻 streamlit-tutorial`](https://github.com/estevam5s/big-data-drisssen)
  ''')
  st.info('Streamlit é uma estrutura python de código aberto para a criação de aplicativos web para Machine Learning e Data Science. Podemos desenvolver instantaneamente aplicativos da web e implantá-los facilmente usando o Streamlit. O Streamlit permite que você escreva um aplicativo da mesma forma que escreve um código python. O Streamlit facilita o trabalho no loop interativo de codificação e visualização de resultados no aplicativo Web.')

  st.header('Streamlit Gallery 🖼️')

  with st.expander('Example 1'):
      st.markdown('''
  ## 💸 Clonando o repositório ✨

  # clone other repositories
  git clone https://github.com/estevam5s/big-data-drisssen.git

      ''')

  with st.expander('Example 2'):
      st.markdown('''
  ## 💸 Instalação de bibliotecas ✨

    ```
  pip install -r requirements.txt
  ```
      ''')

  with st.expander('Example 3'):
      st.markdown('''
  ## 💸 Executando o projeto ✨

  ```
  streamlit run app.py --server.address 0.0.0.0 --server.port 8080
  ```
      ''')

  # bibliotecas do projeto

  with st.expander('Example 4'):
      st.markdown('''
  ## 💸 Bibliotecas do projeto ✨

    ```
    anyio==3.6.2
    deta==1.1.0
    fastapi==0.95.2
    idna==3.4
    numpy==1.24.3
    packaging==23.1
    pandas==2.0.1
    patsy==0.5.3
    pydantic==1.10.7
    python-dateutil==2.8.2
    pytz==2023.3
    scipy==1.10.1
    six==1.16.0
    sniffio==1.3.0
    starlette==0.27.0
    statsmodels==0.14.0
    typing_extensions==4.5.0
    tzdata==2023.3
    tweepy==3.10.0
    textblob==0.15.3
    wordcloud==1.8.1
    regex>=2021.8.3
    streamlit==1.22.0
    matplotlib==3.3.4
    googlenews==1.5.8
    ta==0.7.0
    plotly==4.14.3
    nltk==3.8.1
    requests
    convertdate
    beautifulsoup4
    ```
      ''')

  st.markdown('---')
  st.header('Streamlit API reference')
  st.markdown('')
  st.markdown('''
  **📒 Useful resource**
  - [`streamlit.io`](https://docs.streamlit.io/)
  - [`awesome-streamlit`](https://github.com/MarcSkovMadsen/awesome-streamlit)
  - [`streamlit gallery`](https://streamlit.io/gallery)
  - [`Python Streamlit 사용법 - 프로토타입 만들기`](https://zzsza.github.io/mlops/2021/02/07/python-streamlit-dashboard/)

  ''')

  st.code('import streamlit as st')