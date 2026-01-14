# import configparser

# def configRead(section,key):
    
#     config = configparser.ConfigParser()
#     config.read('../ConfigurationFiles/Config.cfg')
    
#     return config.get(section,key)

# # print(configRead('Details','APP_URL'))

# def readElements(section,key):
    
#     config = configparser.ConfigParser()
#     config.read("../ConfigurationFiles/Elements.cfg")
    
#     return config.get(section,key)

import configparser
import os

config = configparser.ConfigParser()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config_path = os.path.join(BASE_DIR, "Config", "config.ini")

config.read(config_path)

def configRead(section, key):
    return config.get(section, key)
