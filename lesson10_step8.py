from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element_by_id('book')
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
button.click()

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

answer = browser.find_element_by_id("answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
answer.click()
answer.send_keys(y)
button1 = browser.find_element_by_id('solve')
button1.click()

time.sleep(5)

browser.quit()

