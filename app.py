from bottle import Bottle, run, request, static_file, template, response
import json, os
import routes

app = Bottle()

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static').replace('\\', '/')
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '443'))
    except ValueError:
        PORT = 443

    @Bottle.route('/static/<filepath:path>')
    
    
    def server_static(filepath):
        return Bottle.static_file(filepath, root=STATIC_ROOT)