import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd
import numpy as np


# Load data
df_proptech = pd.read_csv('https://raw.githubusercontent.com/adeline-hub/light.danki/refs/heads/main/datasets/df_proptech_frenchtech.csv')
df_incubators = pd.read_csv('https://raw.githubusercontent.com/adeline-hub/light.danki/refs/heads/main/datasets/df_topincubators%20(1).csv')
df_allinvestors = pd.read_csv('https://raw.githubusercontent.com/adeline-hub/light.danki/refs/heads/main/datasets/df_allinvestors%20(2).csv')
df_FR_companies = pd.read_csv('https://raw.githubusercontent.com/adeline-hub/light.danki/refs/heads/main/datasets/df_FR_companies%20(2).csv')

#agregated data
df_incubators_fr = df_incubators[df_incubators['Country'] == 'France']
df_grouped = df_incubators_fr.groupby(['Accelerator / Incubator'], as_index=False)[['Number of Investments', 'Number of Exits']].sum()

# Define KPI values
kpi1_value = 37  # Top French companies in Real Estate
kpi2_value = 59  # Top French companies in Diverse Tech
kpi3_value = 414  

#  SWOT analysis content
strengths = [
    "Strong team & network",
    "Diversified product portfolio",
    "Real estate & Tech expertise"
]
weaknesses = [
    "High operational costs",
    "Dependence on a few incubators",
    "Limited investment industry presence"
]
opportunities = [
    "Expansion into new markets",
    "Partnership with tech companies",
    "Growing demand for sustainable products"
]
threats = [
    "Intense market competition",
    "Regulatory challenges",
    "Economic downturn"
]


# Initialize Dash app with pages
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Define the navigation layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("PropTech ⚙️", href="/")),
            dbc.NavItem(dbc.NavLink("Investors & Distribution", href="/page-2")),
            dbc.NavItem(dbc.NavLink("Exit & SWOT", href="/page-3")),
        ],
        brand="PropTech Market Study - France",
        brand_href="/",
        color="dark",  # Change to "secondary", "success", "info", "warning", "danger", etc.
        dark=True  # Set to False if using a light color
    ),
    html.Div(id='page-content')
])

