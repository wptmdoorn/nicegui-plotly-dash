from dash_page import page
from fastapi.middleware.wsgi import WSGIMiddleware
from nicegui import ui, app


@ui.page('/other_page')
def other_page():
    ui.label('Welcome to the other side')


# A bit odd, but the only way I've been able to get prefixing of the Dash app
# to work is by allowing the Dash/Flask app to prefix itself, then mounting
# it to root
dash_app = page(requests_pathname_prefix="/dash/")
app.mount("/dash", WSGIMiddleware(dash_app.server))

# fulfill
ui.run(title='NiceGUI - Dash Plotly Example', host='0.0.0.0', port=8080)
