import time
from selenium import webdriver


driver = webdriver.Chrome()

def get_auth_yandex(login: str, password:str):

    driver.get("https://passport.yandex.ru/auth/")
    time.sleep(2)

    textarea = driver.find_element_by_id("passp-field-login")
    textarea.send_keys(login)
    time.sleep(2)

    submit_button = driver.find_element_by_id("passp:sign-in")

    submit_button.click()
    time.sleep(2)

    textarea = driver.find_element_by_id("passp-field-passwd")
    textarea.send_keys(password)
    time.sleep(2)

    submit_button = driver.find_element_by_id("passp:sign-in")

    submit_button.click()
    time.sleep(2)

    driver.quit()

get_auth_yandex('Vasya1990', '*******')