from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://clickingbad.nullism.com/")

num_cooks = 100
num_sells = 50

cook = driver.find_element_by_id('make_btn')
sell = driver.find_element_by_id('sell_btn')

while True:
    try:
        counter = 0
        driver.execute_script("window.scrollTo(0,0);")
        while counter < num_cooks:
            cook.click()
            counter+=1
        time.sleep( 1 )
        counter = 0
        driver.execute_script("window.scrollTo(0,0);")
        while counter < num_sells:
            sell.click()
            counter+=1
        time.sleep( 1 )
    except:
        time.sleep( 5 )
        pass
