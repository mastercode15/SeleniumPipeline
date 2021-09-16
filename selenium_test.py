from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def main():
    driver = webdriver.Chrome('/usr/bin/chromedriver')
    driver.get("https://www.python.org")
    print(driver.title)
    search_bar = driver.find_element_by_name("q")
    search_bar.clear()
    time.sleep(2)
    search_bar.send_keys("test")
    search_bar.send_keys(Keys.RETURN)
    time.sleep(5)
    result = driver.find_elements_by_xpath(
        "// p[contains(text(),'No results found.')]")
    print(driver.current_url)
    print('resultado:')
    print(result)
    if result == []:
        print('existe en la base de datos el tema')
        driver.close()
        return "exito"

    else:
        print('no existe en la base de datos el tema')
        driver.close()
        return "error"
