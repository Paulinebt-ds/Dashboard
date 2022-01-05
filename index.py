import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import dash_labs as dl  # pip install dash-labs
from ressources.app import app, server
from components.pages_plugin import *
from components.functions import navbarcurrentpage, corporate_colors
from pages.layout_client import data_domain


df = data_domain[data_domain["SK_ID_CURR"] == int(100002)]
df = df.to_dict('records')
# layout rendu par l'application
header = html.Div([

        html.Div([
            html.H1(children='Dashboard',
                    style={'textAlign': 'center',
                           'color': 'white'})
                ],
                className='col-8',
                style={'padding-top': '1%'}
                ),

        html.Div([
            html.Img(
                    src=app.get_asset_url("logo_pret_a_depenser.PNG"),
                    height='100',
                    width='200')
            ],
            className='col-2',
            style={
                    'align-items': 'center',
                    'padding-top': '1%',
                    'height': '100'})

        ],
        className='row',
        style={'height': '4%',
               'background-color': 'rgb(41, 56, 55)'}
        )
old_navbar = dbc.NavbarSimple(
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem(page["name"], href=page["path"])
            for page in dash.page_registry.values()
            if page["module"] != "pages.not_found_404"
        ],
        nav=True,
        label="More Pages",
    ),
    brand="Multi Page App Plugin Demo",
    color="primary",
    dark=True,
    className="mb-2",
)

navbar = html.Div([

        html.Div([dbc.Nav(
            [
                dbc.NavItem(
                    dbc.NavLink(page["name"], href=page["path"],  style=navbarcurrentpage)
                    for page in dash.page_registry.values())

            ],
            fill=True,
            justified=True
        )
            ],
            className='col-3'),

    ],
    className='row',
    style={'background-color': corporate_colors['dark-green'],
           'box-shadow': '2px 5px 5px 1px rgba(255, 101, 131, .5)'}
    )

app.layout = dbc.Container(
    [header,
     old_navbar,
     dcc.Store(id="memory-output", data=df),
     dl.plugins.page_container]
)


if __name__ == '__main__':
    app.run_server(debug=True)