from bottle import Bottle, run, request, static_file, template, response
from routes import *

app = Bottle()

app.route('/', 'GET', index)
app.route('/about', 'GET', about)
app.route('/static/<filepath:path>', 'GET', server_static)

if __name__ == "__main__":
    app.run()
