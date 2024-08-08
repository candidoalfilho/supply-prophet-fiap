import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# Configuração da barra lateral
# st.sidebar.title('Navegação')

# navigation_options = ['Home', 'Sobre', 'Login']
# if st.session_state.get('authentication_status'):
#     navigation_options = ['Home', 'Estoque', 'Histórico', 'Previsão', 'Sobre', 'Logout']

# navigation = st.sidebar.radio('Ir para', navigation_options)

# Título e descrição da página inicial
st.title("SupplyProphet 🎆")
st.markdown("<h5><i>A solução definitiva para previsão de demanda no varejo</i></h5><br>", unsafe_allow_html=True)

# Seção explicativa
st.markdown("<h3>Como funciona o SupplyProphet?</h3>", unsafe_allow_html=True)
st.write("""
O SupplyProphet é uma aplicação inovadora projetada para ajudar varejistas a prever a demanda com precisão utilizando modelos estatísticos avançados. 
Escolha entre uma variedade de métodos de previsão, faça upload de seus dados e obtenha insights valiosos sobre a demanda futura de seus produtos.

### Principais Características:
- **Métodos de Previsão Avançados:** ARIMA, SARIMA, ARMAX, Prophet e mais.
- **Importação de Dados Simples:** Carregue seus arquivos e inicie a análise de forma rápida.
- **Visualizações Interativas:** Veja gráficos de tendências e previsões detalhadas.
- **Controle de Estoque Eficiente:** Acompanhe e gerencie o estoque de seus produtos com facilidade.
""")

# Exemplo de como a previsão funciona
st.markdown("<h3>Veja um exemplo de previsão</h3>", unsafe_allow_html=True)
st.write("""
Abaixo está um exemplo de como a previsão de demanda pode ser visualizada. Escolha um método de previsão e faça o upload de um arquivo para ver como o SupplyProphet pode ajudá-lo a planejar melhor seu estoque.
""")

# Exemplo de gráfico de previsão
# Gerar dados fictícios
dates = [datetime.now() - timedelta(days=i) for i in range(30)]
values = np.random.randint(50, 150, size=30)

# Plotar gráfico de exemplo
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(dates, values, marker='o', linestyle='-', color='blue')
ax.set_title('Exemplo de Previsão de Demanda')
ax.set_xlabel('Data')
ax.set_ylabel('Demanda')
plt.xticks(rotation=45)
st.pyplot(fig)

# Opções de previsão e upload de arquivo
st.markdown("<h3>Faça uma previsão agora!</h3>", unsafe_allow_html=True)
opcoes_previsao = ["ARIMA", "SARIMA", "ARMAX", "PROPHET"]
st.multiselect(label="Método de previsão", placeholder="Escolha um ou mais métodos", options=opcoes_previsao)

st.file_uploader(label="Insira um arquivo", help="Escolha um arquivo no formato xlsx seguindo o padrão da planilha de exemplo para enviar informações.")

# Mensagem de boas-vindas caso não esteja autenticado
if not st.session_state.get('authentication_status'):
    st.warning('Faça login para acessar todas as funcionalidades.')
