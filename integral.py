from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import csv

options = webdriver.EdgeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Edge(options=options)
driver.get("https://coinmarketcap.com/historical/20230825/")

'''
# Scroll down the page in small steps to load more data
SCROLL_PAUSE_TIME = 1
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    for i in range(10):
        driver.execute_script(f"window.scrollBy(0, {last_height/10});")
        time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Get all the elements
Name = driver.find_elements(By.CLASS_NAME, "cmc-table__column-name--name.cmc-link")
Symbol = driver.find_elements(By.XPATH,"//td[@class='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__symbol']/div")
MarketCap = driver.find_elements(By.XPATH,"//td[@class='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__market-cap']/div")
Price = driver.find_elements(By.XPATH,"//td[@class='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price']/div")
CirculatingSupply= driver.find_elements(By.XPATH,"//td[@class='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__circulating-supply']/div")
Volume =  driver.find_elements(By.CLASS_NAME,"cmc-link")

# Write data to CSV file
with open('output.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Rank" , "Name", "Symbol", "MarketCap", "Price", "CirculatingSupply", "Volume"])
    for i in range(len(Name)):
        writer.writerow([i , Name[i].text, Symbol[i].text, MarketCap[i].text, Price[i].text, CirculatingSupply[i].text, Volume[i].text])

driver.quit()
'''

Names = ["bitcoin", "ethereum", "tether"]

for name in Names:
    driver.get(f"https://coinmarketcap.com/currencies/{name}/historical-data/")

    button1 = driver.find_element(By.CLASS_NAME, "sc-16891c57-0 dalfmx BaseButton_base__aMbeB BaseButton_v-primary__zw8Vo BaseButton_t-default__fZuC3 BaseButton_size-md__jbSJR BaseButton_vd__2Cn0v")
    button1.click()

driver.quit()