def page_1_layout():
    return html.Div([
        html.H1("PropTech Technologies Overview", style={'color': '#FF33FF'}),

        dcc.Markdown("""

                    This dashboard presents the major **stakeholders** of the PropTech Investment Industry in France:
                    **PropTech** projects and companies, **Incubators**, **Investors**, **Companies** as possible PropTech buyers.

                    """),
        #html.P("The output of a technology can vary significantly based on its associations..."),
        html.Div([
                       html.Img(src="https://github.com/adeline-hub/light.danki/blob/main/images/logo_danki.png?raw=true",
                                  style={'height': '20px', 'margin-right': '20px'})
                      ], style={'display': 'flex', 'align-items': 'center'}),

        # Add the missing dropdown
        #dcc.Dropdown(
        #    id="item-filter",
        #    options=[{'label': tech, 'value': tech} for tech in df_proptech['income_stream (technology)'].dropna().unique()],
        #    placeholder="Select a technology",
        #    multi=True
        #),

        dbc.Row([
            dbc.Col(
              dbc.Accordion([
                  dbc.AccordionItem(
                      title=html.Div([
                          html.Img(src="https://cdn3.iconfinder.com/data/icons/crypto-coins-8/32/Ethereum_crypto_cryptocurrency-1024.png",
                                  style={'height': '20px', 'margin-right': '10px'}),
                          "Manufacturing 🔗"
                      ], style={'display': 'flex', 'align-items': 'center'}),
                      children="The use of technology to improve and automate the process of producing goods and services. This can involve machinery, robotics, and other innovations that optimize production efficiency and quality."
                  ),
                  dbc.AccordionItem(
                      title=html.Div([
                          html.Img(src="https://cdn4.iconfinder.com/data/icons/nft-non-fungible-token-5/32/NFT_mobile_Nft_blockchain_crypto_non-fungible_token-1024.png",
                                  style={'height': '20px', 'margin-right': '10px'}),
                          "Mobile app, SaaS 🔗"
                      ], style={'display': 'flex', 'align-items': 'center'}),
                      children="A software-as-a-service (SaaS) solution delivered through a mobile application. It allows users to access software and services over the internet via their smartphones or tablets, without needing to install traditional software."
                  ),
                  dbc.AccordionItem(
                      title=html.Div([
                          html.Img(src="https://cdn2.iconfinder.com/data/icons/web-and-seo-1-2/65/31-512.png",
                                  style={'height': '20px', 'margin-right': '10px'}),
                          "Big Data, Artificial Intelligence, SaaS 🔗"
                      ], style={'display': 'flex', 'align-items': 'center'}),
                      children="The combination of big data and artificial intelligence with SaaS. This enables businesses to analyze large datasets and apply machine learning models to gain deeper insights and optimize their operations in real time."
                  ),
                  dbc.AccordionItem(
                      title=html.Div([
                          html.Img(src="https://cdn3.iconfinder.com/data/icons/web-design-and-development-2-10/66/63-1024.png",
                                  style={'height': '20px', 'margin-right': '10px'}),
                          "Big Data, Marketplace & Ecommerce 🔗"
                      ], style={'display': 'flex', 'align-items': 'center'}),

                      children="The application of big data analytics to ecommerce and marketplace platforms. By analyzing large volumes of transactional data, businesses can uncover trends, customer behavior, and optimize operations in real-time."
                  ),
                  dbc.AccordionItem(
                      title=html.Div([
                          html.Img(src="https://cdn4.iconfinder.com/data/icons/modern-technologies-1/32/technology_Block_blockchain_chain_cryptocurrency-04-512.png",
                                  style={'height': '20px', 'margin-right': '10px'}),
                          "Blockchain, SaaS 🔗"
                      ], style={'display': 'flex', 'align-items': 'center'}),
                      children="The integration of blockchain technology with a SaaS platform. Blockchain offers decentralized, secure, and transparent transaction methods that can be used for applications such as digital contracts, financial transactions, and data management."
                  ),
              ], start_collapsed=True), width=8
            ),
            dbc.Col(dcc.Graph(id='tech-frequency-boxplot'), width=4)
        ]),

        dbc.Row([
            dbc.Col(
                dcc.Markdown("""
                    ### PropTech Business Model
                    In **France**, the dominant business models in PropTech are **commission-based** and **subscription-based**,
                    with fewer companies relying on selling their own inventory or combining subscription and commission models.

                    **Globally**, however, major players in the PropTech sector also embrace **commission and subscription models**
                    but have increasingly diversified with models such as **marketplace platforms**, **data analytics services**,
                    and **partnerships** with real estate developers and financial institutions.

                """),
                width=8
            ),
            dbc.Col(
                html.Div([
                       html.Img(src="https://github.com/adeline-hub/light.danki/blob/main/images/cernunnos.jpg?raw=true",
                                  style={'height': '150px', 'margin-right': '400px'})
                      ], style={'display': 'flex', 'align-items': 'center'}),
                width=4
            )
        ]),

        dbc.Row([
            dbc.Col(
                dcc.Graph(id='bm-barplot'), width=8
            ),
            dbc.Col(
                dcc.Markdown("""
                    ### PropTech combining Technologies
                    The output of a technology can vary significantly based on its associations,
                    as different combinations of technologies serve distinct purposes and create unique solutions.

                    For example, in PropTech, combining **AI and big data** could provide predictive analytics for
                    real estate price trends, while pairing **IoT and SaaS** might enable remote monitoring and management
                    of smart buildings for improved energy efficiency.

                    _(Source: FrenchTech, 2025)_
                    """), width=4)
        ]),
        # Footer
        dbc.Row([
            dbc.Col(html.P("© 2025 .danki", className="text-muted"), width=4),
            dbc.Col(html.A("📄 Documentation", href="https://drive.google.com/file/d/1sVCZLWGOKfHPTLO_FHehl0t75G-SYMId/view?usp=drive_link", target="_blank"), width=4),
            dbc.Col(dbc.Button("📥 Download PDF", href="https://drive.google.com/file/d/1sVCZLWGOKfHPTLO_FHehl0t75G-SYMId/view?usp=drive_link", target="_blank"), width=4)
        ], className="mt-4 text-center"),

    ])



