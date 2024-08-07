from io import BytesIO
import streamlit as st
import pandas as pd
from datetime import datetime 
import random

def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0.00'}) 
    worksheet.set_column('A:A', None, format1)  
    writer.close()
    processed_data = output.getvalue()
    return processed_data


def write_standard_df():
    new_df = pd.DataFrame()
    new_df["Date"] = [datetime(year=2024, month=8, day=i) for i in range(1,11)]
    new_df["Target"] = [100*random.random() for i in range(10)]
    return new_df
    

st.title("Realizar previsão")

if 'authentication_status' not in st.session_state:
    st.session_state['authentication_status'] = None

if st.session_state['authentication_status']:
    st.write("Entenda a futura demanda de seus ativos por meio de métodos estatísticos avançados")

    st.warning("O SupplyProphet ainda está em fase de demo e o fine-tuning de seus resultados está sendo incrementado.")

    st.file_uploader(label="Escolha um arquivo")

    st.write("Caso ainda não tenha submetido nenhum arquivo, faça download do Template padrão do SupplyProphet")

    df_xlsx = write_standard_df()
    df_xlsx = to_excel(df_xlsx)
    st.download_button(label='📥 Template padrão',
                                data=df_xlsx ,
                                file_name= 'template_padrao.xlsx')

    st.text_input("Nome da previsão:")
    st.text_input("Nome do produto:")

    opcoes_modelos = ["ARIMA", "SARIMA", "ARMAX", "PROPHET"]
    st.multiselect(label="Selecione os métodos de previsão de demanda:", placeholder="Selecionar método", options=opcoes_modelos)

    opcoes_granularidade = ["DIA", "HORA", "MINUTO"]
    st.selectbox(label="Selecione a granularidade:", placeholder="Selecionar intervalo", options=opcoes_granularidade)

    st.slider(label="Porcentagem de teste", min_value=60, max_value=80)

    opcoes_futuro = ["1 mês", "6 meses", "1 ano"]
    st.selectbox(label="Selecione a janela de previsão:", placeholder="Selecionar janela de previsão", options=opcoes_futuro)

    st.button(label="Realizar previsão")

else:
    st.warning('Faça login para acessar essa página.')