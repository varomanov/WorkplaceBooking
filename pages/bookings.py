from dash import Dash, html, dcc, register_page, callback, Output, Input, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from views import add_booking, get_places, get_users
from datetime import date, timedelta

register_page(__name__, name='Бронь', path='/')

layout = dbc.Container([
    html.H1('Бронь', className='display-5 text-center border-1 border-bottom pb-2 pt-3'),
    dbc.Stack([
        dbc.Button('Себе', id='self-btn', className='btn-primary'),
        dbc.Button('Другому человеку', id='other-btn',
                   className='btn-secondary'),
    ], direction='horizontal', gap=1, class_name='mt-2'),
    dbc.Select(id='booking_user', options=get_users(),
               placeholder='Пользователь', class_name='mt-3'),
    dbc.Select(id='booking_date', options=[date.today() + timedelta(days=x)
               for x in range(15)], placeholder='Дата бронирования', class_name='mt-3'),
    dbc.Select(id='booking_slot', options=get_places(),
               placeholder='Место', class_name='mt-2'),
    html.P('Ваши избранные места', className='display-5 text-center mt-3'),

    html.Div(html.P('тут будут отображены избранные места'),
             className='border border-1', style={'height': '100px', 'color': 'lightgrey'}),
    dbc.Button('Бронировать', id='book-btn', className='btn-primary mt-3'),
    html.Div(id='output')
])


@callback(
    Output('output', 'children'),
    Input('book-btn', 'n_clicks'),
    State('booking_user', 'value'),
    State('booking_date', 'value'),
    State('booking_slot', 'value'),
    prevent_initial_call=True
)
def make_booking(nclicks, user, period, slot):
    if nclicks:
        if user is None or period is None or slot is None:
            raise PreventUpdate
        else:
            add_booking(user=user, place=slot)
            return dbc.Alert('Место забронировано! Детали в Журнале бронирований', duration=2000)
