import streamlit as st

# Define o título da página
st.title("Interface no Ambiente Global")

# Cria um campo de entrada de texto
# A variável 'nome_usuario' captura o que for digitado instantaneamente
nome_usuario = st.text_input("Digite seu nome para o sistema:")
col1, col2 = st.columns(2)

# Cria um botão de ação
# O código dentro do 'if' só é executado quando o botão é clicado
if st.button("Processar"):
    if nome_usuario:
        st.success(f"Usuário {nome_usuario} registrado com sucesso!")
        st.write("O código está rodando no Python Global.")
    else:
        st.warning("Por favor, digite um nome antes de processar.")
        
with st.sidebar:
    st.image(image="https://upload.wikimedia.org/wikipedia/commons/9/90/IFood_logo.svg", width=200)
    if st.button("Ver Sacola", icon="🛒", type="primary", use_container_width=True):
        st.write("Sacola aberta!")