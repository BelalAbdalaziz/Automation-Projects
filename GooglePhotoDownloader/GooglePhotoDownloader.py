#--------------- Imports ---------------
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
#--------------- Configuration ---------------------
web = webdriver.Firefox()
mouse = webdriver.ActionChains(web)
#--------------- Start Of Script ---------------------
web.get("https://www.google.com/")


searchBox = web.find_element(By.XPATH,'//*[@id="APjFqb"]')
searchBox.send_keys("Cat")
searchClick = web.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
searchClick.click()

imagesSearchClick = web.find_element(By.XPATH,'/html/body/div[6]/div/div[3]/div/div[1]/div/div[1]/div/div[2]/a')
imagesSearchClick.click()

desiredPhotos_1 = web.find_element(By.XPATH,'/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[1]/a[1]/div[1]/img')
desiredPhotos_1.click()
desiredPhotos_2 = web.find_element(By.XPATH,'/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div/div[3]/div[1]/a/img[1]')
#RihtClick
mouse.context_click(desiredPhotos_1)
mouse.perform()
#To open in new page
#.send_keys(Keys.ARROW_DOWN)

#desiredPhotos_2 = find_element(By.XPATH,'/html/body/img')
#savePhoto = desiredPhotos_2.screenshot("img.png")
#print(savePhoto)

#tags = web.find_elements(By.TAG_NAME,'img')
#print(len(tags))



#--------------- End Of Script ---------------------


'''
counter =0
for i in tags:
    counter+=1
    i.click()
    photos = web.find_element(By.XPATH,'/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[1]/a[1]/div[1]/img')
    photos = i.screenshot("Downloaded\img"+str(counter)+".png")
    print(photos)
    if counter ==6:
        break
'''