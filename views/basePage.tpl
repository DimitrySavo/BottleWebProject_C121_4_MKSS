<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Graph Adjacency Matrix</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f0f0f0;
            color: #333;
        }
        .container {
            display: flex;
            justify-content: space-between;
            padding: 20px;
        }
        .left{
            width: 48%;
            background-color: #fff;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .right{
            width: 48%;
            background-color: #fff;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .image-container img {
            max-width: 100%;
            height: auto;
            border-radius: 10px;
        }
        .matrix-container {
            margin-top: 20px;
            max-height: 40vh;
            max-width: 40vw;
            overflow: auto;
            border: 1px solid #ddd;
            padding: 10px;
            background-color: #fafafa;
        }
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 10px;
            text-align: center;
            min-width: 40px;
        }
        th {
            background-color: #f9f9f9;
            position: sticky;
            top: 0; /* Фиксация заголовков таблицы сверху */
            z-index: 1;
        }
        .sticky-col {
            position: sticky;
            left: 0; /* Фиксация первой колонки */
            background-color: #f9f9f9;
            z-index: 2;
        }
        th.sticky-col {
            z-index: 3;
        }
        input[type="number"] {
            width: 100px;
            padding: 5px;
            margin-right: 10px;
        }
        button {
            padding: 10px 15px;
            margin-top: 10px;
            background-color: #007bff;
            color: white;
            border: none;
            cursor: pointer;
            border-radius: 5px;
        }
        button:hover {
            background-color: #0056b3;
        }
        .bottom {
            width: 100%;
            background-color: #fff;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="left">
            <div class="image-container">
                <img id="graph-image" alt="Graph Image">
            </div>
        </div>
        <div class="right">
            <div class="container">
                <form id="matrix-form">
                    <h1>Введите граф через матрицу смежности</h1>
                    <label for="size">Размер графа:</label>
                    <input type="number" id="size" name="size" min="1" required>
                    <button type="button" onclick="generateMatrix()">Создать матрицу смежности</button>
                    <div id="matrix-container" class="matrix-container"></div>
                    <button type="submit" class="submit-button">Отправить</button>
                </form>
            </div>
        </div>
    </div>
    <div class="bottom">
        <p>Текст.Текст.Текст.Текст.Текст.Текст.Текст.Текст.Текст.Текст.</p>
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

            fetch('/create_graph', {
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
                document.getElementById('graph-image').src = 'data:image/png;base64,' + data.image_base64;
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        });
    </script>
</body>
</html>
