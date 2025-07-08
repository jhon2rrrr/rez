from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")


price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
 
book_button = browser.find_element(By.ID, "book")
book_button.click()
    
    
x_element = browser.find_element(By.ID, "input_value")
x = int(x_element.text)
result = str(math.log(abs(12*math.sin(x))))
    
    
answer_field = browser.find_element(By.ID, "answer")
answer_field.send_keys(result)
    

submit_button = browser.find_element(By.ID, "solve")
submit_button.click()
    
    
time.sleep(10)
