from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Инициализация драйвера 
driver = webdriver.Chrome()

try:
    # Открытие локальной веб-страницы
    driver.get('http://127.0.0.1:8080/isolatedSubgraphsDiameter')

    # Разворачивание окна браузера
    driver.maximize_window()

    # Генерация первой матрицы размером 5
    driver.find_element(By.ID, "size1").send_keys("5")
    driver.find_element(By.ID, "create-first-matrix").click()

    # Выбор некоторых чекбоксов в первой матрице
    checkboxes1 = [
        "matrix-container1-cell-0-1",
        "matrix-container1-cell-1-2",
        "matrix-container1-cell-2-3",
        "matrix-container1-cell-3-4",
        "matrix-container1-cell-4-0"
    ]

    for checkbox_id in checkboxes1:
        checkbox = driver.find_element(By.NAME, checkbox_id)
        if not checkbox.is_selected():
            checkbox.click()

    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/form[1]/button[3]").click()
   
    driver.find_element(By.ID, "size2").send_keys("5")
    driver.find_element(By.ID, "create-second-matrix").click()
    
    # Ожидание генерации матрицы
    time.sleep(1)

    # Выбор некоторых чекбоксов во второй матрице
    checkboxes2 = [
        "matrix-container2-cell-0-1",
        "matrix-container2-cell-1-2",
        "matrix-container2-cell-2-3",
        "matrix-container2-cell-3-4",
        "matrix-container2-cell-4-0"
    ]

    for checkbox_id in checkboxes2:
        checkbox = driver.find_element(By.NAME, checkbox_id)
        if not checkbox.is_selected():
            checkbox.click()

    # Подсчет числа рёбер во второй матрице
    driver.find_element(By.ID, "edges-count-button").click()
    
    # Подсчет числа изолированных подграфов во второй матрице
    driver.find_element(By.ID, "isolated-subgraphs-button").click()
    
    # Вычисление диаметра графа во второй матрице
    driver.find_element(By.ID, "diameter-button").click()
   
finally:
    # Пауза для просмотра результатов перед закрытием браузера
    time.sleep(10)
    # Закрытие браузера
    driver.quit()
