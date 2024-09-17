# Rooby Dartiny 
# CSC 360; Project # 2
#Discription: This is a webserver that has a webdriver which launches to amazon and determins if 
#users are bias based on the number of 1 and 5 star reviews given 

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup 
import requests
import json
import time

driver = webdriver.Chrome("") #driver defined as webdriver.chrome which lunches the chrome browser 
def getUsers(url): #function named getUsers that goes to the x-path of the reviews 
    driver.get(url)   
    driver.find_element(By.ID, "acrCustomerReviewText").click()
    driver.find_element(By.XPATH, '//*[@data-hook="see-all-reviews-link-foot"]').click()
    
    time.sleep(2) # wait time  set to 2 seconds 
    
    for i in range(0, 10): #A for loop that counts users profile and grabs the reviews 
        count_Profile = i+1
        temp1 = driver.find_elements(By.XPATH, '//div[@id="cm_cr-review_list"]/div/div[@class="a-row a-spacing-none"]/div/div/a[@class="a-profile"]')
        temp2 = driver.find_elements(By.XPATH, '//div[@id="cm_cr-review_list"]/div/div[@class="a-row a-spacing-none"]/div/div/a[@class="a-profile"]/div[@class="a-profile-content"]/span')
        usersDetails = []
        for j in range(len(temp1)):
            User_Info = {}
            User_Info["userPageLink"] = temp1[j].get_attribute('href')
            User_Info["userName"] = temp2[j].text
            usersDetails.append(User_Info)
        pageOfUsers.append(usersDetails)
        time.sleep(2) #wait time set to 2 seconds 
        try:
            driver.find_element(By.XPATH, '//ul[@class="a-pagination"]/li[2]/a').click()
            driver.refresh()
        except:
            break
        print("Review page", count_Profile, "grabbed.")
    print("---DONE---")  # when finished it will let you know 
    
def Find_Review_Value(s): #function difined as Find_Review_Value which has an array of 5
    arr = [1, 2, 3, 4, 5]
    for el in arr:
        if str(el) in s:
            return el

def Enough(u):
    global Total__Users
    driver.get(u["userPageLink"])
    time.sleep(2)
    
    Total__Users += 1
    return len(driver.find_elements(By.XPATH, '//div[@class="your-content-tab-container"]/div'))

def Find_Bias (u):
    global User__bias__Found
    scoreArr = [0, 0, 0, 0, 0, 0]
    userReviews = driver.find_elements(By.XPATH, '//div[@class="your-content-tab-container"]/div/a/div/div/div/div/i')
    for i in range(len(userReviews)):
        scoreArr[Find_Review_Value(userReviews[i].get_attribute('class'))] += 1
    
    Total__Num = sum(scoreArr)
    Get_percentage = 100/Total__Num
    if(scoreArr[5] * Get_percentage) >= 80 or (scoreArr[1] * Get_percentage) >= 80:
        print("***",u["userName"], "is a bias user. ***")
        User__bias__Found += 1
    else:
        print("***", u["userName"], "is not a bias user. ***")
    

pageOfUsers = []
User__bias__Found = 0
Total__Users = 0
option = int(input("Enter 1 to get product info.")) #you must select 1 for it to work 
while option != 1:
    option = input("Enter valid option:") 
if option == 1:
    getUsers('https://a.co/d/hahQlID')


with open('users.json','w') as outFile:
    if pageOfUsers:
        print("Dumping Users!")
        json.dump(pageOfUsers, outFile)
        outFile.write("\n")

for page in pageOfUsers:
    for entry in page:
        if Enough(entry) >= 15:
            print(entry["userName"], " enough reviews to test for bias!")
            Find_Bias (entry)
        else:
            print(entry["userName"], "Reviews not enough to defined bias!.")
print("\n\nTotal  users:", Total__Users)
print(" Bias users found: " + str(User__bias__Found) + "(" + str(round((100/Total__Users) * User__bias__Found, 2)) + "%)")
driver.quit() #Exits the the amazon page



