function generateMatrix(sizeName, cellIdentifier) {
    const size = sizeName;

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
                input.name = `${cellIdentifier}-cell-${i-1}-${j-1}`;
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
    return table;
}