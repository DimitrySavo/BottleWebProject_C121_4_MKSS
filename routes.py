from bottle import Bottle, run, request, static_file, template, response, route
import json

def index():
    return template('index', header = template('header.tpl'), footer = template('footer.tpl'))

# Страницы для перехода
def concatenatedGraphs():
    return template('concatenatedGraphs', header = template('header.tpl'), footer = template('footer.tpl'))

def edgesCount():
    return template('edgesCount', header = template('header.tpl'), footer = template('footer.tpl'))

def vertexEdgesRights():
    return template('vertexEdgesRights', header = template('header.tpl'), footer = template('footer.tpl'))


def isolatedSubgraphsDiameter():
    return template('isolatedSubgraphsDiameter', header = template('header.tpl'), footer = template('footer.tpl'))

def about():
    return template('about', header = template('header.tpl'), footer = template('footer.tpl'))

# Маршрут для статических файлов (CSS)
def server_static(filepath):
    return static_file(filepath, root='./static')

def server_scripts(filepath):
    return static_file(filepath, root='./scripts')