# Page 2: Investors in Tech & PropTech Distribution in France
def page_2_layout():
    return html.Div([
        dbc.Row([
            dbc.Col(dcc.Markdown("""
                ### Opportunities with PropTech Incubators
                - **For PropTech startups**, incubators provide mentorship, industry connections, and opportunities to pilot solutions, helping accelerate growth and refine business models.
                - **For investors**, incubators offer access to early-stage PropTech ventures, enabling investments in high-potential startups and insights into emerging trends.
                """), width=12),
        ]),
        dbc.Row([
            dbc.Col(dcc.Graph(id='callback2_1'), width=4),
            dbc.Col(
                html.Div([
                       html.Img(src="https://github.com/adeline-hub/light.danki/blob/main/images/cernunnos.jpg?raw=true",
                                  style={'height': '300px', 'margin-right': '400px'})
                      ], style={'display': 'flex', 'align-items': 'center'}),
                width=2),
            dbc.Col(dcc.Graph(id='callback2_2'), width=6),
        ]),
        dbc.Row([
            dbc.Col(dcc.Graph(id='callback2_4'), width=5),
            dbc.Col(dcc.Markdown("""
                ### Tech & Real Estate Investors in PropTech
                - **Tech investors** drive innovation but may lack real estate expertise.
                - **Real estate investors** offer market knowledge but struggle with tech adoption.
                Collaboration between both is key to scaling PropTech successfully.

                _(Source: .danki, 2025)_ """), width=2),
            dbc.Col(dcc.Graph(id='callback2_3'), width=5),
        ]),
        # Footer
        dbc.Row([
            dbc.Col(html.P("© 2025 .danki", className="text-muted"), width=4),
            dbc.Col(html.A("📄 Documentation", href="https://drive.google.com/file/d/1sVCZLWGOKfHPTLO_FHehl0t75G-SYMId/view?usp=drive_link", target="_blank"), width=4),
            dbc.Col(dbc.Button("📥 Download PDF", href="https://drive.google.com/file/d/1sVCZLWGOKfHPTLO_FHehl0t75G-SYMId/view?usp=drive_link", target="_blank"), width=4)
        ], className="mt-4 text-center"),
    ])


# Page 3: Potential Acquisitions & SWOT Analysis

def page_3_layout():
    return html.Div([
         html.H1("Exit Strategies for Early PropTech Investors"),
         dbc.Row([
            dbc.Col(dcc.Markdown("""
                Investors in early-stage **PropTech** startups have multiple exit options:

                - **Acquisition** by real estate giants or larger PropTech firms.
                - **IPO or SPAC Merger** for public market access.
                - **Private Equity Buyout** or **Secondary Market Sale** to other investors.
                - **Dividends or Buybacks** for gradual exits in profitable startups."""), width=12),
        ]),
        dbc.Row([
            dbc.Col(dbc.Card([dbc.CardBody([
                        html.H4("Top French Companies (Real Estate)", className="card-title"),
                        html.H2(f"{kpi1_value}", className="card-value")])
                ], color="dark", inverse=True), width=4),
            dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H4("Top French Companies (Tech)", className="card-title"),
                        html.H2(f"{kpi2_value}", className="card-value")])
                ], color="dark", inverse=True), width=4),
            dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H4("Total Companies Analyzed", className="card-title"),
                        html.H2(f"{kpi3_value}", className="card-value")])
                ], color="dark", inverse=True), width=4)
        ], className="mb-4"),
        dbc.Row([
            dbc.Col(dcc.Graph(id='callback3_1'), width=6),
            dbc.Col(dcc.Graph(id='callback3_2'), width=6),
        ]),
        html.H1("SWOT analysis"),
        dbc.Row([  # Creating a row with 4 columns
            dbc.Col(dbc.Card(
                children=[
                    html.H4("Strengths", className="card-title"),
                    html.Ul([html.Li(item) for item in strengths], className="card-text")
                ],
                color="primary", inverse=True
            ), width=3),

            dbc.Col(dbc.Card(
                children=[
                    html.H4("Weaknesses", className="card-title"),
                    html.Ul([html.Li(item) for item in weaknesses], className="card-text")
                ],
                color="primary", inverse=True
            ), width=3),

            dbc.Col(dbc.Card(
                children=[
                    html.H4("Opportunities", className="card-title"),
                    html.Ul([html.Li(item) for item in opportunities], className="card-text")
                ],
                color="primary", inverse=True
            ), width=3),

            dbc.Col(dbc.Card(
                children=[
                    html.H4("Threats", className="card-title"),
                    html.Ul([html.Li(item) for item in threats], className="card-text")
                ],
                color="primary", inverse=True
            ), width=3),
        ]),
        # Footer
        dbc.Row([
            dbc.Col(html.P("© 2025 .danki", className="text-muted"), width=4),
            dbc.Col(html.A("📄 Documentation", href="https://drive.google.com/file/d/1sVCZLWGOKfHPTLO_FHehl0t75G-SYMId/view?usp=drive_link", target="_blank"), width=4),
            dbc.Col(dbc.Button("📥 Download PDF", href="https://drive.google.com/file/d/1sVCZLWGOKfHPTLO_FHehl0t75G-SYMId/view?usp=drive_link", target="_blank"), width=4)
        ], className="mt-4 text-center"),
    ])

