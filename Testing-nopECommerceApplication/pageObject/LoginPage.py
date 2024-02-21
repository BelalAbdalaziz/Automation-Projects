#############################################
#       For Helping Auto Complete           #
#############################################
#from selenium import webdriver                              
from selenium.webdriver.common.by import By                 

#Creat Class For Page 
class Login :
    #Class Attribute store to it all objects locator
    textBox_userName_id = "Email"
    textBox_password_id = "Password"
    button_login_XPath="/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    link_logout_XPath="/html/body/div[3]/nav/div/ul/li[3]/a"

    def __init__(self,driver):
        self.driver = driver
    
    # Write User Name in textBox_userName
    def setUserName(self,userName):
        #self.driver = webdriver.Firefox() #for Helping Auto Complete
        # Capture Element
        userNameElement = self.driver.find_element(by=By.ID,value=self.textBox_userName_id)
        # Clear
        userNameElement.clear()
        # Write User Name
        userNameElement.send_keys(userName)

    # Write Password in textBox_password
    def setPassword(self,password):
        #self.
        # Capture Element
        passwordElement = self.driver.find_element(by=By.ID,value=self.textBox_password_id)
        # Clear
        passwordElement.clear()
        # Write Password
        passwordElement.send_keys(password)
    
    # click on login button
    def clickLogin(self):
        #self.driver = webdriver.Firefox() #for Helping Auto Complete
        # Capture Element
        loginElement = self.driver.find_element(by=By.XPATH,value=self.button_login_XPath)
        # Click On Login
        loginElement.click()    
    # click on logout button
    def clickLogout(self):
        #self.driver = webdriver.Firefox() #for Helping Auto Complete
        # Capture Element
        logoutElement = self.driver.find_element(by=By.XPATH,value=self.link_logout_XPath)
        # Click On logout
        logoutElement.click() 
    #Quit from the browser
    def clickQuit(self):
        #self.driver = webdriver.Firefox() #for Helping Auto Complete
        # Quit The Browser
        self.driver.quit()
        
         