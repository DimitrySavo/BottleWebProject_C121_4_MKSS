from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import time
import os

driver = webdriver.Firefox()

try:
    driver.get('http://127.0.0.1:8080/concatenatedGraphs')

    driver.maximize_window()

    size_input = driver.find_element(By.ID, "size1").send_keys("10")

    first_generate_button = driver.find_element(By.ID, "create-first-matrix").click()

    checkboxes = [
        "matrix-container-cell-1-3",
        "matrix-container-cell-3-4",
        "matrix-container-cell-2-2",
        "matrix-container-cell-2-9",
        "matrix-container-cell-3-3",
        "matrix-container-cell-2-3",
        "matrix-container-cell-4-4",
        "matrix-container-cell-4-7",
        "matrix-container-cell-1-9",
        "matrix-container-cell-1-1",
        "matrix-container-cell-0-9",
        "matrix-container-cell-0-6",
        "matrix-container-cell-0-7",
        "matrix-container-cell-0-0",
        "matrix-container-cell-0-3"
    ]

    for checkbox_id in checkboxes:
        checkbox = driver.find_element(By.NAME, checkbox_id)
        if not checkbox.is_selected():   
            checkbox.click()

    compliment_button = driver.find_element(By.ID, "complement-button").click()

    unproper_size_input2 = driver.find_element(By.ID, "size2").send_keys("1")

    second_generate_button = driver.find_element(By.ID, "create-second-matrix").click()

 

    unproper_union_button = driver.find_element(By.ID, "union-button").click()

    time.sleep(3)
    alert = Alert(driver)

    alert.accept()

    proper_size_input2 = driver.find_element(By.ID, "size2").send_keys("0")

    second_generate_button = driver.find_element(By.ID, "create-second-matrix").click()

    checkboxes = [
        "matrix-container2-cell-0-0",
        "matrix-container2-cell-0-1",
        "matrix-container2-cell-0-2",
        "matrix-container2-cell-0-3",
        "matrix-container2-cell-0-4",
        "matrix-container2-cell-0-5",
        "matrix-container2-cell-0-6",
        "matrix-container2-cell-0-7",
        "matrix-container2-cell-1-1",
        "matrix-container2-cell-2-4",
        "matrix-container2-cell-3-5",
        "matrix-container2-cell-4-7",
        "matrix-container2-cell-4-4",
        "matrix-container2-cell-3-3",
        "matrix-container2-cell-3-1",
        "matrix-container2-cell-2-8"
    ]

    for checkbox_id in checkboxes:
        checkbox = driver.find_element(By.NAME, checkbox_id)
        if not checkbox.is_selected():   
            checkbox.click()

    proper_union_button = driver.find_element(By.ID, "union-button").click()

    time.sleep(2)

    intersection_button = driver.find_element(By.ID, "intersection-button").click()

finally:
    time.sleep(10)
    driver.quit()