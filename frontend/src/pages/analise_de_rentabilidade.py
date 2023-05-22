import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def analise(csv_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Extract the numeric part from 'ITEM' column
    df['ITEM'] = df['ITEM'].str.split().str[0]

    # Convert 'ITEM' column to numeric
    df['ITEM'] = pd.to_numeric(df['ITEM'])

    # Convert 'ANOTAÇÕES' column to numeric
    df['ANOTAÇÕES'] = df['ANOTAÇÕES'].str.split().str[0].astype(int)

    # Calculate the total cost for each row
    df['Custo Total'] = df['ITEM'] * df['ANOTAÇÕES']

    # Calculate the revenue for each row (assuming a fixed price of R$10 per item)
    df['Receita'] = df['ITEM'] * 10

    # Calculate the profitability for each row
    df['Rentabilidade'] = (df['Receita'] - df['Custo Total']) / df['Custo Total'] * 100

    # Create a bar chart for the profitability analysis
    fig, ax = plt.subplots()
    ax.bar(df['ID'], df['Rentabilidade'])
    ax.set_title('Análise de Rentabilidade')
    ax.set_xlabel('ID')
    ax.set_ylabel('Rentabilidade')

    # Display the chart in Streamlit
    st.pyplot(fig)
