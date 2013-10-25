from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://clickingbad.nullism.com/")

# Amount you'd like to have in terms of cash and
# drugs to start the game
init_drugs = 10000
init_cash = 10000

# Number of cooks and sells to do in a row
num_cooks = 500
num_sells = 500

cook = driver.find_element_by_id('make_btn')
sell = driver.find_element_by_id('sell_btn')

driver.execute_script("gm.add_widgets(" + str(init_drugs) + ")")
driver.execute_script("gm.add_cash(" + str(init_cash) + ")")
while True:
    try:
        counter = 0
        driver.execute_script("window.scrollTo(0,0);")
        while counter < num_cooks:
            cook.click()
            counter+=1
        counter = 0
        driver.execute_script("window.scrollTo(0,0);")
        while counter < num_sells:
            sell.click()
            counter+=1
        time.sleep( 1 )
    except:
        time.sleep( 5 )
        pass
