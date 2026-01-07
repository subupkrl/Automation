from Base.InitiateDriver import startBrowser,closeBrowser

def test_InValidateRegistration():
    
    driver = startBrowser()
    
    driver.find_element('xpath',"//input[@name='firstname']").send_keys("123")
    driver.find_element('xpath',"//input[@name='lastname']").send_keys("23@")
    driver.find_element('xpath',"//select[@name='birthday_month']").send_keys("4")
    driver.find_element('xpath',"//select[@name='birthday_day']").send_keys("3")
    driver.find_element('xpath',"//select[@name='birthday_year']").send_keys("2002")
    driver.find_element('xpath',"//input[@value='1']").click()
    driver.find_element('xpath',"//input[@name='reg_email__']").send_keys("123@ghk")
    driver.find_element('xpath',"//input[@name='reg_passwd__']").send_keys("1223")
    driver.find_element('xpath',"//button[@name='websubmit']").click()
    
    closeBrowser()
    