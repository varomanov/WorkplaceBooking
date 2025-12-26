from dash import Dash, dcc, html, page_container
import dash_bootstrap_components as dbc

app = Dash(__name__,
           use_pages=True,
           external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.Div(
        page_container,
    ),
    html.Nav([
        html.Link(
            rel='stylesheet',
            href='https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css'
        ),
        html.Ul([
            html.Li(dcc.Link([html.I(className='bi bi-calendar3'),
                    html.P('Бронь', className='m-0 p-0 fw-bold')], href='/')),
            html.Li(dcc.Link([html.I(className='bi bi-journal-check'),
                    html.P('Журнал', className='m-0 p-0 fw-bold')], href='/journal')),
            html.Li(dcc.Link([html.I(className='bi bi-view-stacked'),
                    html.P('Этажи', className='m-0 p-0 fw-bold')], href='/floor')),
            html.Li(dcc.Link([html.I(className='bi bi-person-workspace'),
                    html.P('КИР', className='m-0 p-0 fw-bold')], href='/kir'))
        ])
    ], className='mt-auto')
], className='vh-100 d-flex flex-column')

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(port='8501', host='0.0.0.0')
