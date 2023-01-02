import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc 

app = dash.Dash(__name__)
html.Style(
    'font-size': '20px'
)
app.layout = html.Div([
 html.Span(style={'font-size':"100px;'>&#9989"}),
            html.P('I will display &#9658'),
            html.P('I will display &#x2705;')
        
           ])
     
 

if __name__ == '__main__':
    app.run_server(port=2023,debug=True)