from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager




def test_02_calc():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.maximize_window()




    driver.find_element(By.CSS_SELECTOR, "[id = delay]").clear()
    driver.find_element(By.CSS_SELECTOR, "[id = delay]").send_keys("45")

    driver.find_element(By.XPATH, ('//span[text()="7"]')).click()
    driver.find_element(By.XPATH, ('//span[text()="+"]')).click()
    driver.find_element(By.XPATH, ('//span[text()="8"]')).click()
    driver.find_element(By.XPATH, ('//span[text()="="]')).click()

    WebDriverWait(driver, 60).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
                 )
    res = driver.find_element(By.CLASS_NAME, "screen").text
    assert res == "15"
    print(res)

    driver.quit()