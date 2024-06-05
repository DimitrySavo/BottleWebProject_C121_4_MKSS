<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Graph Adjacency Matrix</title>
    <link rel="stylesheet" href="/static/styles.css">
    <link rel="stylesheet" href="/static/basePageStyle.css">
    <style>
        .error-message {
            color: red;
            font-size: 0.9em;
            margin-left: 10px;
        }
    </style>
</head>
<body>
    <header>
        {{ !header }}
    </header>
    <div class="main-container">
        <div class="container-base-page">
            <div class="left zero-width" id="left-container">
                <div class="image-container hidden" id="image-container">
                    <img id="graph-image" alt="Graph Image">
                </div>
            </div>
            <div class="right full-width" id="right-container">
                <div class="container-base-page right-container-with-answer">
                    <form id="matrix-form1">
                        <h1>Введите граф через матрицу смежности</h1>
                        <label class="margined-button" for="size1">Размер графа:</label>
                        <input type="number" id="size1" name="size1" min="1" required>
                        <button type="button" id="create-first-matrix" onclick="generateMatrixOnPage('matrix-container1', 'size1')">Создать матрицу смежности</button>
                        <span id="size1-error" class="error-message"></span>
                        <div id="matrix-container1" class="matrix-container"></div>
                        <button type="button" class="submit-edgesCount" id="edges-count-button">Посчитать число ребер</button>
                        <button type="button" class="submit-countIsolatedSubgraphs" id="isolated-subgraphs-button">Посчитать число изолированных подграфов</button>
                        <button type="button" class="submit-calculateDiameter" id="diameter-button">Посчитать диаметр графа</button>
                    </form>
                    <form id="matrix-form2">
                        <h1>Введите граф через матрицу смежности</h1>
                        <label class="margined-button" for="size2">Размер графа:</label>
                        <input type="number" id="size2" name="size2" min="1" required>
                        <button type="button" id="create-second-matrix" onclick="generateMatrixOnPage('matrix-container2', 'size2')">Создать матрицу смежности</button>
                        <span id="size2-error" class="error-message"></span>
                        <div id="matrix-container2" class="matrix-container"></div>
                    </form>
                    <div id="results" class="results-container"> <!-- Добавлен контейнер для результатов -->
                        <p id="edgesCountResult"></p> <!-- Параграф для вывода числа ребер -->
                        <p></p>
                        <p id="isolatedSubgraphsResult"></p> <!-- Параграф для вывода числа изолированных подграфов -->
                        <p></p>
                        <p id="diameterResult"></p> <!-- Параграф для вывода диаметра графа -->
                    </div>
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
            <div class="image-with-text">
                <img src="/static/images/UnOrientedGraph.png"></img>
                <p>В общем случае графы обоих типов могут содержать и петли. Петля в обоих случаях не имеет ориентации: это ребро, инцидентное только одной вершине. В определении таких графов следует опустить условие u не равно v. Граф обычно изображается на плоскости в виде множества точек, соответствующих вершинам, и соединяющих их линий, соответствующих ребрам. Линия, изображающая ребро {u, v} или дугу (u, v), соединяет точки, изображающие вершины u, v, причем во втором случае стрелка обозначает направление от u к v:</p>
            </div>
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
            const size = parseInt(document.getElementById(sizeId).value);
            const errorElement = document.getElementById(`${sizeId}-error`);

            if (isNaN(size) || size < 1 || size > 10) {
                errorElement.textContent = "Введите корректный размер графа (от 1 до 10).";
                return;
            }

            errorElement.textContent = '';
            const container = document.getElementById(id);
            container.innerHTML = '';
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

        document.getElementById('edges-count-button').addEventListener('click', handleEdgesCount);
        document.getElementById('isolated-subgraphs-button').addEventListener('click', handleIsolatedSubgraphsCount);
        document.getElementById('diameter-button').addEventListener('click', handleDiameterCalculation);

        async function handleEdgesCount() {
            const matrix = readMatrixFromPage('matrix-container1');
            if (matrix) {
                const response = await fetch('/calculate-edges', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(matrix),
                });

                if (response.ok) {
                    const result = await response.json();
                    document.getElementById('edgesCountResult').textContent = `Число рёбер: ${result.edgesCount}`;
                }
            }
        }

        async function handleIsolatedSubgraphsCount() {
            const matrix = readMatrixFromPage('matrix-container1');
            if (matrix) {
                const response = await fetch('/calculate-isolated-subgraphs', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(matrix),
                });

                if (response.ok) {
                    const result = await response.json();
                    document.getElementById('isolatedSubgraphsResult').textContent = `Число изолированных подграфов: ${result.isolatedSubgraphsCount}`;
                }
            }
        }

        async function handleDiameterCalculation() {
            const matrix = readMatrixFromPage('matrix-container1');
            if (matrix) {
                const response = await fetch('/calculate-diameter', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(matrix),
                });

                if (response.ok) {
                    const result = await response.json();
                    document.getElementById('diameterResult').textContent = `Диаметр графа: ${result.diameter}`;
                }
            }
        }

        function generateMatrix(size, id) {
            const table = document.createElement('table');
            for (let i = 0; i < size; i++) {
                const row = document.createElement('tr');
                for (let j = 0; j < size; j++) {
                    const cell = document.createElement('td');
                    const checkbox = document.createElement('input');
                    checkbox.type = 'checkbox';
                    checkbox.name = `matrix-${id}-${i}-${j}`;
                    checkbox.dataset.row = i;
                    checkbox.dataset.col = j;
                    if (i !== j) {
                        checkbox.addEventListener('change', handleCheckboxChange);
                    }
                    cell.appendChild(checkbox);
                    row.appendChild(cell);
                }
                table.appendChild(row);
            }
            return table;
        }

        function readMatrixFromPage(containerId) {
            const container = document.getElementById(containerId);
            if (!container) return null;

            const checkboxes = container.querySelectorAll('input[type="checkbox"]');
            if (!checkboxes.length) return null;

            const size = Math.sqrt(checkboxes.length);
            const matrix = [];

            for (let i = 0; i < size; i++) {
                matrix.push([]);
                for (let j = 0; j < size; j++) {
                    const checkbox = container.querySelector(`input[name="matrix-${containerId}-${i}-${j}"]`);
                    matrix[i].push(checkbox.checked ? 1 : 0);
                }
            }

            return matrix;
        }
    </script>
</body>
</html>
