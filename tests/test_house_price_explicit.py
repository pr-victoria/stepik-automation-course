import math
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


def get_x():
  x = browser.find_element_by_id("input_value").text
  y = calc(x)
  return y

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.wait = WebDriverWait(browser, 12)
browser.get(link)

browser.wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "10000"))
browser.find_element_by_css_selector(".btn").click()


result = get_x()

input = browser.find_element_by_id("answer")
input.send_keys(result)


browser.find_element_by_id("solve").click()
