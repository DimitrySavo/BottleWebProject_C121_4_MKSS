<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Graph Adjacency Matrix</title>
    <link rel="stylesheet" href="/static/styles.css">
    <link rel="stylesheet" href="/static/basePageStyle.css">
</head>
<header>
    {{ !header }}
</header>
<body>
    <div class="main-container">
        <div class="container-base-page">
            <div class="left zero-width" id="left-container">
                <div class="image-container hidden" id="image-container">
                    <img id="graph-image" alt="Graph Image">
                </div>
            </div>
            <div class="right full-width" id="right-container">
                <div class="container-base-page">
                    <form id="matrix-form">
                        <h1>Введите граф через матрицу смежности</h1>
                        <label for="size">Размер графа:</label>
                        <input type="number" id="size1" name="size1" min="1" required>
                        <button type="button" onclick="generateMatrixOnPage('matrix-container', 'size1')">Создать матрицу смежности</button>
                        <div id="matrix-container" class="matrix-container"></div>
                        <button type="button" class="submit-edgesCount">Посчитать число ребер</button>
                        <button type="button" class="submit-countIsolatedSubgraphs">Посчитать число изолированных подграфов</button>
                        <button type="button" class="submit-calculateDiameter">Посчитать диаметр графа</button>
                    </form>
                    <form id="matrix-form2">
                        <h1>Введите граф через матрицу смежности</h1>
                        <label for="size">Размер графа:</label>
                        <input type="number" id="size2" name="size2" min="1" required>
                        <button type="button" onclick="generateMatrixOnPage('matrix-container2', 'size2')">Создать матрицу смежности</button>
                        <div id="matrix-container2" class="matrix-container"></div>
                    </form>
                </div>
            </div>
        </div>
        <div class="line"></div>
        <div class="bottom">
            <h1>Граф</h1>
            <p>Графом G(V,E) называется совокупность двух множеств – непустого множества V (вершин) и множества E (ребер) – двухэлементных подмножеств множества V.</p>
            <img src="/static/images/Graph.png"></img>
            <h2>Неориентированный граф</h2>
            <p>Граф, ни одному ребру которого не присвоено направление, называется неориентированным графом или неорграфом.</p>
            <img src="/static/images/UnOrientedGraph.png"></img>
            <p>В общем случае графы обоих типов могут содержать и петли. Петля в обоих случаях не имеет ориентации: это ребро, инцидентное только одной вершине. В определении таких графов следует опустить условие u не равно v.</p>
            <p>Граф обычно изображается на плоскости в виде множества точек, соответствующих вершинам, и соединяющих их линий, соответствующих ребрам. Линия, изображающая ребро {u, v} или дугу (u, v), соединяет точки, изображающие вершины u, v, причем во втором случае стрелка обозначает направление от u к v.</p>
            <h2>Путь в неориентированном графе</h2>
            <p>Путь в графе — последовательность вершин, в которой каждая вершина соединена со следующей ребром. Из этого следует что проверить путь от X в Y значит пройтись по всем ребрам от X в Y и проверить существует ли между ними связь.</p>
            <h2>Связный граф</h2>
            <p>Граф называется связным, если для любых двух вершин существует путь, состоящий из рёбер, который соединяет эти вершины. В противном случае граф называется несвязным.</p>
            <h2>Число ребер в графе</h2>
            <p>Ребра могут быть направленными или ненаправленными. В неориентированном графе каждое ребро рассматривается как двустороннее соединение между двумя вершинами.</p>
            <p>Матрица смежности — это квадратная матрица, где элемент в строке i и столбце j равен 1, если существует ребро между вершинами i и j, и 0 в противном случае.</p>
            <p>Для неориентированного графа матрица смежности симметрична относительно главной диагонали.</p>
            <p>Для подсчета числа ребер в графе пройдите по всем элементам матрицы смежности и подсчитайте количество единиц выше главной диагонали (или ниже, но не в обеих частях, чтобы не учитывать ребра дважды). Это количество единиц и будет числом ребер в графе.</p>
            <h2>Число изолированных подграфов</h2>
            <p>Изолированный подграф (или компонент связности) — это подмножество вершин графа, в котором каждая пара вершин соединена путями, и который изолирован от остальных вершин графа.</p>
            <p>Чтобы определить число изолированных подграфов, необходимо понять, сколько отдельных "кластеров" или "компонент" существует в графе.</p>
            <p>Инициализируйте массив посещенных вершин. Начните обход графа (например, обход в глубину (DFS) или в ширину (BFS)) с каждой непосещенной вершины. Каждый новый обход, начатый с непосещенной вершины, означает новую компоненту связности. Подсчитайте количество таких обходов.</p>
            <h2>Диаметр графа</h2>
            <p>Диаметр графа — это максимальная длина кратчайшего пути между любыми двумя вершинами в графе. Кратчайший путь — это путь с наименьшим числом ребер между двумя вершинами.</p>
            <p>Для каждой вершины выполните поиск в ширину (BFS) или алгоритм Дейкстры (для взвешенных графов), чтобы найти кратчайшие пути до всех других вершин. Определите максимальное расстояние до любой другой вершины для каждой начальной вершины. Максимум среди этих максимальных расстояний и будет диаметром графа.</p>
        </div>
    </div>
    <script src="/scripts/generateMatrixFun.js"></script>
    <script>
        function generateMatrixOnPage(id, sizeId) {
            const container = document.getElementById(id);
            container.innerHTML = '';
            const size = parseInt(document.getElementById(sizeId).value);
            console.log(size)
            container.appendChild(generateMatrix(size, id));
        }

        function handleCheckboxChange(event) {
            const checkbox = event.target;
            const row = parseInt(checkbox.dataset.row);
            const col = parseInt(checkbox.dataset.col);
            let name = checkbox.name.split('-');
            name[name.length - 2] = col;
            name[name.length - 1] = row;
            const correspondingCheckbox = document.querySelector(`input[name="${name.toString().replace(/,/g, '-')}"]`);
            correspondingCheckbox.checked = checkbox.checked;
        }

        document.querySelector('.submit-edgesCount').addEventListener('click', handleEdgesCount);
        document.querySelector('.submit-countIsolatedSubgraphs').addEventListener('click', handleCountIsolatedSubgraphs);
        document.querySelector('.submit-calculateDiameter').addEventListener('click', handleCalculateDiameter);
        
        function handleEdgesCount(event) {
            event.preventDefault();

            const size1 = parseInt(document.getElementById('size1').value);
            const size2 = parseInt(document.getElementById('size2').value);
            size = size1;
            console.log(size1)

            if (isNaN(size1)) {
                alert("Please enter a valid number for the size of the graph.");
                return;
            }

            const edges1 = [];
            for (let i = 0; i < size1; i++) {
                for (let j = 0; j < size1; j++) {
                    const checkbox = document.querySelector(`input[name="matrix-container-cell-${i}-${j}"]`);
                    if (checkbox && checkbox.checked) {
                        edges1.push([i, j]);
                    }
                }
            }

            edges = edges1;

            const edges2 = [];
            for (let i = 0; i < size2; i++) {
                for (let j = 0; j < size2; j++) {
                    const checkbox = document.querySelector(`input[name="matrix-container2-cell-${i}-${j}"]`);
                    if (checkbox && checkbox.checked) {
                        edges2.push([i, j]);
                    }
                }
            }

            fetch('/CreateGraph', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ size, edges})
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('left-container').classList.replace('zero-width', 'half-width2');
                document.getElementById('right-container').classList.replace('full-width', 'half-width');
                document.getElementById('image-container').classList.remove('hidden');
                document.getElementById('graph-image').src = 'data:image/png;base64,' + data.image_base64;
            })
            .catch((error) => {
                console.error('Error:', error);
            });

            fetch('/EdgesCount', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ size1, size2, edges1, edges2})
            })
            .then(response => response.json())
            .then(data => {

                console.log(data.edgesCount)
                
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        }

        // Функция для обработки события "Посчитать число изолированных подграфов"
        function handleCountIsolatedSubgraphs(event) {
            event.preventDefault();

            const size = parseInt(document.getElementById('size1').value);

            if (isNaN(size)) {
                alert("Please enter a valid number for the size of the graph.");
                return;
            }

            const edges = [];
            for (let i = 0; i < size; i++) {
                for (let j = 0; j < size; j++) {
                    const checkbox = document.querySelector(`input[name="matrix-container-cell-${i}-${j}"]`);
                    if (checkbox && checkbox.checked) {
                        edges.push([i, j]);
                    }
                }
            }


            fetch('/CreateGraph', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ size, edges})
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('left-container').classList.replace('zero-width', 'half-width2');
                document.getElementById('right-container').classList.replace('full-width', 'half-width');
                document.getElementById('image-container').classList.remove('hidden');
                document.getElementById('graph-image').src = 'data:image/png;base64,' + data.image_base64;
            })
            .catch((error) => {
                console.error('Error:', error);
            });

            fetch('/IsolatedSubgraphsCount', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ size, edges})
            })
            .then(response => response.json())
            .then(data => {

                console.log(data.isolatedSubgraphsCount)
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        }

        // Функция для обработки события "Посчитать диаметр графа"
        function handleCalculateDiameter(event) {
            event.preventDefault();
            
            const size = parseInt(document.getElementById('size2').value);
            console.log(size)

            if (isNaN(size)) {
                alert("Please enter a valid number for the size of the graph.");
                return;
            }

            const edges = [];
            for (let i = 0; i < size; i++) {
                for (let j = 0; j < size; j++) {
                    const checkbox = document.querySelector(`input[name="matrix-container2-cell-${i}-${j}"]`);
                    if (checkbox && checkbox.checked) {
                        edges.push([i, j]);
                    }
                }
            }

            fetch('/CreateGraph', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ size, edges})
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('left-container').classList.replace('zero-width', 'half-width2');
                document.getElementById('right-container').classList.replace('full-width', 'half-width');
                document.getElementById('image-container').classList.remove('hidden');
                document.getElementById('graph-image').src = 'data:image/png;base64,' + data.image_base64;
            })
            .catch((error) => {
                console.error('Error:', error);
            });

            fetch('/CalculateDiameter', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({size, edges})
            })
            .then(response => response.json())
            .then(data => {
                console.log(data.diameter)
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        }

    </script>
</body>
<footer>
    {{ !footer }}
</footer>
</html>
