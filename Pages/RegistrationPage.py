from Library.ConfigReader import readElements

class RegistrationData:
    
    def __init__(self,obj):
        global driver 
        driver=obj

    def enterFirstName(self,firstname):
        driver.find_element('name',readElements("Registration","fname")).send_keys(firstname)
    
    def enterLastName(self,lastname):
        driver.find_element('name',readElements("Registration","lname")).send_keys(lastname)
    
    def birthdayMonth(self,month):
        driver.find_element('name',readElements("Registration","bd_mon")).send_keys(month)

    def birthdayDay(self,day):
        driver.find_element('name',readElements("Registration","bd_day")).send_keys(day)
    
    def birthdayYear(self,year):
        driver.find_element('name',readElements("Registration","bd_year")).send_keys(year)
    
    def gender(self,genderData):
        if genderData=='Male':
            driver.find_element('xpath',readElements("Registration","b")).click()
        elif genderData=='Female':
            driver.find_element('xpath',readElements("Registration","a")).click()
        else:
            driver.find_element('xpath',readElements("Registration","c")).click()

    def enterEmail(self,email):
        driver.find_element('name',readElements("Registration","email")).send_keys(email)
    
    def enterPassword(self,pwd):
        driver.find_element('name',readElements("Registration","pwd")).send_keys(pwd)

    def submit(self):
        driver.find_element('xpath',readElements("Registration","submit")).click()
    
