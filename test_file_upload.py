from selenium import webdriver
import time
import os
def get_file():
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')
    return file_path
    
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
fname_input = browser.find_element_by_name("firstname")
fname_input.send_keys("FirstName")
lname_input = browser.find_element_by_name("lastname")
lname_input.send_keys("LastName")
email_input = browser.find_element_by_name("email")
email_input.send_keys("Email")
file = browser.find_element_by_id("file")
file.send_keys(get_file())
# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()
