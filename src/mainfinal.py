import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from PIL import Image
import os
from src.Sprint1 import base_donnee
from src.Sprint2 import ressemblance
from src.Sprint3 import adresse_image
from src.Sprint4 import mosaique
import pandas as pd

data = pd.read_json('Data/base_données_twitter.json')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Twinter'),
    html.H4("Entrez votre pseudo:"),
    html.Div([
        "Votre @",
        dcc.Input(id='my-input', value='ex: EmmanuelMacron', type='text')
    ]),
    html.Br(),
    html.Button('Valider', id='submit-val', n_clicks=0),
    html.Div(id='my-output'),
])


@app.callback(
    Output(component_id='my-output', component_property='children'),
    [Input('submit-val', 'n_clicks'),
     State('my-input', 'value')]
)
def update_output_div(n_clicks, input_value):
    mots_user = base_donnee([input_value])[input_value]

    test = adresse_image(ressemblance(mots_user, data))

    mosaique(test)
    im1 = Image.open('Résultat.jpg', mode='r')
    return html.Img(src=im1, height='600', width='750', alt="Photo Test", title=input_value),


if __name__ == '__main__':
    app.run_server(debug=True)
