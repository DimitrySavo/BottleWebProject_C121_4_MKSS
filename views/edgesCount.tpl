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
                    <div class="form-and-result-container">
                        <form id="matrix-form">
                            <h1>Матрица смежности 1</h1>
                            <label for="size">Размер графа:</label>
                            <input type="number" id="size" name="size" min="1" required>
                            <button type="button" onclick="generateMatrixOnPage('matrix-container', 'size')">Создать матрицу смежности</button>
                            <div id="matrix-container" class="matrix-container"></div>
                            <label for="countEdges">Количество вершин</label>
                            <input type="number" id="countEdges" name="countEdges" min="0" required>
                            <button type="button" class="submit-Check">Проверить</button>
                            <button type="button" class="submit-Degree">Степени вершин</button>
                        </form>
                        <span id="ResultCountFirst" class="hidden"></span>
                        <span id="ResultCountSecond" class="hidden"></span>
                        <span id="ResultRegularFirst" class="hidden"></span>
                        <span id="ResultRegularSecond" class="hidden"></span>
                    </div>
                    <form id="matrix-form2">
                        <h1>Матрица смежности 2</h1>
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
    <script src="/scripts/generateMatrixFun.js"></script>
    <script>
        function generateMatrixOnPage(id, sizeId) {
            const container = document.getElementById(id);
            container.innerHTML = '';
            const size = parseInt(document.getElementById(sizeId).value);
            console.log(size)
            console.log(id)
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

        document.querySelector('.submit-Check').addEventListener('click', handleCheck);
        document.querySelector('.submit-Degree').addEventListener('click', handleDegree);
        
        // Функция для обработки события "Проверить графы на правильность"
        function handleCheck(event) {
            event.preventDefault();
            alert('Посчитать число изолированных подграфов');

            const size1 = parseInt(document.getElementById('size').value);
            const size2 = parseInt(document.getElementById('size2').value);

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


            const edges2 = [];
            for (let i = 0; i < size2; i++) {
                for (let j = 0; j < size2; j++) {
                    const checkbox = document.querySelector(`input[name="matrix-container2-cell-${i}-${j}"]`);
                    if (checkbox && checkbox.checked) {
                        edges2.push([i, j]);
                    }
                }
            }

            const amountOfVertexes = parseInt(document.getElementById('countEdges').value);
            console.log(amountOfVertexes)

            fetch('/Create2Graph', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ size1,edges1,size2,edges2})
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

            fetch('/IsGraphOfNRegular',{
                method: 'POST',
                headers: {
                    'Content-Type' : 'application/json',
                },
                body: JSON.stringify({size1,edges1,size2,edges2,amountOfVertexes})
            })
            .then(response => response.json())
            .then(data =>{
                document.getElementById('ResultRegularFirst').classList.remove('hidden');
                document.getElementById('ResultRegularSecond').classList.remove('hidden');
                document.getElementById('ResultRegularFirst').textContent = `Граф 1: ${ data.is_first_regular}`
                document.getElementById('ResultRegularSecond').textContent = `Граф 2: ${data.is_second_regular}`
            })
        }

        // Функция для обработки события "Посчитать степени вершин"
        function handleDegree(event) {
            event.preventDefault();
            alert('Посчитать число ребер');
            
            const size1 = parseInt(document.getElementById('size').value);
            const size2 = parseInt(document.getElementById('size2').value);

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


            const edges2 = [];
            for (let i = 0; i < size2; i++) {
                for (let j = 0; j < size2; j++) {
                    const checkbox = document.querySelector(`input[name="matrix-container2-cell-${i}-${j}"]`);
                    if (checkbox && checkbox.checked) {
                        edges2.push([i, j]);
                    }
                }
            }

            fetch('/Create2Graph', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ size1,edges1,size2,edges2})
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

            fetch('/DegreesForGraph',{
                method: 'POST',
                headers: {
                    'Content-Type' : 'application/json',
                },
                body: JSON.stringify({size1,edges1,size2,edges2})
            })
            .then(response => response.json())
            .then(data => {
                let stringDegrees1 = ""
                let stringDegrees2 = ""

                for (let i = 0; i < data.degrees1.length; i++){
                    stringDegrees1 = stringDegrees1.concat(`${i + 1} = `, data.degrees1[i], ' ')
                    console.log(data.degrees1[i])
                }

                for (let i = 0; i < data.degrees2.length; i++){
                    stringDegrees2 = stringDegrees2.concat(`${i + 1} = `, data.degrees2[i], ' ')
                    console.log(data.degrees2[i])
                }

                console.log(stringDegrees1)
                console.log(stringDegrees2)

                document.getElementById('ResultCountFirst').classList.remove('hidden');
                document.getElementById('ResultCountSecond').classList.remove('hidden');
                document.getElementById('ResultCountFirst').textContent = `Число ребер в первом графе:\n ${stringDegrees1}`
                document.getElementById('ResultCountSecond').textContent = `Число ребер во втором графе:\n ${stringDegrees2}`
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
