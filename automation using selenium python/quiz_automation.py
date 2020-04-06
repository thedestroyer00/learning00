# BuzzBuddy(quiz) automation using python selenium : 

import random
import string
from time import sleep 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


length = random.randint(1,9)

def random_name(name_length):
    rand_str = string.ascii_letters
    return ''.join(random.choice(rand_str) for i in range(name_length))
    
name = random_name(length)
url= 'https://buzzbuddy.site/en/d/3115542'


# brower automation part 
browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://buzzbuddy.site/en/d/3115542')
sleep(3)


enter_name = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.NAME,'name')))
enter_name.click()
enter_name.send_keys(name)

start = browser.find_element_by_link_text("Let's Play Now")
start.click()

answers = browser.find_elements_by_css_selector('div.card.options.option.option-ans.correct')

for i in answers:
    sleep(2)
    i.click()

sleep(3)

button = browser.find_element_by_css_selector('button.btn.btn-green')
button.click()

print('\n\nAutomation is a success')
print('Your name is : ' + name)
score = browser.find_element_by_id('congo')
print('your score is ',score.text)

browser.quit()

