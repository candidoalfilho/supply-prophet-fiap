import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Gerar dados fictícios de previsões
def generate_forecast_data():
    np.random.seed(0)
    products = ['Produto A', 'Produto B', 'Produto C']
    models = ['ARIMA', 'SARIMA', 'ARMAX', 'PROPHET']
    data = []

    for product in products:
        start_date = datetime(2024, 1, 1)
        for i in range(12):  # 12 meses de previsões
            date = start_date + timedelta(days=i * 30)
            train_dates = [date - timedelta(days=x) for x in range(7)]  # Últimos 7 dias para treino
            test_dates = [date + timedelta(days=x) for x in range(7)]  # Próximos 7 dias para teste
            train_outputs = np.random.randint(50, 200, size=len(train_dates))
            test_outputs = np.random.randint(50, 200, size=len(test_dates))
            selected_models = np.random.choice(models, size=2, replace=False)
            data.append({
                'Produto': product,
                'Data': date,
                'Treino Datas': train_dates,
                'Treino Saídas': train_outputs.tolist(),
                'Teste Datas': test_dates,
                'Teste Saídas': test_outputs.tolist(),
                'Modelos': ', '.join(selected_models)
            })

    df = pd.DataFrame(data)
    return df

# Gerar dados fictícios para histórico
df_history = generate_forecast_data()

# Página de Histórico
st.title("Histórico de Previsões")

# Dropdown para selecionar o produto
selected_product = st.selectbox("Selecione o produto:", df_history['Produto'].unique())

# Filtrar os dados com base no produto selecionado
filtered_df = df_history[df_history['Produto'] == selected_product]

# Identificar a previsão mais recente
latest_forecast_date = filtered_df['Data'].max()
latest_forecast = filtered_df[filtered_df['Data'] == latest_forecast_date]

st.write(f"Histórico de previsões para o {selected_product}:")

# Inicializar o estado da sessão para a página atual
if 'pagina_atual' not in st.session_state:
    st.session_state['pagina_atual'] = 0

# Número de previsões por página
previsoes_por_pagina = 5
total_previsoes = len(filtered_df)
pagina_atual = st.session_state['pagina_atual']

# Mostrar a lista de previsões com controle de página
start_index = pagina_atual * previsoes_por_pagina
end_index = min(start_index + previsoes_por_pagina, total_previsoes)
paginated_df = filtered_df.iloc[start_index:end_index]

for idx, row in paginated_df.iterrows():
    with st.expander(f"Previsão em {row['Data'].strftime('%d/%m/%Y')}"):
        st.write(f"**Treino Datas:**")
        st.write(', '.join(date.strftime('%d/%m/%Y') for date in row['Treino Datas']))
        st.write(f"**Treino Saídas:** {', '.join(map(str, row['Treino Saídas']))}")
        st.write(f"**Teste Datas:**")
        st.write(', '.join(date.strftime('%d/%m/%Y') for date in row['Teste Datas']))
        st.write(f"**Teste Saídas:** {', '.join(map(str, row['Teste Saídas']))}")
        st.write(f"**Modelos Utilizados:** {row['Modelos']}")
        
        # Gráfico para a previsão
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(row['Treino Datas'], row['Treino Saídas'], marker='o', linestyle='-', color='blue', label='Treino')
        ax.plot(row['Teste Datas'], row['Teste Saídas'], marker='o', linestyle='--', color='red', label='Teste')
        ax.set_title(f'Previsões em {row["Data"].strftime("%d/%m/%Y")}')
        ax.set_xlabel('Data')
        ax.set_ylabel('Valor')
        ax.legend()
        plt.xticks(rotation=45)
        st.pyplot(fig)

# Controle de navegação de página
col1, col2 = st.columns(2)

if pagina_atual > 0:
    with col1:
        if st.button('Anterior'):
            st.session_state['pagina_atual'] -= 1

if end_index < total_previsoes:
    with col2:
        if st.button('Próximo'):
            st.session_state['pagina_atual'] += 1

# Destacar a previsão mais recente
st.subheader("Previsão Mais Recente")
st.write(f"A previsão mais recente foi realizada em {latest_forecast_date.strftime('%d/%m/%Y')}.")
latest_forecast["Treino"] = [f"{a[-1]} a {a[0]}" for a in latest_forecast["Treino Datas"]]
latest_forecast["Teste"] = [f"{a[-1]} a {a[0]}" for a in latest_forecast["Teste Datas"]]
st.dataframe(latest_forecast[['Data', 'Treino', 'Teste']])

# Adicionar gráfico para visualizar o histórico
fig, ax = plt.subplots(figsize=(10, 5))

# Preparar dados para o gráfico
for i in range(len(filtered_df)):
    row = filtered_df.iloc[i]
    ax.plot(row['Teste Datas'], row['Teste Saídas'], marker='o', linestyle='-', label=f'{row["Data"].strftime("%d/%m/%Y")} ({row["Modelos"]})')

ax.set_title(f'Previsões ao longo do tempo para {selected_product}')
ax.set_xlabel('Data')
ax.set_ylabel('Valor')
plt.xticks(rotation=45)
ax.legend(loc='upper left')
st.pyplot(fig)
