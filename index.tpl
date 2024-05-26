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
    </header>
    <div class="grid-container">
        <div class="grid-item item1" onclick="location.href='/page1'">
            <h2>Box 1</h2>
            <p>This is the first box.</p>
        </div>
        <div class="grid-item item2" onclick="location.href='/page2'">
            <h2>Box 2</h2>
            <p>This is the second box.</p>
        </div>
        <div class="grid-item item3" onclick="location.href='/page3'">
            <h2>Box 3</h2>
            <p>This is the third box.</p>
        </div>
        <div class="grid-item item4" onclick="location.href='/page4'">
            <h2>Box 4</h2>
            <p>This is the fourth box.</p>
        </div>
    </div>
    <footer>
        <p>Footer</p>
    </footer>
</body>
</html>
