import pandas as pd
from deta import Deta
import streamlit as st
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff

# Load environment variables
DETA_KEY = "e0zg3sgc85x_rLjU5Zy93MAHEY8UaoCnMGDJSNZiiHNR"

# Initialize Deta
deta = Deta(DETA_KEY)

lucro_db = deta.Base("analiseLucro")
pedidos_db = deta.Base("pedidos")


def generate_chart(db, chart_type):
    # Consultar todos os registros no banco de dados
    registros = db.fetch().items

    # Criar um DataFrame com os dados
    data = {
        "DATA": [registro["DATA"] for registro in registros]
    }
    df = pd.DataFrame(data)

    # Converter a coluna 'DATA' para o tipo datetime
    df['DATA'] = pd.to_datetime(df['DATA'])

    # Agrupar os pedidos por data e contar o número de pedidos
    orders = df.groupby('DATA').size().reset_index(name='QUANTIDADE')

    if chart_type == 'bolha':
        # Gerar um gráfico de bolha usando o Plotly Express
        fig = px.scatter(
            orders,
            x='DATA',
            y='QUANTIDADE',
            size='QUANTIDADE',
            color='QUANTIDADE',
            hover_name='DATA',
            log_x=True,
            size_max=60
        )

        # Personalizar o layout do gráfico
        fig.update_layout(
            title='Pedidos por Data (Gráfico de Bolha)',
            xaxis_title='Data',
            yaxis_title='Quantidade de Pedidos',
            showlegend=False
        )

        # Exibir o gráfico no Streamlit
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == 'bolha_modificado':
        # Consultar todos os registros no banco de dados
        registros = db.fetch().items

        # Criar um DataFrame com os dados
        data = {
            "ID": [registro["ID"] for registro in registros],
            "DATA": [registro["DATA"] for registro in registros],
            "ITEM": [registro["ITEM"] for registro in registros]
        }
        df = pd.DataFrame(data)

        # Definir um tamanho fixo para os pontos
        size = 10

        fig = px.scatter(
            df,
            x="DATA",
            y="ITEM",
            size=[size] * len(df),  # Usar o tamanho fixo para todos os pontos
            color="ID",
            hover_name="ID",
            log_x=True,
            size_max=60,
        )

        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
            # Use the Streamlit theme.
            # This is the default. So you can also omit the theme argument.
            st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        with tab2:
            # Use the native Plotly theme.
            st.plotly_chart(fig, theme=None, use_container_width=True)


    elif chart_type == 'dist':
        # Gerar um gráfico de distribuição usando o Plotly Figure Factory
        x = np.random.randn(200)

        # Create distplot
        fig = ff.create_distplot([x], ['Group 1'], show_hist=False)

        # Personalizar o layout do gráfico
        fig.update_layout(title='Distribuição de Dados',
                          xaxis_title='Valores',
                          yaxis_title='Densidade',
                          showlegend=False)

        # Exibir o gráfico no Streamlit
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == 'area':
        # Gerar um gráfico de área usando o Streamlit
        st.area_chart(orders.set_index('DATA'))
        
    elif chart_type == 'pizza':
        # Gerar um gráfico de pizza usando o Plotly Express
        fig = px.pie(orders, values='QUANTIDADE', names='DATA')

        # Personalizar o layout do gráfico
        fig.update_layout(title='Pedidos por Data (Gráfico de Pizza)')

        # Exibir o gráfico no Streamlit
        st.plotly_chart(fig)
    elif chart_type == 'normal':
        # Gerar um gráfico normal usando o Plotly Express
        fig = px.line(orders, x='DATA', y='QUANTIDADE')

        # Personalizar o layout do gráfico
        fig.update_layout(title='Pedidos por Data (Gráfico Normal)',
                          xaxis_title='Data',
                          yaxis_title='Quantidade de Pedidos')

        # Exibir o gráfico no Streamlit
        st.plotly_chart(fig)
    elif chart_type == 'barra':
        # Gerar um gráfico de barras usando o Plotly Express
        fig = px.bar(orders, x='DATA', y='QUANTIDADE', color='DATA')

        # Personalizar o layout do gráfico
        fig.update_layout(title='Pedidos por Data (Gráfico de Barras)',
                          xaxis_title='Data',
                          yaxis_title='Quantidade de Pedidos',
                          showlegend=False)

        # Exibir o gráfico no Streamlit
        st.plotly_chart(fig)
    
    elif chart_type == 'scatter':
        # Gerar um gráfico de dispersão usando o Plotly Express
        fig = px.scatter(orders, x='DATA', y='QUANTIDADE', trendline='lowess')

        # Personalizar o layout do gráfico
        fig.update_layout(title='Pedidos por Data (Gráfico de Dispersão)',
                          xaxis_title='Data',
                          yaxis_title='Quantidade de Pedidos')

        # Exibir o gráfico no Streamlit
        st.plotly_chart(fig)

    elif chart_type == 'histograma':
        # Histograma
        fig = px.histogram(orders, x='QUANTIDADE', nbins=10)

        fig.update_layout(title='Histograma de Quantidade de Pedidos',
                          xaxis_title='Quantidade de Pedidos',
                          yaxis_title='Frequência')

        st.plotly_chart(fig)
    elif chart_type == 'boxplot':
        # Boxplot
        fig = px.box(orders, y='QUANTIDADE')

        fig.update_layout(title='Boxplot de Quantidade de Pedidos',
                          yaxis_title='Quantidade de Pedidos')
        
    elif chart_type == 'scatter3d':
        # Gráfico de dispersão 3D
        fig = px.scatter_3d(orders, x='DATA', y='QUANTIDADE', z='QUANTIDADE')

        fig.update_layout(title='Pedidos por Data (Gráfico de Dispersão 3D)',
                          scene=dict(xaxis_title='Data',
                                     yaxis_title='Quantidade de Pedidos',
                                     zaxis_title='Quantidade de Pedidos'))

        st.plotly_chart(fig)
    elif chart_type == 'barra3d':
        # Gráfico de barras 3D
        fig = px.bar_3d(orders, x='DATA', y='QUANTIDADE', z='QUANTIDADE')

        fig.update_layout(title='Pedidos por Data (Gráfico de Barras 3D)',
                          scene=dict(xaxis_title='Data',
                                     yaxis_title='Quantidade de Pedidos',
                                     zaxis_title='Quantidade de Pedidos'))

        st.plotly_chart(fig)
    elif chart_type == 'treemap':
        # Treemap
        fig = px.treemap(orders, path=['DATA'], values='QUANTIDADE')

        fig.update_layout(title='Pedidos por Data (Treemap)')

        st.plotly_chart(fig)
    elif chart_type == 'linha3d':
        # Gráfico de linha 3D
        fig = px.line_3d(orders, x='DATA', y='QUANTIDADE', z='QUANTIDADE')

        fig.update_layout(title='Pedidos por Data (Gráfico de Linha 3D)',
                          scene=dict(xaxis_title='Data',
                                     yaxis_title='Quantidade de Pedidos',
                                     zaxis_title='Quantidade de Pedidos'))

        st.plotly_chart(fig)
    elif chart_type == 'scatterpolar':
        # Gráfico de dispersão polar
        fig = px.scatter_polar(orders, r='QUANTIDADE', theta='DATA', size='QUANTIDADE', color='QUANTIDADE')

        fig.update_layout(title='Pedidos por Data (Gráfico de Dispersão Polar)')

        st.plotly_chart(fig)
    elif chart_type == 'barraempilhada':
        # Gráfico de barras empilhadas
        fig = px.bar(orders, x='DATA', y='QUANTIDADE', color='QUANTIDADE', barmode='stack')

        fig.update_layout(title='Pedidos por Data (Gráfico de Barras Empilhadas)',
                          xaxis_title='Data',
                          yaxis_title='Quantidade de Pedidos')

        st.plotly_chart(fig)
    elif chart_type == 'mapa':
        # Mapa
        fig = px.scatter_geo(orders, lat='LATITUDE', lon='LONGITUDE')

        fig.update_layout(title='Mapa de Pedidos',
                          geo=dict(showland=True,
                                   showlakes=True,
                                   showocean=True,
                                   showrivers=True))

        st.plotly_chart(fig)
    elif chart_type == 'scattermatrix':
        # Matriz de dispersão
        fig = px.scatter_matrix(orders, dimensions=['DATA', 'QUANTIDADE'])

        fig.update_layout(title='Matriz de Dispersão de Pedidos')

        st.plotly_chart(fig)
    elif chart_type == 'paralelo':
        # Gráfico de linhas paralelas
        fig = px.parallel_categories(orders, dimensions=['DATA', 'QUANTIDADE'])

        fig.update_layout(title='Gráfico de Linhas Paralelas de Pedidos')

        st.plotly_chart(fig)
    elif chart_type == 'funil':
        # Gráfico de funil
        fig = px.funnel(orders, x='QUANTIDADE', y='DATA')

        fig.update_layout(title='Gráfico de Funil de Pedidos')

        st.plotly_chart(fig)
    elif chart_type == 'radar':
        # Gráfico de radar
        fig = px.line_polar(orders, r='QUANTIDADE', theta='DATA')

        fig.update_layout(title='Gráfico de Radar de Pedidos')

        st.plotly_chart(fig)
        
    else:
        st.error("Tipo de gráfico não suportado.")