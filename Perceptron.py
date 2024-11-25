from dash import Dash, dcc, html, Input, Output, callback
import pandas as pd
import plotly.express as px

# Incorporate data
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app
app = Dash()

# App layout
# app.layout = html.Div([
#     html.Div(html.H1('Blah My First App with Data and a Graph',
#                      style={'color': 'blue', 'background-color': '#629ccd', 'textAlign': 'center', 'padding': '7px'})),
#     # dash_table.DataTable(data=df.to_dict('records'), page_size=10),
#     dcc.Graph(figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg'))
# ])
tabs_styles = {
    'height': '44px',
    'align-items': 'center'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '10px',
    'fontWeight': 'bold',
    'border-radius': '15px',
    'background-color': '#F2F2F2',
}
tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'backgroundColor': '#3776ab',
    'color': 'white',
    'fontWeight': 'bold',
    'padding': '10px',
    'border-radius': '15px',
}

app.layout = html.Div([
    html.H1('Perceptron', 
            style={'color': 'white', 'background-color': '#629ccd', 'textAlign': 'center', 'padding': '7px'}),
    dcc.Tabs(id="tabs", value='tab1', children=[
        dcc.Tab(label='Observe perceptron', value='tab1', style = tab_style, selected_style = tab_selected_style),
        dcc.Tab(label='Optimization in municipalities', value='tab2', style = tab_style, selected_style = tab_selected_style),
        dcc.Tab(label='Seasonality of cases', value='tab3', style = tab_style, selected_style = tab_selected_style),
        # dcc.Tab(label='Ambulance turnaround times', value='tab4', style = tab_style, selected_style = tab_selected_style),
        # dcc.Tab(label='Cost analysis', value='tab5', style = tab_style, selected_style = tab_selected_style),
    ], style = tabs_styles),
    html.Div(id='tabs-content')
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
