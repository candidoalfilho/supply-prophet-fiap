import streamlit as st

# Check if the user is authenticated
if 'authentication_status' not in st.session_state or not st.session_state['authentication_status']:
    st.warning('Please log in to access this page.')

else:
    st.title("Perfil do Usuário")

    # Display user information
    st.write(f"Nome: {st.session_state.get('name', 'Não disponível')}")
    st.write(f"Usuário: {st.session_state.get('username', 'Não disponível')}")

    # Option to update profile information
    st.subheader("Atualizar Informações")

    # Example of updating user information
    with st.form(key='update_profile_form'):
        name = st.text_input("Nome", value=st.session_state.get('name', ''))
        username = st.text_input("Usuário", value=st.session_state.get('username', ''))
        password = st.text_input("Nova Senha", type='password')
        
        submit_button = st.form_submit_button(label='Atualizar')

        if submit_button:
            # Update session state with new information
            st.session_state['name'] = name
            st.session_state['username'] = username
            if password:
                # Handle password update logic here
                st.session_state['password'] = password
                st.success('Informações atualizadas com sucesso!')
            else:
                st.success('Informações atualizadas com sucesso!')

    # Option to delete account (example)
    st.subheader("Excluir Conta")
    if st.button('Excluir Conta'):
        # Handle account deletion logic here
        st.session_state['authentication_status'] = None
        st.session_state['name'] = None
        st.session_state['username'] = None
        st.success('Conta excluída com sucesso!')
        st.experimental_rerun()