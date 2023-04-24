from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
print("sample test case started")
#s=Service(r'./chromedriver.exe')
driver = webdriver.Chrome(r'C:\Users\Gaurav\Desktop\Rider\driver\driverchromedriver.exe')
#driver=webdriver.firefox()
#driver=webdriver.ie()
#maximize the window size
driver.maximize_window()
#navigate to the url
driver.get("https://www.google.com/")
#identify the Google search text box and enter the value
v=driver.find_element("name","q")
v.send_keys("12th")
time.sleep(1)
#click on the Google search button
v=driver.find_element("name","btnK")
v.send_keys(Keys.ENTER)
time.sleep(3)
#close the browser
driver.close()
print("sample test case successfully completed")

# inside rider make driver folder and pyfile folder; in driver keep the driver content and in pyfile keep this code and run 
# https://chromedriver.storage.googleapis.com/index.html?path=113.0.5672.24/
