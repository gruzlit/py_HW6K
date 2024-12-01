from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_03_shop():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    driver.find_element(By.CSS_SELECTOR, "[id = user-name]").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "[id = password]").send_keys("secret_sauce")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[type = submit]'))
    )

    driver.find_element(By.CSS_SELECTOR, "[type = submit]").click()

    driver.find_element(By.CSS_SELECTOR, "[id = add-to-cart-sauce-labs-backpack]").click()
    driver.find_element(By.CSS_SELECTOR, "[id = add-to-cart-sauce-labs-bolt-t-shirt]").click()
    driver.find_element(By.CSS_SELECTOR, "[id = add-to-cart-sauce-labs-onesie]").click()


    driver.find_element(By.CSS_SELECTOR, "[id = shopping_cart_container]").click()

    driver.find_element(By.CSS_SELECTOR, "[id = checkout]").click()

    driver.find_element(By.CSS_SELECTOR, "[id = first-name]").send_keys("Владимир")
    driver.find_element(By.CSS_SELECTOR, "[id = last-name]").send_keys("Ахалкаци")
    driver.find_element(By.CSS_SELECTOR, "[id = postal-code]").send_keys("647000")

    driver.find_element(By.CSS_SELECTOR, "[id = continue]").click()

    total = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text

    print(total)

    driver.find_element(By.CSS_SELECTOR, "[id = finish]").click()

    driver.quit()








