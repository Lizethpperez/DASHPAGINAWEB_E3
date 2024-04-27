from dash import html, dcc
import dash_bootstrap_components as dbc
from flask import Flask, render_template
import layout
from PIL import Image



areadatosr = dbc.Container([
    html.H1("CANAL RECTANGULAR"),
    html.H2("Encontraremos las Propiedades Hidráulicas"),

    # Valores de Entrada B y Y
    html.Div([
        html.Label("Valor de B"),
        dcc.Input(id="ValorB", type="number", placeholder="Ingrese el valor de B"),
    ]),
    
    html.Div([
        html.Label("Valor de Y"),
        dcc.Input(id="ValorY", type="number", placeholder="Ingrese el valor de Y"),
    ]),

    # Cálculo del área
    html.Div([
        html.Label("Área del Canal"),
        html.Label(id="Area_Canal"),
    ]),
    
    # Cálculo del perímetro
    html.Div([
        html.Label("Perímetro del Canal"),
        html.Label(id="Perimetro_Canal"),
    ]),
    
    # Cálculo del Radio Hidráulico
    html.Div([
        html.Label("Radio Hidráulico"),
        html.Label(id="RH_Canal"),
    ]),
    
    # Cálculo del Espejo de agua T
    html.Div([
        html.Label("Espejo de agua T"),
        html.Label(id="T_Canal"),

    ]),
])
 


variableCR = dbc.Container([
     dbc.Row([
         html.Br(),
         dbc.Col('IMAGEN GEOMETRIA DEL CANAL', md=3, style={'textAlign': 'center', 'background-color': 'honeydew'}),
         html.Br(), 
         html.Br(),
          html.Br(),
           html.Br(),
            html.Br(),
             html.Br(),
              html.Br(),
               html.Br(),
                html.Br(),
                 html.Br(),
                  html.Br(),
                   
                   html.Br(),
        dbc.Col(areadatosr, md=9, style={'textAlign': 'center'}),
        
  
  
    ])  
])

   
