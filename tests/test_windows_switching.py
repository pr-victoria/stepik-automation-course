import math
from selenium import webdriver

def get_x():
  x = browser.find_element_by_id("input_value").text
  y = calc(x)
  return y

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
cur_win = browser.window_handles[0]
browser.find_element_by_css_selector(".btn").click()
next_win = browser.window_handles[1]
browser.switch_to.window(next_win)

result = get_x()

input = browser.find_element_by_id("answer")
input.send_keys(result)


browser.find_element_by_css_selector(".btn").click()
