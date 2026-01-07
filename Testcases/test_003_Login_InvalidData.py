from Base.InitiateDriver import startBrowser,closeBrowser

def test_InvalidLogin():
    
    driver = startBrowser()
    
    driver.find_element('xpath',"//input[@name='email']").send_keys("1hello")
    driver.find_element('xpath',"//input[@name='pass']").send_keys("4567")
    driver.find_element('xpath',"//button[@name='login']").click()
    
    closeBrowser()
    
    
    