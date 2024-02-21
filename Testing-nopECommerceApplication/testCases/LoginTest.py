
############ Imports ##############
import selenium
import pytest
#Import <Login Class> from <LoginPage file> Page Objects
from pageObject.LoginPage import Login
# Common Info from Config.ini by use ReadConfig from utilites Package
from utilites.ReadConfig import ReadConfig
#Import Custom logger which used to loging operations
from utilites.CustomLogger import LogGen  

# Creat Class To LoginTest <test_ID_Name>
class Test_001_Login :
    # Happy Scenario 
    #  Class Attributes For Common Test Data
    urlBase = ReadConfig.get_loginURL()
    validUserName =ReadConfig.get_userName_valid()
    validPassword = ReadConfig.get_password_valid()
    # Creat Variable to store return of log_gen Method
    logger = LogGen.loggen()
    
    def test_pageTitle(self,setup) :
        ####1.1.Log ####
        #### 1.Log ####
        self.logger.info("******************* 1.1.Test_001_Login *****************")
        self.logger.info("******************* 1.1.1.Start Test Page Title *****************")
        #setup driver
        self.driver = setup
        # Go To Login Page
        self.driver.get(self.urlBase)
        # Actual Result and Expected Result
        expectedResult = "Your store. Login"
        actualResult = self.driver.title
        # Verify
        ####1.2.Log ####
        self.logger.info("******************* 1.1.2.Verifying Page Title *****************")
        if actualResult == expectedResult :
            assert True
            #### Log ####
            self.logger.info("******************* 1.1.3. Test Result: Test Page Title Is Passed *****************")
        else:
            #### Log ####
            self.logger.error("******************* 1.1.3. Test Result: Test Page Title Is Failed *****************")
            assert False 
        self.driver.quit()


    def test_login(self,setup) :
        ####2.1.Log ####
        self.logger.info("******************* 1.2.1.Start Test Login *****************")
        #setup driver
        self.driver = setup
        # Go To Login Page
        self.driver.get(self.urlBase)
        #creat objectClass from Login Page
        loginPageObject = Login(self.driver)
        #write userName
        loginPageObject.setUserName(self.validUserName)
        #write password
        loginPageObject.setPassword(self.validPassword)
        #Click Login
        loginPageObject.clickLogin()
        # Actual Result and Expected Result
        expectedResult = "Dashboard / nopCommerce administration"
        actualResult = self.driver.title
        # Verify
        ####2.2.Log ####
        self.logger.info("******************* 1.2.2.Verifying Login *****************")
        if actualResult == expectedResult :
            self.driver.save_screenshot(".\\ScreenShots\\test_validPass_validUserName_Pass.png")
            assert True
            #### Log ####
            self.logger.info("******************* 1.2.3. Test Result: Test Login Is Passed *****************")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\test_validPass_validUserName_Fail.png")
            #### Log ####
            self.logger.error("******************* 1.2.3. Test Result: Test Login Is Failed *****************")
            assert False
        #Quit
        loginPageObject.clickQuit()    

#To run Test Cases in CMD Write => pytest -v -s testCases\LoginTest.py