# Import Dependencies
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

PATH = "C:\Windows\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://twitter.com/login")
 

# Setup the log in
sleep(3)
username = driver.find_element(By.XPATH,"//input[@name='text']")
username.send_keys("imAmnrai")
next_button = driver.find_element(By.XPATH,"//span[contains(text(),'Next')]")
next_button.click()

sleep(3)
password = driver.find_element(By.XPATH,"//input[@name='password']")
password.send_keys('leanerea.bot')
log_in = driver.find_element(By.XPATH,"//span[contains(text(),'Log in')]")
log_in.click()

link = input("Eneter the link here : ")
driver.get(link)

 
sleep(3)
UserTag = driver.find_element(By.XPATH,".//div[@data-testid='User-Names']").text

sleep(3)
Tweet = driver.find_element(By.XPATH,".//div[@data-testid='primaryColumn']").text


sleep(3)
Like = driver.find_element(By.XPATH,".//div[@data-testid='tweetText']").text
 
data = {}
data["User_Name"] = UserTag.split("\n")[0]
data["User_id"] = UserTag.split("\n")[1]
data["Tweets"] = (Tweet.split("\n")[1]).split(" ")[0]
data["Following"] = (Tweet.split("\n")[-2]).split(" ")[0]
data["Followers"] = (Tweet.split("\n")[-1]).split(" ")[0]

print(data)
 
 