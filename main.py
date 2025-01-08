# import streamlit as st
# import plotly.graph_objects as go
# import random
# import time

# # Função para gerar os dados
# def gerar_dados():
#     aspersores_status = [random.choice([0, 1]) for _ in range(12)]
#     nivel_reservatorio = random.uniform(0.3, 1.0)
#     estado_bomba = "LIGADA" if nivel_reservatorio < 0.7 else "DESLIGADA"
#     return aspersores_status, nivel_reservatorio, estado_bomba

# # Título do app
# st.title("Painel de Monitoramento")

# # Layout: Aspersores como círculos
# st.subheader("Aspersores")
# aspersores_status, nivel_reservatorio, estado_bomba = gerar_dados()

# cols = st.columns(len(aspersores_status))  # Cria colunas para os aspersores
# for col, status in zip(cols, aspersores_status):
#     color = "green" if status == 1 else "red"
#     col.markdown(
#         f'<div style="width:30px; height:30px; border-radius:50%; background-color:{color}; margin:auto;"></div>',
#         unsafe_allow_html=True,
#     )

# # Indicador do reservatório
# st.subheader("Nível do Reservatório")
# fig = go.Figure(go.Indicator(
#     mode="gauge+number",
#     value=nivel_reservatorio * 100,
#     gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "blue"}},
#     title={'text': "Nível (%)"}
# ))
# fig.update_layout(height=300)
# st.plotly_chart(fig)

# # Estado da bomba
# st.subheader("Estado da Bomba")
# estado_cor = "green" if estado_bomba == "LIGADA" else "red"
# st.markdown(f'<h3 style="color:{estado_cor}; text-align:center;">{estado_bomba}</h3>', unsafe_allow_html=True)

# # Atualização automática
# st.markdown("---")
# st.write("Atualizando os dados a cada segundo...")

# # Loop de atualização
# if st.button("Iniciar Monitoramento"):
#     while True:
#         aspersores_status, nivel_reservatorio, estado_bomba = gerar_dados()
        
#         # Atualiza os aspersores
#         cols = st.columns(len(aspersores_status))
#         for col, status in zip(cols, aspersores_status):
#             color = "green" if status == 1 else "red"
#             col.markdown(
#                 f'<div style="width:30px; height:30px; border-radius:50%; background-color:{color}; margin:auto;"></div>',
#                 unsafe_allow_html=True,
#             )

#         # Atualiza o nível do reservatório
#         fig = go.Figure(go.Indicator(
#             mode="gauge+number",
#             value=nivel_reservatorio * 100,
#             gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "blue"}},
#             title={'text': "Nível (%)"}
#         ))
#         fig.update_layout(height=300)
#         st.plotly_chart(fig)

#         # Atualiza o estado da bomba
#         estado_cor = "green" if estado_bomba == "LIGADA" else "red"
#         st.markdown(f'<h3 style="color:{estado_cor}; text-align:center;">{estado_bomba}</h3>', unsafe_allow_html=True)

#         # Aguarda 1 segundo antes de atualizar
#         time.sleep(1)


import streamlit as st
import random

# Função para gerar os dados dos aspersores
def gerar_dados_aspersores():
    return [random.choice([0, 1]) for _ in range(12)]

# Estilo para o layout dos aspersores e imagem de fundo
STYLE = """
    <style>
        .container {
            position: relative;
            width: 100%;
            max-width: 600px;
            margin: auto;
        }
        .background-image {
            display: block;
            width: 100%;
            height: auto;
        }
        .circle {
            position: absolute;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            border: 2px solid black;
        }
        .circle-on { background-color: red; }
        .circle-off { background-color: lightblue; }

        /* Posições dos aspersores */
        .circle1 { top: 5%; left: 3%; }
        .circle2 { top: 5%; left: 31%; }
        .circle3 { top: 5%; left: 60%; }
        .circle4 { top: 5%; left: 92%; }

        .circle5 { top: 45%; left: 3%; }
        .circle6 { top: 45%; left: 33%; }
        .circle7 { top: 45%; left: 63%; }
        .circle8 { top: 45%; left: 93%; }

        .circle9 { top: 87%; left: 3%; }
        .circle10 { top: 87%; left: 33%; }
        .circle11 { top: 87%; left: 63%; }
        .circle12 { top: 87%; left: 93%; }
    </style>
"""

# Layout do app
st.title("Painel de Monitoramento")
st.subheader("Aspersores")

# Dados dos aspersores
aspersores_status = gerar_dados_aspersores()

# Inserindo o CSS no Streamlit
st.markdown(STYLE, unsafe_allow_html=True)

# Caminho da imagem de fundo (use sua própria imagem ou URL)
background_image_url = "https://izabeldietrich.com.br/wp-content/uploads/2024/12/campoH.png"  # Substitua pelo caminho da sua imagem

# Criação do layout com a imagem de fundo e os círculos
html_content = f"""
<div class="container">
    <img src="{background_image_url}" alt="Fundo dos Aspersores" class="background-image">
"""

# Adiciona os círculos com base no status dos aspersores
for i, status in enumerate(aspersores_status, start=1):
    css_class = "circle-on" if status == 1 else "circle-off"
    html_content += f'<div class="circle circle{i} {css_class}"></div>'

html_content += "</div>"

# Renderiza o HTML no Streamlit
st.markdown(html_content, unsafe_allow_html=True)
