from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

driver = webdriver.Firefox()

try:
  
    driver.get("http://127.0.0.1:8080/vertexEdgesRights")

    # Ввод размера графа
    size_input = driver.find_element(By.ID, "size").send_keys("3")

    # Нажатие на кнопку создания матрицы
    generate_button = driver.find_element(By.XPATH, "//button[text()='Создать матрицу смежности']").click()

    # Ожидание появления матрицы
    #WebDriverWait(driver, 10).until(
    #    EC.presence_of_element_located((By.ID, "matrix-container"))
    #)

    # Установка значений в матрице смежности (предположим, что это checkboxes)
    checkboxes = [
        "matrix-container-cell-0-1",
        "matrix-container-cell-1-0",
        "matrix-container-cell-1-2",
        "matrix-container-cell-2-1",
    ]
    for checkbox_id in checkboxes:
        checkbox = driver.find_element(By.NAME, checkbox_id)
        if not checkbox.is_selected():
            checkbox.click()

    # Ввод начальной и конечной точки пути
    pathX_input = driver.find_element(By.ID, "pathX")
    pathX_input.send_keys("0")

    pathY_input = driver.find_element(By.ID, "pathY")
    pathY_input.send_keys("2")

    # Нажатие на кнопку проверки пути
    submit_button = driver.find_element(By.XPATH, "//button[text()='Проверить путь']")
    submit_button.click()

    # Вывод результата
    result_path = driver.find_element(By.ID, "ResultPath")
    result_linked = driver.find_element(By.ID, "ResultLinked")

    print("ResultPath:", result_path.text)
    print("ResultLinked:", result_linked.text)
    
    time.sleep(10)

finally:
    # Закрытие браузера
    driver.quit()
