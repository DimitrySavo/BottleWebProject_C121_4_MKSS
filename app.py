from bottle import Bottle, run, request, static_file, template, response
from routes import *

app = Bottle()

app.route('/', 'GET', index)
app.route('/about', 'GET', about)

if __name__ == "__main__":
    app.run()
