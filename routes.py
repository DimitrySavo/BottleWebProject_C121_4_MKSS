from bottle import Bottle, run, request, static_file, template, response, route
import json

@route('/')
def index():
    return template('index')

# Страницы для перехода
@route('/page1')
def page1():
    return '<h1>Page 1</h1><p>This is the content of page 1.</p>'

@route('/page2')
def page2():
    return '<h1>Page 2</h1><p>This is the content of page 2.</p>'

@route('/page3')
def page3():
    return '<h1>Page 3</h1><p>This is the content of page 3.</p>'

@route('/page4')
def page4():
    return '<h1>Page 4</h1><p>This is the content of page 4.</p>'

@route('/about')
def authors():
    return template('about')

# Маршрут для статических файлов (CSS)
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')