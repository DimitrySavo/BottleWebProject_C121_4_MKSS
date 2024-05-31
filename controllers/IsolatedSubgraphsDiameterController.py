from bottle import Bottle, run, request, static_file, template, response, route
import networkx as nx
import matplotlib.pyplot as plt
import io
import base64
from models.Graph import Graph as MGraph
import json


def create_graph():
    data = request.json #Получение данных с клиента
    size = data['size']
    edges = data['edges']

    G = nx.Graph()#Создание вспомогательного графа для вывода на экран
    corrected_edges = [(edge[0] + 1, edge[1] + 1) for edge in edges]
    G.add_nodes_from(range(1, size + 1))
    G.add_edges_from(corrected_edges)


    graph = MGraph(size)#Создание графа для математических подсчётов
    graph.add_nodesAndEdges(size,edges)
   

    is_connected = graph.is_connected()

    # Создание рисунка графа
    plt.figure(figsize=(5, 5))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=400, node_color='lightblue', font_size=10, font_color='black', font_weight='bold', edge_color='gray')
    #Конвертация картинки графа в base64
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    plt.close()

    matrix = nx.to_numpy_array(G).tolist()

    response.content_type = 'application/json'
    #отправка ответа
    return json.dumps({'is_connected': is_connected, 'matrix': matrix, 'image_base64': image_base64})