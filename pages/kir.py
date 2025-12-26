from dash import Dash, html, dcc, register_page
import dash_bootstrap_components as dbc

register_page(__name__, name='КИР', path='/kir')

layout = html.H1('КИР')