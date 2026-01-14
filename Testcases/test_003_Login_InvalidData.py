from Base.InitiateDriver import startBrowser,closeBrowser
from selenium.webdriver import Chrome

def test_InvalidLogin():
    
    driver = Chrome()
    driver.get("https://www.facebook.com/login")
    driver.find_element('xpath',"//input[@name='email']").send_keys("1hello")
    driver.find_element('xpath',"//input[@name='pass']").send_keys("4567")
    driver.find_element('xpath',"//button[@name='login']").click()
    
    closeBrowser()
    
    
    