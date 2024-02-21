#This file used to repharse data from < Config.ini File > To < TestCases Files >
import configparser

#Creat Object to use it for reading data
config = configparser.RawConfigParser()
# Read Config data from other file
config.read(".\\Configurations\Config.ini")

#Creat Class To use it into test files
#config.get("Category","key")
class ReadConfig :
    #creat all methods Static to call it without creat object from class
    @staticmethod
    def get_loginURL():
        return config.get("Common Info","url_login")
    @staticmethod
    def get_userName_valid():
        return config.get("Common Info","userName_valid")
    @staticmethod
    def get_password_valid():
        return config.get("Common Info","password_valid")
    