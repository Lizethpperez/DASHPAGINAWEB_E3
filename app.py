import dash
from dash import html, dcc
import dash_bootstrap_components as dbc 
import layout
import matplotlib.pyplot as plt



# Importamos los enlaces de las otras carpetas
from matplotlib import colors 
from Dash.frontend.Estructuras.area_superior.titulo import variableA
from Dash.frontend.Estructuras.area_subtitulos.subtitulos import variableB
from Dash.frontend.Estructuras.DatosCR.CanalR import variableCR
from Dash.frontend.Estructuras.DatosCT.CanalT import variableCT
from Dash.frontend.Estructuras.DatosCC.CanalC import variableCC
from Dash.frontend.Estructuras.DatosCTR.CanalTR import variableCTR

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(variableA, md=12, style={'textAlign': 'center'}),
        dbc.Col(variableB, md=12, style={'background-color':'gold', 'textAlign': 'center'}),
        dbc.Col(variableCR, md=12, style={'background-color':'darkturquoise'}),
        dbc.Col(variableCT, md=12, style={'background-color':'lightseagreen'}),
        dbc.Col(variableCC, md=12, style={'background-color':'turquoise'}),
        dbc.Col(variableCTR, md=12, style={'background-color':'paleturquoise'}),
    ])
])



# Callback para actualizar los cálculos cuando se ingresan nuevos valores de B y Y
@app.callback(
    [dash.dependencies.Output("Area_Canal", "children"),
     dash.dependencies.Output("Perimetro_Canal", "children"),
     dash.dependencies.Output("RH_Canal", "children"),
     dash.dependencies.Output("T_Canal", "children")],
    [dash.dependencies.Input("ValorB", "value"),
     dash.dependencies.Input("ValorY", "value")]
)
def update_properties(B, Y):
    # Aquí puedes realizar los cálculos necesarios
    area = B * Y  # Cálculo del área
    perimetro = ((2 * Y)+B)  # Cálculo del perímetro
    radio_hidraulico = (B*Y)/(B+(2*Y)) # Cálculo del radio hidráulico
    espejo_agua_T =B  # Cálculo del espejo de agua T
    
    return f"Área: {area}", f"Perímetro: {perimetro}", f"Radio Hidráulico: {radio_hidraulico}", f"Espejo de agua T: {espejo_agua_T}"

if __name__ == '__main__':
    app.run_server(debug=True)
