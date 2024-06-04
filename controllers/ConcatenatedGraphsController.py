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
    plt.figure(figsize=(10, 5))
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

def create_united_graph(): #Функция объединения графов

    #Получаем данные из формы из json
    data = request.json
    size1 = data['size1']
    edges1 = data['edges1']
    size2 = data['size2']
    edges2 = data['edges2']

    #Создание графов
    graph1 = MGraph(size1)
    graph2 = MGraph(size2)
    graph1.add_edges_from(edges1)
    graph2.add_edges_from(edges2)

    united_graph = MGraph.union(graph1, graph2) #Получаем объединенный граф

    #Создаем граф для отрисовки на основе объединения графов
    u_g_for_drawing = nx.Graph()
    u_g_for_drawing.add_nodes_from(range(1, united_graph.size + 1))
    corrected_edges = [(edge[0] + 1, edge[1] + 1) for edge in united_graph.get_edges()]
    u_g_for_drawing.add_edges_from(corrected_edges)

    #Отрисовываем граф
    plt.figure(figsize=(10, 7))
    plt.title('Объединение графов')
    pos = nx.spring_layout(u_g_for_drawing)
    nx.draw(u_g_for_drawing, pos, with_labels=True, node_size=400, node_color='lightblue', 
    font_size=10, font_color='black', font_weight='bold', edge_color='gray')

    #Сохраняем картинку в формате base64
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    plt.close()

    response.content_type = 'application/json'
    return json.dumps({'image_base64': image_base64})

def create_intersection(): #Функция пересечения графов
    #Получаем данные из формы из json
    data = request.json
    size1 = data['size1']
    edges1 = data['edges1']
    size2 = data['size2']
    edges2 = data['edges2']
    
    #Создание графов
    graph1 = MGraph(size1)
    graph2 = MGraph(size2)
    graph1.add_edges_from(edges1)
    graph2.add_edges_from(edges2)

    intersection = MGraph.intersection(graph1, graph2) #Ищем пересечение

    #Создаем граф для отрисовки
    u_g_for_drawing = nx.Graph()
    corrected_edges = [(edge[0] + 1, edge[1] + 1) for edge in intersection.get_edges()]

    print(intersection.get_edges()) #Данные для логов
    print(intersection.size)
    u_g_for_drawing.add_nodes_from(range(1, intersection.size + 1))
    u_g_for_drawing.add_edges_from(corrected_edges)

    #Отрисовываем граф
    plt.figure(figsize=(10, 7))
    plt.title('Пересечение графов')
    pos = nx.spring_layout(u_g_for_drawing)
    nx.draw(u_g_for_drawing, pos, with_labels=True, node_size=400, node_color='lightblue', 
    font_size=10, font_color='black', font_weight='bold', edge_color='gray')
  
    #Сохраняем граф в формате base64
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    plt.close()

    response.content_type = 'application/json'
    return json.dumps({'image_base64': image_base64})

def make_full(): #Дополнение первого графа до полного
    #Получаем данные из json
    data = request.json
    size = data['size']
    edges = data['edges']
    #Создаем граф на основе данных из формы
    graph = MGraph(size)
    graph.add_edges_from(edges)

    full_graph = MGraph.complement(graph) #Ищем дополнение

    #Отладочные данные для логов
    print("Размер графа: " + str(size))
    print("Матрица графа: ")
    print(graph.matrix)
    print("Edges: ")
    print(edges)

    #Отрисовываем граф
    f_g_for_drawing = nx.Graph()
    corrected_edges = [(edge[0] + 1, edge[1] + 1) for edge in full_graph.get_edges()]
    
    f_g_for_drawing.add_nodes_from(range(1, full_graph.size + 1))
    f_g_for_drawing.add_edges_from(corrected_edges)

    plt.figure(figsize=(10, 7))
    plt.title('Дополнение первого графа до полного')
    pos = nx.spring_layout(f_g_for_drawing)
    nx.draw(f_g_for_drawing, pos, with_labels=True, node_size=400, node_color='lightblue', 
    font_size=10, font_color='black', font_weight='bold', edge_color='gray')


    #Сохраняем картинку в формате base64
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    plt.close()

    response.content_type = 'application/json'
    return json.dumps({'image_base64': image_base64})