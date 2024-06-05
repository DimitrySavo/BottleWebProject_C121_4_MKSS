from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Инициализация драйвера 
driver = webdriver.Chrome()

try:
    # Открытие локальной веб-страницы
    driver.get('http://127.0.0.1:8080/concatenatedGraphs')

    # Разворачивание окна браузера
    driver.maximize_window()

    # Генерация первой матрицы размером 5
    driver.find_element(By.ID, "size1").send_keys("5")
    driver.find_element(By.ID, "create-first-matrix").click()
    
    # Ожидание генерации матрицы
    time.sleep(1)

    # Выбор некоторых чекбоксов в первой матрице
    checkboxes1 = [
        "matrix-matrix-container1-0-1",
        "matrix-matrix-container1-1-2",
        "matrix-matrix-container1-2-3",
        "matrix-matrix-container1-3-4",
        "matrix-matrix-container1-4-0"
    ]

    for checkbox_id in checkboxes1:
        checkbox = driver.find_element(By.NAME, checkbox_id)
        if not checkbox.is_selected():
            checkbox.click()

    # Подсчет числа рёбер
    driver.find_element(By.ID, "edges-count-button").click()
    time.sleep(1)
    edges_count_result = driver.find_element(By.ID, "edgesCountResult").text
    print(f"Результат подсчета рёбер: {edges_count_result}")

    # Подсчет числа изолированных подграфов
    driver.find_element(By.ID, "isolated-subgraphs-button").click()
    time.sleep(1)
    isolated_subgraphs_result = driver.find_element(By.ID, "isolatedSubgraphsResult").text
    print(f"Результат подсчета изолированных подграфов: {isolated_subgraphs_result}")

    # Вычисление диаметра графа
    driver.find_element(By.ID, "diameter-button").click()
    time.sleep(1)
    diameter_result = driver.find_element(By.ID, "diameterResult").text
    print(f"Результат вычисления диаметра: {diameter_result}")

    # Генерация второй матрицы размером 5
    driver.find_element(By.ID, "size2").send_keys("5")
    driver.find_element(By.ID, "create-second-matrix").click()
    
    # Ожидание генерации матрицы
    time.sleep(1)

    # Выбор некоторых чекбоксов во второй матрице
    checkboxes2 = [
        "matrix-matrix-container2-0-1",
        "matrix-matrix-container2-1-2",
        "matrix-matrix-container2-2-3",
        "matrix-matrix-container2-3-4",
        "matrix-matrix-container2-4-0"
    ]

    for checkbox_id in checkboxes2:
        checkbox = driver.find_element(By.NAME, checkbox_id)
        if not checkbox.is_selected():
            checkbox.click()

    # Подсчет числа рёбер во второй матрице
    driver.find_element(By.ID, "edges-count-button").click()
    time.sleep(1)
    edges_count_result_2 = driver.find_element(By.ID, "edgesCountResult").text
    print(f"Результат подсчета рёбер (вторая матрица): {edges_count_result_2}")

    # Подсчет числа изолированных подграфов во второй матрице
    driver.find_element(By.ID, "isolated-subgraphs-button").click()
    time.sleep(1)
    isolated_subgraphs_result_2 = driver.find_element(By.ID, "isolatedSubgraphsResult").text
    print(f"Результат подсчета изолированных подграфов (вторая матрица): {isolated_subgraphs_result_2}")

    # Вычисление диаметра графа во второй матрице
    driver.find_element(By.ID, "diameter-button").click()
    time.sleep(1)
    diameter_result_2 = driver.find_element(By.ID, "diameterResult").text
    print(f"Результат вычисления диаметра (вторая матрица): {diameter_result_2}")

finally:
    # Пауза для просмотра результатов перед закрытием браузера
    time.sleep(10)
    # Закрытие браузера
    driver.quit()
