import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def analise_pedidos_semana(csv_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Convert the 'DATA' column to datetime
    df['DATA'] = pd.to_datetime(df['DATA'])

    # Group the data by week and calculate the total number of orders per week
    df['WEEK'] = df['DATA'].dt.isocalendar().week
    df_weekly = df.groupby('WEEK')['ID'].count().reset_index()

    # Convert the 'WEEK' and 'ID' columns to numpy arrays
    weeks = df_weekly['WEEK'].to_numpy()
    orders = df_weekly['ID'].to_numpy()

    # Plot the weekly orders
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(weeks, orders, marker='o')
    ax.set_xlabel('Week')
    ax.set_ylabel('Number of Orders')
    ax.set_title('Weekly Orders')
    ax.grid(True)
    st.pyplot(fig)

    # Generate insights about the data
    total_orders = df['ID'].nunique()
    total_weeks = df_weekly['WEEK'].nunique()
    avg_orders_per_week = total_orders / total_weeks

    st.subheader('Insights')
    st.write(f'Total Orders: {total_orders}')
    st.write(f'Total Weeks: {total_weeks}')
    st.write(f'Average Orders per Week: {avg_orders_per_week:.2f}')
