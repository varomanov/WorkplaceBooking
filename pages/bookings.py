from dash import Dash, html, dcc, register_page
import dash_bootstrap_components as dbc

register_page(__name__, name='Бронь', path='/')

layout = dbc.Container([
    html.H1('Бронь', className='display-5 text-center border-1 border-bottom pb-2 pt-3'),
    dbc.Stack([
        dbc.Button('Себе', id='self-btn', className='btn-primary'),
        dbc.Button('Другому человеку', id='self-btn', className='btn-secondary'),
    ], direction='horizontal', gap=1, class_name='mt-5'),
    dbc.Select(id='booking_date', options=[1,2,3], placeholder='Дата бронирования', class_name='mt-5'),
    dbc.Select(id='booking_slot', options=[1,2,3], placeholder='Слот', class_name='mt-2'),
    html.P('Ваши избранные места', className='display-5 text-center mt-5'),

    html.Div(html.P('тут будут отображены избранные места'), className='border border-1', style={'height': '200px', 'color': 'lightgrey'})
])