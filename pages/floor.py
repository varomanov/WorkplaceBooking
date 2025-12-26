from dash import Dash, html, dcc, register_page
import dash_bootstrap_components as dbc

register_page(__name__, name='Этажи', path='/floor')

layout = html.H1('Доступные этажи')