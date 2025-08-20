from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    # browser.implicitly_wait(12)
    browser.get('http://suninjuly.github.io/explicit_wait2.html')


    text = WebDriverWait(browser, 12).until(
       EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
    # new_window = browser.window_handles[1]
    # browser.switch_to.window(new_window)

    


    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    # x = x_element.get_attribute('valuex')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.NAME, "text")
    input1.send_keys(y)
 

    button = browser.find_element(By.ID, "solve")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()