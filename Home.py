import streamlit as st


st.title("SupplyProphet 🎆")
st.markdown("<h5><i>A solução para a sua previsão de demanda no varejo</i></h5><br>", unsafe_allow_html=True)


st.markdown("<h3>Como funciona o SupplyProphet?</h3>", unsafe_allow_html=True)
st.write("""O SupplyProphet é uma aplicação voltada a varejistas que necessitam de informações confiáveis para a 
         previsão de demanda com modelos estatísticos avançados confiados pela indústria, como ARIMA, SARIMA, Prophet, entre outros.
         """)
# st.balloons()

# st.chat_input(placeholder="Fale aqui")
# st.chat_message(name='sei la')

opcoes_previsao = ["ARIMA", "SARIMA", "ARMAX", "PROPHET"]
st.multiselect(label="Método de previsão", placeholder="Escolha um método", options=opcoes_previsao)
st.file_uploader(label="Insira um arquivo", help="Escolha um arquivo no formato xlsx seguindo o padrão da planilha de exemplo para enviar informações.", )