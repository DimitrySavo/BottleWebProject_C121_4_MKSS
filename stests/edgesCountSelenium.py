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
  
    driver.get("http://127.0.0.1:8080/edgesCount")
    time.sleep(1)

    # Ввод размера графа
    driver.find_element(By.ID, "size").send_keys("10")
    time.sleep(1)

    driver.find_element(By.ID, "size2").send_keys("10")
    time.sleep(1)

    driver.find_element(By.ID, "countEdges").send_keys("4")
    time.sleep(1)

    # Нажатие на кнопку создания матрицы
    generate_button = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/div/form/button[1]").click()
    time.sleep(0.1)


    generate_button2 = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/form/button").click()
    time.sleep(0.1)

    first_matrix_checkboxes = [
        "matrix-container-cell-0-0",
        "matrix-container-cell-1-1",
        "matrix-container-cell-2-2",
        "matrix-container-cell-3-3"
    ]

    for checbox_name in first_matrix_checkboxes:
        checkbox = driver.find_element(By.NAME, checbox_name)
        if not checkbox.is_selected():
            checkbox.click()
            time.sleep(0.1)


    second_matrix_checkboxes = [
        "matrix-container2-cell-0-0",
        "matrix-container2-cell-1-0",
        "matrix-container2-cell-2-0",
        "matrix-container2-cell-3-0"
    ]

    for checbox_name in second_matrix_checkboxes:
        checkbox = driver.find_element(By.NAME, checbox_name)
        if not checkbox.is_selected():
            checkbox.click()
            time.sleep(0.1)

    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/div/form/button[3]").click()
    time.sleep(4)
    driver.find_element(By.CLASS_NAME, "submit-Check").click()   


    first_graph_degrees = driver.find_element(By.ID, "ResultCountFirst").text
    second_graph_degrees = driver.find_element(By.ID, "ResultCountSecond").text

    print(f"result first: {first_graph_degrees}")
    print(f"result second: {second_graph_degrees}")

    time.sleep(2)

    right_matrix = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/div/span[3]/pre/code").text

    time.sleep(10)
    print(f"result matrixes:\n {right_matrix}")


except:
    driver.quit()
