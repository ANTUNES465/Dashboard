#import dash  substituting with DjangoDash 
from django_plotly_dash import DjangoDash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = DjangoDash('SimpleExample', external_stylesheets=external_stylesheets)
app.layout = html.Div([
    #html.H1('Balise H1 n°1 Square Root Slider Graph'),
    dcc.Graph(id='slider-graph', animate=True , style={"backgroundColor": '#1a2d46' , "color": '#ffffff'}),
    #html.H1('Balise H1 n°2 le graphique est censé être en n°1 et n°2'),
        dcc.Slider(
        id='slider-updatemode',
        marks={i: '{}'.format(i) for i in range(20)},
        min=0,
        max=21,
        step=1,
        value=5,
        updatemode='drag'
    ),
    html.Div(id='updatemode-output-container', style={'margin-top': 20})  

])

@app.callback(
    [Output('slider-graph', 'figure'), Output('updatemode-output-container', 'children')],
    [Input('slider-updatemode', 'value')])

def display_value(value):
    x =[i for i in range(value)]
    y = [i*i for i in range(value)]
    graph = go.Scatter(x=x, y=y, name ='Manipulate Graph' , mode='lines+markers', marker={'size': 10, 'color': 'red'})
    layout = go.Layout(
        paper_bgcolor ='#27293d' , plot_bgcolor = 'rgba(0,0,0,0)',
        title='Square Root Graph', 
        xaxis=dict(range=[min(x),max(x)]),
        yaxis=dict(range=[min(y),max(y)]),
        font=dict(color='white')
        )

    return {'data': [graph], 'layout': layout}, 'The square root of {} is {}'.format(value, value*value)

#if __name__ == '__main__':
#    app.run_server(debug=True)

