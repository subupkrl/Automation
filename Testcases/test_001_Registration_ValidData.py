# from Base import InitiateDriver
from Base.InitiateDriver import startBrowser,closeBrowser
from Library.ConfigReader import readElements

def test_ValidateRegistration():
    # driver = InitiateDriver.startBrowser()
    driver = startBrowser()
    
    driver.find_element('name',readElements("Registration","fname")).send_keys("Hello")
    driver.find_element('name',readElements("Registration","lname")).send_keys("Sharma")
    driver.find_element('name',readElements("Registration","bd_mon")).send_keys("Dec")
    driver.find_element('name',readElements("Registration","bd_day")).send_keys("3")
    driver.find_element('name',readElements("Registration","bd_year")).send_keys("2002")
    driver.find_element('xpath',readElements("Registration","a")).click()
    driver.find_element('name',readElements("Registration","email")).send_keys("subu@gmail.com")
    driver.find_element('name',readElements("Registration","pwd")).send_keys("subu@123")
    driver.find_element('xpath',readElements("Registration","submit")).click()
    
    closeBrowser()
    # InitiateDriver.closeBrowser()