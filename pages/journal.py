from dash import Dash, html, dcc, register_page, dash_table
import dash_bootstrap_components as dbc
from views import get_journal

register_page(__name__, name='Журнал', path='/journal')

layout = dbc.Container([
    html.H1('Журнал', className='display-5 text-center border-1 border-bottom pb-2 pt-3'),
    dash_table.DataTable(data=get_journal())
])