from dash import html, dcc
from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

# Crea la aplicación Dash
app = DjangoDash('SimpleDashApp')  # El nombre debe ser único

# Ajusta los estilos para eliminar el padding
app.layout = html.Div(
    style={
        'padding': '0px',  # Elimina cualquier padding
        'margin': '0px',   # Elimina cualquier margen
        'width': '100%',   # Asegúrate de que ocupe todo el ancho
        'height': '90vh',  # Asegúrate de que ocupe toda la altura visible
        
    },
    children=[
        html.H1(
            'Hello Dash',
            style={'text-align': 'center', 'margin': '0px'}  # Centra el texto y elimina márgenes
        ),
        html.Div(
            'Dash: A web application framework for Python.',
            style={'text-align': 'center', 'margin': '0px'}  # Centra el texto y elimina márgenes
        ),
        dcc.Graph(
            id='example-graph',
            style={'height': '40vh'},  # Ajusta el tamaño de la gráfica dentro del contenedor
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montreal'},
                ],
                'layout': {
                    'title': 'Dash Data Visualization',
                    'autosize': True,
                    'margin': {'l': 10, 'r': 10, 't': 30, 'b': 30},  # Márgenes ajustados
                }
            }
        )
    ]
)
