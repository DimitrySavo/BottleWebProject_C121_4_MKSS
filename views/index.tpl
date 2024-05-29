<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sample Page</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <header>
        <h1>Header</h1>
        <a href="/about">About us</a>
    </header>
    <div class="grid-container">
        <div class="grid-item item1" onclick="location.href='/isolatedSubgraphsDiameter'">
            <h2>Эмиль</h2>
            <p>This is the first box.</p>
        </div>
        <div class="grid-item item2" onclick="location.href='/concatenatedGraphs'">
            <h2>Клим</h2>
            <p>This is the second box.</p>
        </div>
        <div class="grid-item item3" onclick="location.href='/edgesCount'">
            <h2>Дима</h2>
            <p>This is the third box.</p>
        </div>
        <div class="grid-item item4" onclick="location.href='/vertexEdgesRights'">
            <h2>Влад</h2>
            <p>This is the fourth box.</p>
        </div>
    </div>
    <footer>
        <p>Footer</p>
    </footer>
</body>
</html>
