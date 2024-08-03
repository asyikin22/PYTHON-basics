print('Selenium')

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# import time

#provide the path to your chrome driver executable
PATH = r"C:\Program Files (x86)\chromedriver.exe"

service = Service(PATH)

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver=webdriver.Chrome(service=service,options=options)

driver=webdriver.Chrome(service=service)

driver.get("https://automatetheboringstuff.com/")

print(f"Page title: {driver.title}")

#Locate an element by <p> element
single_paragraph = driver.find_element(By.TAG_NAME, 'p')
print(single_paragraph.text)

input('Press Enter to close the browser...')
# time.sleep(5)
driver.quit()

