from bottle import Bottle, run, request, static_file, template, response, route
import networkx as nx
import matplotlib.pyplot as plt
import io
import base64
from models.Graph import Graph as MGraph
import json

def check_path():
    data = request.json #Получение данных с клиента
    size = data['size']
    edges = data['edges']
    pathX = data['pathX']
    pathY = data['pathY']


    graph = MGraph(size)#Создание графа для математических подсчётов
    graph.add_nodesAndEdges(size,edges)
   

    is_connected = graph.is_connected()
    is_path = graph.path(pathX - 1, pathY - 1)

    response.content_type = 'application/json'
    #отправка ответа
    return json.dumps({'is_connected': is_connected, 'is_path': is_path,})