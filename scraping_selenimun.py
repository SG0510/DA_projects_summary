import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_driver = '/Users/amberguan/Desktop/drivers/chromedriver'

# 1 landing page:
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
url = 'https://jobready123.com:2096'
driver.get(url)

# 2 enter the user name and password and RETURN

#TODO : remove it after test
username = 'customer_support@jobready123.com'
password = 'support_customer'

elem = driver.find_element(By.ID, "user")
elem.clear()
elem.send_keys(username)

elem = driver.find_element(By.ID, "pass")
elem.clear()
elem.send_keys(password)

elem.send_keys(Keys.RETURN)
# make sure Chorme does not close immediately

# synchronization point
# time.sleep(5.0)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
try:
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"quotamenu"))
    )
except:
    driver.quit()
# 3 scrap all the email subject from the mailbox

elist = driver.find_elements(By.XPATH,"//td[@class = 'subject']")

for e in elist:
    print(f'the text we have here {e.text}')
time.sleep(5.0)

# monitor the change
# {'com_1':{'2022-08-20':'book1'},{'2022-08-21':'book1'},{'2022-08-25':'book2'}}