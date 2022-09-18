from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import msgWhats
import os
import sys
 
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get('https://www.linkedin.com/jobs/search?keywords=Desenvolvimento%20De%20Front-end&location=Brasil&locationId=&geoId=106057199&f_TPR=r86400&f_JT=F%2CT%2CI&f_E=2%2C3&position=1&pageNum=0')


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

list_titles = []
list_description = []
list_links = []

job_link = driver.find_elements(By.CSS_SELECTOR, '.base-card__full-link')


for link in job_link:
  if len(list_links) <= 2:
    list_links.append(link.get_attribute('href'))
for li in list_links:  
  driver.switch_to.new_window('tab')
  driver.get(li)
  time.sleep(2)
  title_job = driver.find_element(By.CLASS_NAME, 'top-card-layout__title').text
  description = driver.find_element(By.CLASS_NAME, 'show-more-less-html__markup').text
  list_titles.append(title_job)
  list_description.append(description)

job_title = pd.DataFrame(data=list_titles)
job_title.to_excel('TITULO.xlsx', index = False)

links = pd.DataFrame(data=list_links)
links.to_excel('LINKS.xlsx', index = False)

description_job = pd.DataFrame(data=list_description)
description_job.to_excel('DESCRICAO.xlsx', index = False)

driver.quit()
msgWhats.sendMessageWhatsApp()

for i in range(10, 0, -1):
    print(f'Recomecando em {i}')
    time.sleep(1)
restart_program()