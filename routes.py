from bottle import Bottle, run, request, static_file, template, response, route
import json

def index():
    return template('index')

# Страницы для перехода
def page1():
    return '<h1>Page 1</h1><p>This is the content of page 1.</p>'

def page2():
    return '<h1>Page 2</h1><p>This is the content of page 2.</p>'

def page3():
    return '<h1>Page 3</h1><p>This is the content of page 3.</p>'

def page4():
    return '<h1>Page 4</h1><p>This is the content of page 4.</p>'

def about():
    return template('about')

# Маршрут для статических файлов (CSS)
def server_static(filepath):
    return static_file(filepath, root='./static')