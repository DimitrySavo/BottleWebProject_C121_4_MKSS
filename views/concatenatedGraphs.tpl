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
<header>
    {{ !header }}
</header>
<body>
    <div class="main-container">
        <div class="container-base-page">
            <div class="left half-width" id="left-container">
                <div class="image-container hidden" id="image-container">
                    <img id="graph-image" alt="Graph Image">
                </div>
            </div>

            <div>
                <div class="right full-width" id="right-container">
                    <div class="container-base-page">
                        <form id="matrix-form1">
                            <h1>Создать матрицу</h1>
                            <label class="margined-button" for="size">Размер графа:</label>
                            <input type="number" id="size1" name="size" min="1" required>
                            <button type="button" onclick="generateMatrixOnPage('matrix-container', 'size1')">Создать</button>
                            <span id="size1-error" class="error-message"></span>
                            <div id="matrix-container" class="matrix-container"></div>
                        </form>
                    </div>
                </div>

                    <div class="right full-width" id="right-container">
                        <div class="container-base-page">
                            <form id="matrix-form2">
                                <h1>Создать матрицу</h1>
                                <label  class="margined-button" for="size">Размер графа:</label>
                                <input type="number" id="size2" name="size" min="1" required>
                                <button type="button" onclick="generateMatrixOnPage('matrix-container2', 'size2')">Создать</button>
                                <span id="size2-error" class="error-message"></span>
                                <div id="matrix-container2" class="matrix-container"></div>
                            </form>
                        </div>
                        <div class="container-base-page">
                            <button id="union-button" type="button">Объединение</button>
                            <button id="intersection-button" class="margined-button" type="button">Пересечение</button>
                            <button id="complement-button" class="margined-button" type="button">Дополнение</button>                            
                        </div>  
                    </div>
            </div>
        </div>
    </div>
        <div class="line"></div>
        <div class="bottom">
            <h1>Граф</h1>
            <p>Графом G(V,E) называется совокупность двух множеств – непустого множества V (вершин) и множества E (ребер) – двухэлементных подмножеств множества V</p>
            <img src="/static/images/Graph.png"></img>
            <h2>Неориентированный граф</h1>
            <p>Граф, ни одному ребру которого не присвоено направление, называется неориентированным графом или неорграфом.</p>
            <div class="image-with-text">
                <img src="/static/images/UnOrientedGraph.png"></img>
                <p>В общем случае графы обоих типов могут содержать и петли. Петля в обоих случаях не имеет ориентации: это ребро, инцидентное только одной вершине. В определении таких графов следует опустить условие u не равно v. Граф обычно изображается на плоскости в виде множества точек, соответствующих вершинам, и соединяющих их линий, соответствующих ребрам. Линия, изображающая ребро {u, v} или дугу (u, v), соединяет точки, изображающие вершины u, v, причем во втором случае стрелка обозначает направление от u к v:</p>
            </div>
            <h2>Путь в неориентированном графе</h1>
            <p>Путь в графе — последовательность вершин, в которой каждая вершина соединена со следующей ребром. Из этого следует что проверить путь от X в Y значит пройтись по всем ребрам от X в Y и проверить существует ли между ними связь.</p>
            <h2>Связный граф</h1>
            <p>Граф называется связным, если для любых двух вершин существует путь, состоящий из рёбер, который соединяет эти вершины. В противном случае граф называется несвязным.</p>
             <h2>Пересечение графов </h2>
            <p>Переcечение графов - это операция, в результате которой создаётся новый граф, содержащий только те рёбра, которые присутствуют как в первом, так и во втором графе. Иными словами, это нахождение общих элементов между двумя графами.</p>
            <h2>Дополнение графа</h2>
            <p>Дополнение графа - это операция, в результате которой создаётся новый граф, содержащий рёбра, которые отсутствуют в исходном графе. В контексте задачи дополнение первого графа до полного предполагает создание графа, в котором отсутствуют все рёбра исходного графа, кроме петель (связей вершины с самой собой).</p>
            <h2>Объединение графов</h2>
            <p>Объединение графов - это операция, в результате которой создаётся новый граф, содержащий все рёбра, которые присутствуют хотя бы в одном из объединяемых графов.</p>
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

        document.getElementById('union-button').addEventListener('click', handleUnion);
        document.getElementById('intersection-button').addEventListener('click', handleIntersection);
        document.getElementById('complement-button').addEventListener('click', handleMakeFull);

        function handleUnion(event) {
            event.preventDefault();

            const size1 = parseInt(document.getElementById('size1').value);
            const size2 = parseInt(document.getElementById('size2').value);

            if (size1 != size2) {
                alert("Размеры матриц должны совпадать");
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

            const edges2 = [];
            for (let i = 0; i < size2; i++) {
                for (let j = 0; j < size2; j++) {
                    const checkbox = document.querySelector(`input[name="matrix-container2-cell-${i}-${j}"]`);
                    if (checkbox && checkbox.checked) {
                        edges2.push([i, j]);
                    }
                }
            }

            fetch('/CreateUnitedGraph', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ size1,edges1,size2,edges2})
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('image-container').classList.remove('hidden');
                document.getElementById('graph-image').src = 'data:image/png;base64,' + data.image_base64;
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        }

        function handleIntersection(event) {
            event.preventDefault();

            const size1 = parseInt(document.getElementById('size1').value);
            const size2 = parseInt(document.getElementById('size2').value);

            
            if (size1 != size2) {
                alert("Размеры матриц должны совпадать");
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

            const edges2 = [];
            for (let i = 0; i < size2; i++) {
                for (let j = 0; j < size2; j++) {
                    const checkbox = document.querySelector(`input[name="matrix-container2-cell-${i}-${j}"]`);
                    if (checkbox && checkbox.checked) {
                        edges2.push([i, j]);
                    }
                }
            }

            fetch('/CreateIntersection', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ size1,edges1,size2,edges2})
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('image-container').classList.remove('hidden');
                document.getElementById('graph-image').src = 'data:image/png;base64,' + data.image_base64;
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        }

        function handleMakeFull(event) {
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

            fetch('/MakeFirstFull', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ size,edges })
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('image-container').classList.remove('hidden');
                document.getElementById('graph-image').src = 'data:image/png;base64,' + data.image_base64;
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
