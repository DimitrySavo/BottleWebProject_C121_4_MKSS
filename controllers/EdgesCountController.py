from bottle import Bottle, run, request, static_file, template, response, route
import networkx as nx
import matplotlib.pyplot as plt
import io
import base64
from models.Graph import Graph as MGraph
import json


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

    graph1.save_base64_img(f"{size1}, {size2}, {edges1}, {edges2}")

    return json.dumps({'degrees1' : degrees1, 'degrees2' : degrees2})

def is_regular_graphs_with_n():
    data = request.json
    size1 = data["size1"]
    edges1 = data["edges1"]
    size2 = data["size2"]
    edges2 = data["edges2"]
    amountOfVertexes = data["amountOfVertexes"]

    graph1 = MGraph(amountOfVertexes)

    set_of_regular_graphs = graph1.is_regular(amountOfVertexes)

    graph1.save_base64_img(f"{size1}, {size2}, {edges1}, {edges2}")

    return json.dumps({'set_of_regular_graphs' : list(set_of_regular_graphs)})

