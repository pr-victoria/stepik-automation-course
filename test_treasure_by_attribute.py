import math
from selenium import webdriver

def get_x():
  image = browser.find_element_by_id("treasure")
  x = image.get_attribute("valuex")
  y = calc(x)
  return y

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

result = get_x()



input = browser.find_element_by_id("answer")
input.send_keys(result)

cb = browser.find_element_by_id("robotCheckbox")
cb.click()

rb = browser.find_element_by_id("robotsRule")
rb.click()

browser.find_element_by_css_selector(".btn").click()
