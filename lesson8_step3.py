import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

a = browser.find_element_by_css_selector('span#num1.nowrap')
a = a.text
b = browser.find_element_by_css_selector('span#num2.nowrap')
b = b.text

res = int(a) + int(b)
res = str(res)
select = Select(browser.find_element_by_id('dropdown'))

otvet = select.select_by_visible_text(res)

button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(5)

browser.quit()