import streamlit as st

# if 'authentication_status' not in st.session_state:
#     st.session_state['authentication_status'] = None
# Sidebar navigation
st.sidebar.title('Navegação')
# if 'authentication_status' not in st.session_state:
#     st.session_state['authentication_status'] = None
#     navigation = st.sidebar.radio('Ir para', ['Home', 'Sobre', 'Login'],  key='super_unauthenticated_navigation')

if st.session_state.get('authentication_status'):
    navigation = st.sidebar.radio('Ir para', ['Home','Estoque','Histórico','Previsão', 'Sobre', 'Login'], key='authenticated_navigation')
else:
    navigation = st.sidebar.radio('Ir para', ['Home', 'Sobre', 'Login'],  key='unauthenticated_navigation')
    
# if st.session_state['authentication_status']:
st.title("SupplyProphet 🎆")
st.markdown("<h5><i>A solução para a sua previsão de demanda no varejo</i></h5><br>", unsafe_allow_html=True)

st.markdown("<h3>Como funciona o SupplyProphet?</h3>", unsafe_allow_html=True)
st.write("""O SupplyProphet é uma aplicação voltada a varejistas que necessitam de informações confiáveis para a 
        previsão de demanda com modelos estatísticos avançados confiados pela indústria, como ARIMA, SARIMA, Prophet, entre outros.
        """)

opcoes_previsao = ["ARIMA", "SARIMA", "ARMAX", "PROPHET"]
st.multiselect(label="Método de previsão", placeholder="Escolha um método", options=opcoes_previsao)
st.file_uploader(label="Insira um arquivo", help="Escolha um arquivo no formato xlsx seguindo o padrão da planilha de exemplo para enviar informações.")
# else:
#     st.warning('Please log in to access this page.')
