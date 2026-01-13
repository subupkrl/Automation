# from Base import InitiateDriver
from Base.InitiateDriver import startBrowser,closeBrowser
from Library.ConfigReader import readElements
from Pages.RegistrationPage import RegistrationData
import pytest
from DataGenerator.DataGen import dataGenerator

# def dataGenerator():
#     listData=[
#         ['Ram','Sharma','Dec','3','2003','ram@gmail.com','12345678','Male'],
#         ['Shyam','Karki','Sep','10','1999','shyam@gmail.com','123456789','Male'],
#         ['Sita','Pandey','Oct','20','2000','sita@gmail.com','1234567890','Female']
#         ]
#     return listData


@pytest.mark.parametrize('data',dataGenerator())
def test_ValidateRegistration(data):
    # driver = InitiateDriver.startBrowser()
    driver = startBrowser()
    register=RegistrationData(driver)
    register.enterFirstName(data[0])
    register.enterLastName(data[1])
    register.birthdayMonth(data[2])
    register.birthdayDay(data[3])
    register.birthdayYear(data[4])
    register.gender(data[7])
    register.enterEmail(data[5])
    register.enterPassword(data[6])

    register.submit()
    
    closeBrowser()
    # InitiateDriver.closeBrowser()