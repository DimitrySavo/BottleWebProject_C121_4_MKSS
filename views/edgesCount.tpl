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
                        <label for="countEdges">Количество вершин</label>
                        <input type="number" id="countEdges" name="countEdges" min="0" required>
                        <button type="button" class="submit-Check">Проверить</button>
                        <button type="button" class="submit-Degree">Степени вершин</button>
                    </form>
                </div>
            </div>
        </div>
        <div class="line"></div>
        <div class="bottom">
            <h1>Что такое граф</h1>
            <p>Граф — математическая абстракция реальной системы любой природы, объекты которой обладают парными связями. Граф как математический объект есть совокупность двух множеств — множества самих объектов, называемого множеством вершин, и множества их парных связей, называемого множеством рёбер. Элемент множества рёбер есть пара элементов множества вершин. </p>
            <h1>Степень вершины</h1>
            <p>Степень вершины - это число рёбер, которые выходят из вершины графа. Если у каждой вершины графа одинаковые степени, то граф считается правильным.</p>
            <h1>Правильный и неправильный граф</h1>
            <div class="image-with-text">
                <img src="/static/images/UnOrientedGraph.png">
                <h2> Пример неправильного графа с разными степенями вершин.</h2>
            </div>
            <div class="image-with-text">
                <img src="/static/images/RightUnOrientedGraph.png">
                <h2> Пример правильного графа с одинаковыми степенями вершин.</h2>
            </div>
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

        document.querySelector('.submit-Check').addEventListener('click', handleCheck);
        document.querySelector('.submit-Degree').addEventListener('click', handleDegree);
        
        function handleCheck(event) {
            event.preventDefault();
            alert('Посчитать число ребер');
            // Ваша логика для подсчета числа ребер
        }

        // Функция для обработки события "Посчитать число изолированных подграфов"
        function handleDegree(event) {
            event.preventDefault();
            alert('Посчитать число изолированных подграфов');
            // Ваша логика для подсчета числа изолированных подграфов
        }
    </script>
</body>
<footer>
    {{ !footer }}
</footer>
</html>
