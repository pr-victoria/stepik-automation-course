import math
from selenium import webdriver

def get_x():
  x = browser.find_element_by_id("input_value").text
  y = calc(x)
  return y

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 

link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

result = get_x()

input = browser.find_element_by_id("answer")
input.send_keys(result)

browser.execute_script("window.scrollBy(0, 150);")
cb = browser.find_element_by_id("robotCheckbox")
cb.click()

rb = browser.find_element_by_id("robotsRule")
rb.click()

browser.find_element_by_css_selector(".btn").click()
