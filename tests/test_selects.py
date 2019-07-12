import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select

def get_sum():
  num1 = browser.find_element_by_id("num1").text
  num2 = browser.find_element_by_id("num2").text
  return int(num1) + int(num2)

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

res = str(get_sum())
select = Select(browser.find_element_by_id("dropdown"))
select.select_by_value(res)

browser.find_element_by_css_selector(".btn").click()
