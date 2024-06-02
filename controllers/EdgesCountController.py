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
    graph.add_nodes_from(range(1, size))
    graph.add_edges_from( [(edge[0], edge[1]) for edge in edges])
   

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

def degrees_for_graphs():
    data = request.json
    size1 = data["size1"]
    edges1 = data["edges1"]
    size2 = data["size2"]
    edges2 = data["edges2"]

    graph1 = MGraph(size1)
    graph2 = MGraph(size2)

    graph1.add_nodesAndEdges(size1, edges1)
    graph2.add_nodesAndEdges(size2, edges2)

    degrees1 = graph1.degrees()
    degrees2 = graph2.degrees()

    return json.dumps({'degrees1' : degrees1, 'degrees2' : degrees2})

def is_regular_graphs_with_n():
    data = request.json
    size1 = data["size1"]
    edges1 = data["edges1"]
    size2 = data["size2"]
    edges2 = data["edges2"]
    amountOfVertexes = data["amountOfVertexes"]

    graph1 = MGraph(size1)
    graph2 = MGraph(size2)

    graph1.add_nodesAndEdges(size1, edges1)
    graph2.add_nodesAndEdges(size2, edges2)

    is_first_regular = graph1.is_regular(amountOfVertexes)
    is_second_regular = graph2.is_regular(amountOfVertexes)

    return json.dumps({'is_first_regular' : is_first_regular, 'is_second_regular' : is_second_regular})

