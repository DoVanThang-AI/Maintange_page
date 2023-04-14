import dash
import dash_bootstrap_components as dbc
from dash import html
import dash
import dash_core_components as dcc
import dash_extensions as de
import dash_html_components as html
from dash.dependencies import Output, Input,State
import dash_bootstrap_components as dbc
import dash_extensions as de

app = dash.Dash(__name__,
                external_stylesheets=[dbc.icons.FONT_AWESOME,dbc.themes.BOOTSTRAP],suppress_callback_exceptions=True
       )
maintance_url = 'https://assets5.lottiefiles.com/packages/lf20_p3HYrw.json'
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

app.layout = html.Div([
    dbc.Container([
        html.Div([
            # html.Img(src='/assets/setting.svg',style={'display':'block','margin-left':'auto','margin-right':'auto','margin-top':'5%','width':'20%','color':'black'}),
            de.Lottie(options=options, width="25%", height="25%", url=maintance_url),
            html.Br(),
            html.H1("We'll be back soon !", style={'text-align':'center','font-weight':'bold','font-size':'5rem','color':'black'}),
            html.H1('The website under maintenance',style={'text-align':'center'}),
            html.Br(),
            html.P(['We’re very sorry for the inconvenience but we’re performing maintenance. Please check back soon',html.B(" Apr 19th, 2023.")],style={'text-align':'center'})

        ])
    ],fluid=True)
])

if __name__ == '__main__':
    app.run_server(debug=True,port=8050)