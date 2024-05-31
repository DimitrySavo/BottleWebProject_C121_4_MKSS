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

    response.content_type = 'application/json'
    #отправка ответа
    return json.dumps({'image_base64': image_base64})

def edges_count():
    data = request.json
    size1 = data['size1']
    edges1= data['edges1']
    size2 = data['size2']
    edges2 = data['edges2']
    
    graph1 = MGraph(size1)
    graph2 = MGraph(size2)
    graph1.add_nodesAndEdges(size1, edges1)
    graph2.add_nodesAndEdges(size2, edges2)
                
    edges_count = graph1.count_edges() + graph2.count_edges()
    response.content_type = 'application/json'
    return json.dumps({'edgesCount': edges_count})

def isolated_subgraphs_count():
    data = request.json
    size = data['size']
    edges = data['edges']
    
    graph = MGraph(size)
    graph.add_nodesAndEdges(size, edges)  

    isolated_subgraphs_count = graph.count_isolated_subgraphs()
    response.content_type = 'application/json'
    return json.dumps({'isolatedSubgraphsCount': isolated_subgraphs_count})

def calculate_diameter():
    data = request.json
    size = data['size']
    edges = data['edges']
    
    graph = MGraph(size)
    graph.add_nodesAndEdges(size, edges)  

    diameter = graph.diameter()
    response.content_type = 'application/json'
    return json.dumps({'diameter': diameter})