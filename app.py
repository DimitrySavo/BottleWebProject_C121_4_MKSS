from bottle import Bottle, run, request, static_file, template, response
import json

app = Bottle()

@app.route('/')
def index():
    return template('index')

# Страницы для перехода
@app.route('/page1')
def page1():
    return '<h1>Page 1</h1><p>This is the content of page 1.</p>'

@app.route('/page2')
def page2():
    return '<h1>Page 2</h1><p>This is the content of page 2.</p>'

@app.route('/page3')
def page3():
    return '<h1>Page 3</h1><p>This is the content of page 3.</p>'

@app.route('/page4')
def page4():
    return '<h1>Page 4</h1><p>This is the content of page 4.</p>'

@app.route('/about')
def authors():
    return template('about')

# Маршрут для статических файлов (CSS)
@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)