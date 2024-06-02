from bottle import Bottle, run, request, static_file, template, response
from routes import *
from controllers import ConcatenatedGraphsController, EdgesCountController, IsolatedSubgraphsDiameterController, vertexEdgesRightsController
from models.Graph import Graph as MGraph

app = Bottle()

app.route('/', 'GET', index)
app.route('/about', 'GET', about)
app.route('/concatenatedGraphs','GET', concatenatedGraphs)
app.route('/edgesCount','GET', edgesCount)
app.route('/vertexEdgesRights','GET', vertexEdgesRights)
app.route('/isolatedSubgraphsDiameter','GET', isolatedSubgraphsDiameter)
app.route('/static/<filepath:path>', 'GET', server_static)
app.route('/scripts/<filepath:path>', 'GET', server_scripts)
app.post('/checkVertexEdgesRights')(vertexEdgesRightsController.check_path)
app.post('/checkConcatenatedGraphs')(ConcatenatedGraphsController.create_graph)
app.post('/DegreesForGraph')(EdgesCountController.degrees_for_graphs)
app.post('/IsGraphOfNRegular')(EdgesCountController.is_regular_graphs_with_n)
app.post('/EdgesCount')(IsolatedSubgraphsDiameterController.edges_count)
app.post('/IsolatedSubgraphsCount')(IsolatedSubgraphsDiameterController.isolated_subgraphs_count)
app.post('/CalculateDiameter')(IsolatedSubgraphsDiameterController.calculate_diameter)
app.post('/CreateGraph')(IsolatedSubgraphsDiameterController.create_image_graph_from_client)
app.post('/Create2Graph')(IsolatedSubgraphsDiameterController.create_image_2graph_from_client)

if __name__ == "__main__":
    app.run()
