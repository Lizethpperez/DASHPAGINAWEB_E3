from dash import html
import dash_bootstrap_components as dbc

# Estilos CSS para los botones
button_style = {
    'width': '20%',  # Establecer el ancho igual para cada botón
    'margin-right': '10px',  # Margen derecho para separar los botones
    'margin-bottom': '10px'  # Margen inferior para separar las filas
}

# Contenedor de los botones en una sola fila
variableB = html.Div([
    html.Button('INICIO', style=button_style),
    html.Button('CANAL RECTANGULAR', style=button_style),
    html.Button('CANAL TRAPEZOIDAL', style=button_style),
    html.Button('CANAL CIRCULAR', style=button_style),
    html.Button('CANAL TRIANGULAR', style=button_style),
], style={'display': 'flex', 'justify-content': 'space-between'})  # Distribución uniforme de los botones
