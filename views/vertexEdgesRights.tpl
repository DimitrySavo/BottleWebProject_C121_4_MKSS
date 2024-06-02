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
                <div class="container-base-page right-container-with-answers">
                    <form id="matrix-form">
                        <h1>Введите граф через матрицу смежности</h1>
                        <label for="size">Размер графа:</label>
                        <input type="number" id="size" name="size" min="1" required>
                        <button type="button" onclick="generateMatrixOnPage('matrix-container')">Создать матрицу смежности</button>
                        <div id="matrix-container" class="matrix-container"></div>
                        <label for="pathX">От:</label>
                        <input type="number" id="pathX" name="pathX" required>
                        <label for="pathY">До:</label>
                        <input type="number" id="pathY" name="pathY" required>
                        <button type="submit" class="submit-button">Проверить путь</button>
                    </form>
                    <span id="ResultPath" class="hidden"></span>
                    <span id="ResultLinked" class="hidden"></span>
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
        </div>
    </div>
    <script src="/scripts/generateMatrixFun.js"></script>
    <script>
        //Создание матрицы на странице
        function generateMatrixOnPage(id) {
            const container = document.getElementById(id);
            container.innerHTML = '';
            const size = parseInt(document.getElementById('size').value);
            container.appendChild(generateMatrix(size, id));
        }

        //Обработчик отзеркаливает действия пользователя
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

        //Обработчик получает данные и отправляет на сервер
        document.getElementById('matrix-form').addEventListener('submit', function(event) {
            event.preventDefault();

            const size = parseInt(document.getElementById('size').value);
            console.log(size)
            const pathX = parseInt(document.getElementById('pathX').value);
            const pathY = parseInt(document.getElementById('pathY').value);
            if (isNaN(size)) {
                alert("Please enter a valid number for the size of the graph.");
                return;
            }
            if (isNaN(pathX)){
                alert("Введите начало пути");
                return;
            }
            if (isNaN(pathY)){
                alert("Введите конец пути");
                return;
            }

            if (pathX > pathY){
                alert("Указан неверный путь ");
                return;
            }
            console.log(pathX)
            console.log(pathY)

            //Получение матрицы смежности графа
            const edges = [];
            console.log(edges);
            for (let i = 0; i < size; i++) {
                for (let j = 0; j < size; j++) {
                    const checkbox = document.querySelector(`input[name="matrix-container-cell-${i}-${j}"]`);
                    if (checkbox && checkbox.checked) {
                        edges.push([i, j]);
                    }
                }
            }

            //Создание и вывод графа на экран
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

            //ПРоверка пути графа
            fetch('/checkVertexEdgesRights', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ size, edges, pathX, pathY })
            })
            .then(response => response.json())
            .then(data => {
                console.log(data.matrix);
                console.log(data.is_connected);
                console.log(data.is_path);

                document.getElementById('ResultLinked').classList.remove('hidden');
                document.getElementById('ResultPath').classList.remove('hidden');
                document.getElementById('ResultPath').textContent = `Результат: ${data.is_path? "Путь существует":"Путь не существует"}`
                document.getElementById('ResultLinked').textContent = `Граф ${data.is_connected? "связный":"не связный"}`
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        });
    </script>
</body>
<footer>
    {{ !footer }}
</footer>
</html>
