import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from io import BytesIO
import matplotlib.dates as mdates

# Gerar dados fictícios de estoque
def generate_stock_data():
    np.random.seed(0)
    products = ['Produto A', 'Produto B', 'Produto C']
    data = []

    for product in products:
        start_date = datetime(2024, 1, 1)
        for i in range(12):  # 12 meses de dados de estoque
            date = start_date + timedelta(days=i * 30)
            stock_levels = np.random.randint(0, 1000, size=30)  # Níveis de estoque para 30 dias
            stock_dates = [date - timedelta(days=x) for x in range(30)]
            data.append({
                'Produto': product,
                'Data': date,
                'Estoque Datas': stock_dates,
                'Estoque Níveis': stock_levels.tolist()
            })

    df = pd.DataFrame(data)
    return df

# Gerar dados fictícios para estoque
df_stock = generate_stock_data()

# Página de Estoque
if st.session_state.get('authentication_status'):
    st.title("Controle de Estoque dos Produtos")

    # Dropdown para selecionar o produto
    selected_product = st.selectbox("Selecione o produto:", df_stock['Produto'].unique())

    # Filtrar os dados com base no produto selecionado
    filtered_df_stock = df_stock[df_stock['Produto'] == selected_product]

    # Preparar os dados para o gráfico
    all_dates = []
    all_levels = []
    for idx, row in filtered_df_stock.iterrows():
        all_dates.extend(row['Estoque Datas'])
        all_levels.extend(row['Estoque Níveis'])

    # Ordenar os dados
    sorted_indices = np.argsort(all_dates)
    all_dates = [all_dates[i] for i in sorted_indices]
    all_levels = [all_levels[i] for i in sorted_indices]

    # Mostrar gráfico para o estoque
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(all_dates, all_levels, marker='', linestyle='-', color='blue', label='Nível de Estoque', alpha=0.7)
    ax.set_title(f'Tendência de Estoque ao Longo do Tempo para {selected_product}')
    ax.set_xlabel('Data')
    ax.set_ylabel('Nível de Estoque')
    plt.xticks(rotation=45)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.legend()
    st.pyplot(fig)

    # Mostrar tabela de estoque para detalhes
    st.write("**Detalhes do Estoque:**")
    
    # Criação de um DataFrame para exibir os detalhes
    df_details = pd.DataFrame({
        'Data': all_dates,
        'Nível de Estoque': all_levels
    })
    
    st.dataframe(df_details)

    # Função para exportar para Excel
    def to_excel(df):
        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Estoque')
            worksheet = writer.sheets['Estoque']
            format1 = writer.book.add_format({'num_format': '0'})
            worksheet.set_column('A:A', 20, format1)
            worksheet.set_column('B:B', 20)
        processed_data = output.getvalue()
        return processed_data

    # Exportar para Excel
    st.download_button(
        label='📥 Exportar para Excel',
        data=to_excel(df_details),
        file_name=f'estoque_{selected_product}.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
else:
    st.warning('Você precisa estar autenticado para acessar esta página.')
