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
                        <input type="number" id="size" name="size" min="1" required>
                        <button type="button" onclick="generateMatrix()">Создать матрицу смежности</button>
                        <div id="matrix-container" class="matrix-container"></div>
                        <label for="pathX">От:</label>
                        <input type="number" id="pathX" name="pathX" min="0" required>
                        <label for="pathY">До:</label>
                        <input type="number" id="pathY" name="pathY" min="0" required>
                        <button type="submit" class="submit-button">Проверить путь</button>
                    </form>
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

    <script>
        function generateMatrix() {
            const size = parseInt(document.getElementById('size').value);
            if (isNaN(size)) {
                alert("Please enter a valid number for the size of the graph.");
                return;
            }
            const container = document.getElementById('matrix-container');
            container.innerHTML = '';

            const table = document.createElement('table');
            table.style.minWidth = (size + 1) * 50 + 'px'; // Установка минимальной ширины таблицы
            for (let i = 0; i <= size; i++) {
                const row = document.createElement('tr');
                for (let j = 0; j <= size; j++) {
                    const cell = document.createElement(i === 0 || j === 0 ? 'th' : 'td');
                    if (i === 0 && j > 0) {
                        cell.innerText = j;
                        cell.classList.add('sticky-header');
                    } else if (j === 0 && i > 0) {
                        cell.innerText = i;
                        cell.classList.add('sticky-col');
                    } else if (i > 0 && j > 0) {
                        const input = document.createElement('input');
                        input.type = 'checkbox';
                        input.name = `cell-${i-1}-${j-1}`;
                        input.dataset.row = i - 1;
                        input.dataset.col = j - 1;
                        input.addEventListener('change', handleCheckboxChange);
                        cell.appendChild(input);
                    }
                    if (i === 0 || j === 0) {
                        cell.classList.add('sticky-col');
                    }
                    row.appendChild(cell);
                }
                table.appendChild(row);
            }
            container.appendChild(table);
        }

        function handleCheckboxChange(event) {
            const checkbox = event.target;
            const row = parseInt(checkbox.dataset.row);
            const col = parseInt(checkbox.dataset.col);
            const correspondingCheckbox = document.querySelector(`input[name="cell-${col}-${row}"]`);
            correspondingCheckbox.checked = checkbox.checked;
        }

        document.getElementById('matrix-form').addEventListener('submit', function(event) {
            event.preventDefault();

            const size = parseInt(document.getElementById('size').value);
            if (isNaN(size)) {
                alert("Please enter a valid number for the size of the graph.");
                return;
            }

            const edges = [];
            for (let i = 0; i < size; i++) {
                for (let j = 0; j < size; j++) {
                    const checkbox = document.querySelector(`input[name="cell-${i}-${j}"]`);
                    if (checkbox && checkbox.checked) {
                        edges.push([i, j]);
                    }
                }
            }

            fetch('/checkConcatenatedGraphs', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ size, edges }),
            })
            .then(response => response.json())
            .then(data => {
                //alert(`Graph created! Check the console for the adjacency matrix.\nIs Connected: ${data.is_connected}`);
                console.log(data.matrix);
                console.log(data.is_connected);
                // Обновляем изображение графа
                
                document.getElementById('left-container').classList.replace('zero-width', 'half-width2');
                document.getElementById('right-container').classList.replace('full-width', 'half-width');
                document.getElementById('image-container').classList.remove('hidden');
                document.getElementById('graph-image').src = 'data:image/png;base64,' + data.image_base64;
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
