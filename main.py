import streamlit as st

# Título da página
st.title("Meu Frontend com Streamlit")

# Subtítulo
st.subheader("Bem-vindo ao meu app!")

# Texto
st.write("Este é um exemplo básico de como criar um frontend usando Streamlit.")

# Entrada de texto
nome = st.text_input("Digite seu nome:")

# Botão
if st.button("Enviar"):
    st.success(f"Olá, {nome}! Bem-vindo ao Streamlit!")
