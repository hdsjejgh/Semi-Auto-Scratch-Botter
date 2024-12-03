from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from random import randint,choices
from string import ascii_letters
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
#imports ^^^

while False:
    os.system("shutdown /p")

def submit(browser): #clicks submit button since it is the same on each signup page
    browser.find_element(By.CLASS_NAME,"modal-flush-bottom-button").click()
    sleep(1)

def bot(link):
    #creates a scratch account (each block is a different screen)

    #setting up browser and going to scratch
    options = Options()
    ua = UserAgent()
    user_agent = ua.random
    options.add_argument(f'--user-agent={user_agent}')
    browser = webdriver.Chrome(options=options) #the random agent might bypass recaptcha?? (maybe)
    browser.set_window_size(500, 750)
    browser.get("https://scratch.mit.edu/join")

    #clicks sign up and creates username and password and continues
    username=''.join(choices(ascii_letters,k=8))+str(randint(1_000_000,999_999_999))
    print(f"Username: {username}")
    browser.find_element(By.ID, "username").send_keys(username)
    password  = "p"+str(randint(1_000_000,999_999_999))
    print(f"Password: {password}")
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "passwordConfirm").send_keys(password)
    submit(browser)

    #selects index 4 as country and continues
    try:
        x=browser.find_element(By.ID,"country")
    except:
        print("username error????")
        browser.quit()
        return
    sel = Select(x)
    sel.select_by_value("France")
    submit(browser)

    #selects april 1984 as birth year and continues
    Select(browser.find_element(By.ID, "birth_month")).select_by_visible_text("April")
    Select(browser.find_element(By.ID, "birth_year")).select_by_visible_text("1984")
    submit(browser)

    #selects male as gender and continues
    browser.find_element(By.ID, "GenderRadioOptionMale").click()
    submit(browser)


    #selects random email and continues
    email=''.join(choices(ascii_letters,k=4))+str(randint(100,999))+"@gmail.com"
    print(f"Email: {email}")
    browser.find_element(By.ID, "email").send_keys(email)
    sleep(1)
    submit(browser)
    if (input("Is there a captcha? (Y/N): ").upper()=="Y"):
        print("Solve it")
        input("Click enter when done")


    #submits final screen
    submit(browser)


    # goes through scratch guidelines
    for i in range(7):
        browser.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div[2]/button[2]").click()
        sleep(.1)
    browser.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div[2]/button[2]").click()
    #browser should be signed in

    #goes to specified project link
    browser.get(link)
    sleep(3)
    #favorites and hears project
    browser.find_element(By.CLASS_NAME, "project-loves").click()
    browser.find_element(By.CLASS_NAME, "project-favorites").click()

    sleep(1)
    browser.quit()

