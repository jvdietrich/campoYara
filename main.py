from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Div
from bokeh.plotting import curdoc, figure
import random

# Dados iniciais
source = ColumnDataSource(data={'aspersores': [random.choice([0, 1]) for _ in range(12)]})

# Figura para aspersores
plot = figure(title="Status dos Aspersores", x_range=(0, 4), y_range=(0, 3), tools="")
plot.circle(
    x=[i % 4 for i in range(12)], 
    y=[i // 4 for i in range(12)],
    size=40, color=['green' if s == 1 else 'red' for s in source.data['aspersores']]
)

# Indicador de nível
nivel = Div(text="<h3>Nível do Reservatório: 75%</h3>", width=400)

# Estado da bomba
estado_bomba = Div(text="<h3>Bomba: DESLIGADA</h3>", width=400, style={'color': 'red'})

# Layout
layout = column(
    plot,
    nivel,
    estado_bomba
)

curdoc().add_root(layout)

def atualizar():
    # Atualiza dados
    aspersores = [random.choice([0, 1]) for _ in range(12)]
    source.data = {'aspersores': aspersores}
    nivel.text = f"<h3>Nível do Reservatório: {random.randint(50, 100)}%</h3>"
    estado_bomba.text = "<h3>Bomba: LIGADA</h3>" if random.choice([0, 1]) else "<h3>Bomba: DESLIGADA</h3>"

curdoc().add_periodic_callback(atualizar, 1000)  # Atualiza a cada segundo