# Callback to update page content

@app.callback(
    Output('page-content', 'children'),
     [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/page-2':
        return page_2_layout()
    elif pathname == '/page-3':
        return page_3_layout()
    return page_1_layout()

# 📌 Page 1 Callbacks: PropTech

@app.callback(
    Output("tech-frequency-boxplot", "figure"),
    Input("url", "pathname")  # Update on page load instead
)
def update_boxplot(selected_item):
    df_proptech_split = df_proptech['income_stream (technology)'].dropna().str.split(',\s*')
    technology_counts = df_proptech_split.explode().value_counts().reset_index()
    technology_counts.columns = ['technology', 'count']
    total_count = technology_counts['count'].sum()
    technology_counts['percentage'] = ((technology_counts['count'] / total_count) * 100).round().astype(int)
    technologies = technology_counts['technology'].tolist()
    counts = technology_counts['percentage'].tolist()
    tech_index = {tech: idx for idx, tech in enumerate(technologies)}
    # Define the source (start node) and target (end node) for the Sankey chart
    sources = [tech_index[tech] for tech in technologies]
    targets = [len(technologies)] * len(technologies)  # Targeting a single node that represents all technologies
    # Create the values which represent the count (frequency) of each technology
    values = counts

    # Create the Sankey chart
    fig = go.Figure(go.Sankey(
        node=dict(
            pad=55,  # Padding between nodes
            thickness=20,  # Thickness of nodes
            line=dict(color="black", width=0.5),
            label=technologies + ['a PropTech technology'],  # Add a label for the 'Total' node
            color="rgba(255,0,255, 0.8)"  # Color for nodes
        ),
        link=dict(
            source=sources,
            target=targets,
            value=values,
            color='#33FFA2'  # Light green color for the links
        )
    ))

    # Update layout to make it horizontal
    fig.update_layout(
        title_text="Technology Frequency Distribution in French PropTech",
        font_size=12,
        height=400,
        width=600
    )
    return fig

@app.callback(
    Output("bm-barplot", "figure"),
    Input("url", "pathname")  # Update on page load instead
)
def update_barplot(selected_item):
    business_model_counts = df_proptech['business_model '].value_counts().reset_index()
    business_model_counts.columns = ['business_model ', 'count']
    custom_colors = ['#FF33FF', '#33FFA2', '#898B8E', '#009688', '#a48363']
    unique_models = business_model_counts['business_model '].unique()
    color_map = {model: custom_colors[i % len(custom_colors)] for i, model in enumerate(unique_models)}

    # Create a bar chart
    fig = px.bar(
        business_model_counts,
        y='business_model ',
        x='count',
        title="Major Business Models in French PropTech 2020-2025",
        color='business_model ',
        color_discrete_map=color_map,  # Apply custom colors
        orientation='h'
    )
    # Update layout for better readability
    fig.update_layout(
        xaxis_tickangle=-45,  # Rotate x-axis labels for better visibility
        showlegend=False       # Hide legend as it might be redundant
    )
    return fig




# 📌 Page 2 Callbacks: Investors in Tech & PropTech Distribution in France

# ✅ Callback 1: Update the incubators table based on the selected year
@app.callback(
    Output("callback2_1", "figure"),
    Input("url", "pathname")  # Update on page load instead
)
def update_callback2_1(_):  # No need for selected_item
    df_top7 = df_grouped.sort_values(by='Number of Investments', ascending=False).head(7)

    #fig = ff.create_table(df_top7, height_constant=40)
    header_color = '#33FFA2'
    row_color = 'lightgrey'
    font_color = 'white'
    alt_row_color = 'whitesmoke'

    fig = ff.create_table(df_top7, height_constant=40, colorscale=[[0, header_color], [0.5, row_color], [1, alt_row_color]])

    return fig

# ✅ Callback 2: Generate scatter plot of incubators' investment vs exits
@app.callback(
    Output("callback2_2", "figure"),
    Input("url", "pathname")  # Update on page load instead
)
def update_callback2_2(selected_item):
    df_incubators_clean = df_incubators.dropna(subset=['Number of Investments', 'Number of Exits'])

    fig = px.scatter(df_incubators_clean, x="Number of Investments", y="Number of Exits",
                    size="Number of Investments", color="Country",
                    hover_name="Accelerator / Incubator", log_x=True, size_max=60)
    return fig


# ✅ Callback 3: Create a bar chart of top tech investors in France
@app.callback(
    Output("callback2_3", "figure"),
    Input("url", "pathname")  # Update on page load instead
)
def update_callback2_3(selected_item):
    df_all_France_Tech = df_allinvestors[(df_allinvestors['Country_ok'] == 'France') & (df_allinvestors['Areas of investment'].str.contains('ProTech|Tech|Software|Analytics|Real Estate', case=False, na=False))]
    df_top_7_investors = df_all_France_Tech.sort_values(by='Portfolio companies', ascending=False).head(10)

    fig = px.bar(df_top_7_investors, x="Total investments", y="Investor Name", color='Portfolio companies',
                color_continuous_scale='Jet', orientation='h', title="Top 7 French Investors in Tech")
    fig.update_layout(height=400, bargap=0.2, title_x=0.5,showlegend=False)
    return fig



# ✅ Callback 4: Generate geographical plot of investors
@app.callback(
    Output("callback2_4", "figure"),
    Input("url", "pathname")  # Update on page load instead
)
def update_callback2_4(selected_item):
    fig = px.scatter_geo(df_allinvestors,
                     locations="Country_iso_alpha3",
                     color="Total investments",
                     hover_name="Investor Name",
                     #size="Portfolio companies",
                     size_max=50,
                     title="(Prop)Tech investors distribution",
                     projection="eckert4")
    fig.update_layout(showlegend=False)  # Hide the legend
    return fig


# 📌 Page 3 Callbacks: Exit & SWOT

import plotly.figure_factory as ff
import pandas as pd

# ✅ Callback 1: tab real estate
@app.callback(
    Output("callback3_1", "figure"),
    Input("url", "pathname")  # Update on page load instead
)
def update_callback3_1(_):  # No need for selected_item
    df_FR_RE = df_FR_companies[df_FR_companies['Sector'].str.contains('Real Estate', case=False, na=False)]
    filtered_RE_df = df_FR_RE.groupby('Company')['Market Cap (Billion USD)'].sum().round().astype(int).nlargest(7)
    filtered_RE_df = filtered_RE_df.reset_index() 
    
    header_color = '#33FFA2'
    row_color = 'lightgrey'
    font_color = 'white'
    alt_row_color = 'whitesmoke'

    fig = ff.create_table(filtered_RE_df, height_constant=40, colorscale=[[0, header_color], [0.5, row_color], [1, alt_row_color]])
    return fig

# ✅ Callback 2: tab tech
@app.callback(
    Output("callback3_2", "figure"),
    Input("url", "pathname")  # Update on page load instead
)
def update_callback3_2(_):  # No need for selected_item
    df_FR_tech = df_FR_companies[df_FR_companies['Sector'].str.contains('Tech', case=False, na=False)]
    filtered_tech_df = df_FR_tech.groupby('Company')['Market Cap (Billion USD)'].sum().round().astype(int).nlargest(7)
    filtered_tech_df = filtered_tech_df.reset_index()  # Converts the Series to DataFrame
        
    header_color = '#33FFA2'
    row_color = 'lightgrey'
    font_color = 'white'
    alt_row_color = 'whitesmoke'

    fig = ff.create_table(filtered_tech_df, height_constant=40, colorscale=[[0, header_color], [0.5, row_color], [1, alt_row_color]])
    return fig


# ✅ Callback 3: Create a bar chart of top tech investors in France


# ✅ Callback 4: Generate geographical plot of investors



if __name__ == '__main__':
    app.run_server(debug=True)

server = app.server
