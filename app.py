from bottle import Bottle, run, request, static_file, template, response
import networkx as nx
import matplotlib.pyplot as plt
import io
import base64
from routes import *

app = Bottle()

app.route('/', 'GET', index)
app.route('/about', 'GET', about)
app.route('/concatenatedGraphs','GET', concatenatedGraphs)
app.route('/edgesCount','GET', edgesCount)
app.route('/vertexEdgesRights','GET', vertexEdgesRights)
app.route('/isolatedSubgraphsDiameter','GET', isolatedSubgraphsDiameter)
app.route('/static/<filepath:path>', 'GET', server_static)

@app.post('/create_graph')
def create_graph():
    data = request.json
    size = data['size']
    edges = data['edges']

    G = nx.Graph()
    G.add_nodes_from(range(1, size + 1))
    
    corrected_edges = [(edge[0] + 1, edge[1] + 1) for edge in edges]

    G.add_edges_from(corrected_edges)

    is_connected = nx.is_connected(G)

    # Рисуем граф
    plt.figure(figsize=(8, 8))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=400, node_color='lightblue', font_size=10, font_color='black', font_weight='bold', edge_color='gray')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    plt.close()

    matrix = nx.to_numpy_array(G).tolist()

    response.content_type = 'application/json'
    return json.dumps({'is_connected': is_connected, 'matrix': matrix, 'image_base64': image_base64})


if __name__ == "__main__":
    app.run()
