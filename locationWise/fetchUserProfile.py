from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import random
import csv

driver = webdriver.Firefox()
with open("user-id.txt", 'r') as file:
	arr=file.readlines()
arr=[x.strip() for x in arr]
file.close()
 
f=open("user-links.txt", 'w')
try:
	f=open("user-data.csv", 'wb')
	writer=csv.writer(f, delimiter=',')
	writer.writerow(['UserName','NOP','Followers','Following', 'Name', 'Bio'])
	for i in arr:
		driver.implicitly_wait(random.randrange(15,20))
		driver.get("https://"+i)
		f.write( driver.find_element_by_xpath("html/body/span/section/main/div/div/article/header/div/a").get_attribute('href'))
		f.write("\n")
		driver.implicitly_wait(random.randrange(50,55))
		driver.find_element_by_xpath("html/body/span/section/main/div/div/article/header/div/a").click()
		driver.implicitly_wait(random.randrange(50,55))
		k=driver.find_element_by_xpath(".//*[@id='react-root']/section/main/article/header/div[2]").text
		k=[i.encode('utf-8') for i in k.split("\n")]
		writer.writerow(k)
finally:
	driver.quit()
