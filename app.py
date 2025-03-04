import dash_mantine_components as dmc
from dash import Dash, html, dcc, Input, Output
from dash_iconify import DashIconify
import pandas as pd
import plotly.express as px

app = Dash(__name__)

# Sample DataFrame
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

markdown_text = '''
### Dash and Markdown
Each work should be ...
'''

# App Layout
app.layout = html.Div(children=[
    html.H1(children='Hello Citrus Fan'),

    html.Div(children='''Dash: A web application framework for your data.'''),

    dcc.Markdown(markdown_text),  # Display Markdown

    dcc.Dropdown(
        id='city-dropdown',
        options=[{'label': city, 'value': city} for city in df["City"].unique()],
        value=df["City"].unique().tolist(),  # Default to selecting all cities
        multi=True  # Allow multiple selections
    ),

    dcc.Graph(id='example-graph')
])

# Callback to Update the Chart Based on Dropdown Selection
@app.callback(
    Output('example-graph', 'figure'),
    Input('city-dropdown', 'value')
)
def update_graph(selected_cities):
    filtered_df = df[df["City"].isin(selected_cities)]  # Filter based on selection
    fig = px.bar(filtered_df, x="Fruit", y="Amount", color="City", barmode="group")
    return fig

# Run the App
if __name__ == "__main__":
    app.run_server(debug=True)

server = app.server
