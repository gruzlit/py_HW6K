from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





def test_01_form():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.maximize_window()


    first_name = driver.find_element(By.CSS_SELECTOR, "[name = first-name]")
    first_name.send_keys("Иван")

    last_name = driver.find_element(By.CSS_SELECTOR, "[name = last-name]")
    last_name.send_keys("Петров")

    address = driver.find_element(By.CSS_SELECTOR, "[name = address]")
    address.send_keys("Ленина, 55-3")

    email = driver.find_element(By.CSS_SELECTOR, "[name = e-mail]")
    email.send_keys("test@skypro.com")

    phone_number = driver.find_element(By.CSS_SELECTOR, "[name = phone]")
    phone_number.send_keys("+7985899998787")

    zip_code= driver.find_element(By.CSS_SELECTOR, "[name = zip-code]")
    zip_code.send_keys("")

    city = driver.find_element(By.CSS_SELECTOR, "[name = city]")
    city.send_keys("Москва")

    country = driver.find_element(By.CSS_SELECTOR, "[name = country ]")
    country.send_keys("Россия")

    job_position = driver.find_element(By.CSS_SELECTOR, "[name = job-position]")
    job_position.send_keys("QA")

    company = driver.find_element(By.CSS_SELECTOR, "[name = company]")
    company.send_keys("SkyPro")

    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3"))
    )


    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3").click()

    color_form = driver.find_element(By.CSS_SELECTOR, "[id = zip-code]").value_of_css_property("color")

    print(color_form)
    assert color_form == "rgba(132, 32, 41, 1)"

    elements = ["first-name", "last-name", "address", "city", "country", "e-mail", "phone", "job-position", "company"]
    for i in elements:
        color_form2 = driver.find_element(By.CSS_SELECTOR, "[id=%s]" % i).value_of_css_property("color")
        
    assert color_form2 == "rgba(15, 81, 50, 1)"