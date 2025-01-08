import streamlit as st
import plotly.graph_objects as go
import random
import time

# Função para gerar os dados
def gerar_dados():
    aspersores_status = [random.choice([0, 1]) for _ in range(12)]
    nivel_reservatorio = random.uniform(0.3, 1.0)
    estado_bomba = "LIGADA" if nivel_reservatorio < 0.7 else "DESLIGADA"
    return aspersores_status, nivel_reservatorio, estado_bomba

# Título do app
st.title("Painel de Monitoramento")

# Layout: Aspersores como círculos
st.subheader("Aspersores")
aspersores_status, nivel_reservatorio, estado_bomba = gerar_dados()

cols = st.columns(len(aspersores_status))  # Cria colunas para os aspersores
for col, status in zip(cols, aspersores_status):
    color = "green" if status == 1 else "red"
    col.markdown(
        f'<div style="width:30px; height:30px; border-radius:50%; background-color:{color}; margin:auto;"></div>',
        unsafe_allow_html=True,
    )

# Indicador do reservatório
st.subheader("Nível do Reservatório")
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=nivel_reservatorio * 100,
    gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "blue"}},
    title={'text': "Nível (%)"}
))
fig.update_layout(height=300)
st.plotly_chart(fig)

# Estado da bomba
st.subheader("Estado da Bomba")
estado_cor = "green" if estado_bomba == "LIGADA" else "red"
st.markdown(f'<h3 style="color:{estado_cor}; text-align:center;">{estado_bomba}</h3>', unsafe_allow_html=True)

# Atualização automática
st.markdown("---")
st.write("Atualizando os dados a cada segundo...")

# Loop de atualização
if st.button("Iniciar Monitoramento"):
    while True:
        aspersores_status, nivel_reservatorio, estado_bomba = gerar_dados()
        
        # Atualiza os aspersores
        cols = st.columns(len(aspersores_status))
        for col, status in zip(cols, aspersores_status):
            color = "green" if status == 1 else "red"
            col.markdown(
                f'<div style="width:30px; height:30px; border-radius:50%; background-color:{color}; margin:auto;"></div>',
                unsafe_allow_html=True,
            )

        # Atualiza o nível do reservatório
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=nivel_reservatorio * 100,
            gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "blue"}},
            title={'text': "Nível (%)"}
        ))
        fig.update_layout(height=300)
        st.plotly_chart(fig)

        # Atualiza o estado da bomba
        estado_cor = "green" if estado_bomba == "LIGADA" else "red"
        st.markdown(f'<h3 style="color:{estado_cor}; text-align:center;">{estado_bomba}</h3>', unsafe_allow_html=True)

        # Aguarda 1 segundo antes de atualizar
        time.sleep(1)
