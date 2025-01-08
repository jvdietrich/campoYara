import streamlit as st
import time

# Configuração da página
st.set_page_config(page_title="Painel de Monitoramento", layout="wide")

# Título e cabeçalho
st.title("Painel de Monitoramento")
st.subheader("Status dos Aspersores e Reservatório")

# Simulação de dados iniciais
aspersores_status = [1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1]  # 1 = ligado, 0 = desligado
nivel_reservatorio = 0.75  # 75%
estado_bomba = 1  # 1 = ligada, 0 = desligada

# Atualização periódica
def atualizar_dados():
    # Simula dados atualizados
    global aspersores_status, nivel_reservatorio, estado_bomba
    aspersores_status = [1 if i % 2 == 0 else 0 for i in range(12)]
    nivel_reservatorio = max(0.0, min(1.0, nivel_reservatorio + 0.1 * (-1 if estado_bomba else 1)))
    estado_bomba = 1 if nivel_reservatorio < 0.8 else 0

# Exibição dos aspersores
st.subheader("Status dos Aspersores")
cols = st.columns(4)  # Dividindo em 4 colunas
for i, status in enumerate(aspersores_status):
    with cols[i % 4]:
        color = "green" if status == 1 else "red"
        st.markdown(
            f"<div style='width: 30px; height: 30px; border-radius: 50%; background-color: {color}; margin: auto;'></div>",
            unsafe_allow_html=True,
        )

# Indicador do nível do reservatório
st.subheader("Nível do Reservatório")
st.progress(int(nivel_reservatorio * 100))
st.write(f"Nível atual: {nivel_reservatorio * 100:.0f}%")

# Estado da bomba
st.subheader("Estado da Bomba")
estado_texto = "LIGADA" if estado_bomba == 1 else "DESLIGADA"
estado_cor = "green" if estado_bomba == 1 else "red"
st.markdown(
    f"<span style='font-size: 1.5em; color: {estado_cor};'>{estado_texto}</span>",
    unsafe_allow_html=True,
)

# Link para a tabela
st.markdown(
    "[Clique aqui para acessar a tabela com as últimas 48 horas](https://docs.google.com/spreadsheets/d/1kjLx7Cbj_EMQLHRCqgEEKKgUPZd9HS-DFruKavRNOvM)",
    unsafe_allow_html=True,
)

# Atualização automática
placeholder = st.empty()
while True:
    with placeholder.container():
        atualizar_dados()
        time.sleep(1)  # Atualiza os dados a cada segundo
