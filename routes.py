from bottle import Bottle, run, request, static_file, template, response, route
import json

def index():
    return template('index', header = template('header.tpl'), footer = template('footer.tpl'))

# Страницы для перехода
def concatenatedGraphs():
    return template('concatenatedGraphs', header = template('header.tpl'), footer = template('footer.tpl'))

def edgesCount():
    return template('edgesCount')

def vertexEdgesRights():
    return template('vertexEdgesRights')


def isolatedSubgraphsDiameter():
    return template('isolatedSubgraphsDiameter')

def about():
    return template('about')

# Маршрут для статических файлов (CSS)
def server_static(filepath):
    return static_file(filepath, root='./static')