from bottle import Bottle, run, request, static_file, template, response
from routes import *
from controllers import ConcatenatedGraphsController, EdgesCountController, IsolatedSubgraphsDiameterController, vertexEdgesRightsController

app = Bottle()

app.route('/', 'GET', index)
app.route('/about', 'GET', about)
app.route('/concatenatedGraphs','GET', concatenatedGraphs)
app.route('/edgesCount','GET', edgesCount)
app.route('/vertexEdgesRights','GET', vertexEdgesRights)
app.route('/isolatedSubgraphsDiameter','GET', isolatedSubgraphsDiameter)
app.route('/static/<filepath:path>', 'GET', server_static)
app.route('/scripts/<filepath:path>', 'GET', server_scripts)
app.post('/checkVertexEdgesRights')(vertexEdgesRightsController.create_graph)
app.post('/checkConcatenatedGraphs')(ConcatenatedGraphsController.create_graph)
app.post('/EdgesCount')(EdgesCountController.create_graph)
app.post('/IsolatedSubgraphsDiameter')(IsolatedSubgraphsDiameterController.create_graph)
app.post('/EdgesCount')(IsolatedSubgraphsDiameterController.edges_count)
app.post('/IsolatedSubgraphsCount')(IsolatedSubgraphsDiameterController.isolated_subgraphs_count)
app.post('/CalculateDiameter')(IsolatedSubgraphsDiameterController.calculate_diameter)
app.post('/CreateGraph')(IsolatedSubgraphsDiameterController.create_graph)

if __name__ == "__main__":
    app.run()
