<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sample Page</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body class="body">
    <header>
        {{ !header }}
    </header>
    <div class="grid-container">
        <div class="grid-item item1" onclick="location.href='/isolatedSubgraphsDiameter'">
            <h2>Рёбра графа</h2>
            <p>Страница может находить число ребер в 2 графах, число изолированных подграфов в первом графе и диаметр второго графа</p>
        </div>
        <div class="grid-item item2" onclick="location.href='/concatenatedGraphs'">
            <h2>Объединение графов</h2>
            <p>Страница может объединять 2 графа, искать пересечение двух графов и дополнять первый граф до полного графа</p>
        </div>
        <div class="grid-item item3" onclick="location.href='/edgesCount'">
            <h2>Правильные графы</h2>
            <p>Страница может считать число рёбер, выходящих из каждой вершины 2 графов (Степени вершин), находить все правильные графы</p>
        </div>
        <div class="grid-item item4" onclick="location.href='/vertexEdgesRights'">
            <h2>Пути в графе</h2>
            <p>Страница может проверять путь от X до Y в графе, а также определять является ли граф связным</p>
        </div>
    </div>
    <footer>
        {{ !footer }}
    </footer>
</body>
</html>
