from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time

def getLocation():
    options = Options()
    options.add_argument("--use--fake-ui-for-media-stream")
    driver = webdriver.Chrome(executable_path = './chromedriver.exe',options=options) #Edit path of chromedriver accordingly
    timeout = 20
    driver.get("https://mycurrentlocation.net/")
    wait = WebDriverWait(driver, timeout)
    time.sleep(3)
    longitude = driver.find_elements_by_xpath('//*[@id="longitude"]')     
    longitude = [x.text for x in longitude]    
    longitude = str(longitude[0])    
    latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')    
    latitude = [x.text for x in latitude]    
    latitude = str(latitude[0])    
    driver.quit()    
    return (latitude,longitude)

#Main Function
tuple1=getLocation()
lat=tuple1[0]
lon=tuple1[1]
driver = webdriver.Chrome(executable_path = './chromedriver.exe')
driver.get('https://www.google.com/maps/place/'+str(lat)+" "+str(lon))
sleep(1)
a=driver.find_element_by_xpath("//span[@class='widget-pane-link']")
text = a.get_attribute('innerText')
print("Location: "+text)
driver.quit() 

