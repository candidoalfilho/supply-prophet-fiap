import streamlit as st

st.title("Realizar previsão")
st.write("Entenda a futura demanda de seus ativos por meio de métodos estatísticos avançados")

st.warning("O SupplyProphet ainda está em fase de demo e o fine-tuning de seus resultados está sendo incrementado.")

st.file_uploader(label="Escolha um arquivo")

st.write("Caso ainda não tenha submetido nenhum arquivo, faça download do Template padrão do SupplyProphet")
st.download_button(label="Template padrão", data="teset.xlsx", )

st.text_input("Nome da previsão:")
st.text_input("Nome do produto:")

opcoes_modelos = ["ARIMA", "SARIMA", "ARMAX", "PROPHET"]
st.multiselect(label="Selecione os métodos de previsão de demanda:", placeholder="Selecionar método", options=opcoes_modelos)

opcoes_granularidade = ["DIA", "HORA", "MINUTO"]
st.selectbox(label="Selecione a granularidade:", placeholder="Selecionar intervalo", options=opcoes_granularidade)

st.button(label="Realizar previsão")
