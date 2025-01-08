from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import random

app = Dash(__name__)

# Layout do dashboard
app.layout = html.Div([
    html.H1("Painel de Monitoramento", style={'text-align': 'center'}),
    
    # Aspersores como círculos
    html.Div(id='aspersores', style={'display': 'flex', 'justify-content': 'center', 'gap': '10px'}),
    
    # Indicador do reservatório
    html.Div([
        html.H3("Nível do Reservatório"),
        dcc.Graph(id='reservatorio')
    ], style={'text-align': 'center'}),
    
    # Estado da bomba
    html.Div([
        html.H3("Estado da Bomba"),
        html.Div(id='estado-bomba', style={'font-size': '24px', 'color': 'red'})
    ], style={'text-align': 'center'}),
    
    # Atualização automática
    dcc.Interval(id='intervalo', interval=1000, n_intervals=0)  # Atualiza a cada segundo
])

# Callback para atualizar os dados
@app.callback(
    [Output('aspersores', 'children'),
     Output('reservatorio', 'figure'),
     Output('estado-bomba', 'children')],
    [Input('intervalo', 'n_intervals')]
)
def atualizar_dados(n):
    # Simulando dados
    aspersores_status = [random.choice([0, 1]) for _ in range(12)]
    nivel_reservatorio = random.uniform(0.3, 1.0)
    estado_bomba = "LIGADA" if nivel_reservatorio < 0.7 else "DESLIGADA"
    estado_cor = "green" if estado_bomba == "LIGADA" else "red"

    # Aspersores
    aspersores = [
        html.Div(
            style={
                'width': '30px',
                'height': '30px',
                'border-radius': '50%',
                'background-color': 'green' if status == 1 else 'red',
                'display': 'inline-block'
            }
        ) for status in aspersores_status
    ]

    # Indicador do reservatório
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=nivel_reservatorio * 100,
        gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "blue"}},
        title={'text': "Nível (%)"}
    ))
    fig.update_layout(height=300)

    # Estado da bomba
    estado = html.Div(estado_bomba, style={'color': estado_cor})

    return aspersores, fig, estado

if __name__ == '__main__':
    app.run_server(debug=True)
