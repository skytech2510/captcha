
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import json
from time import sleep
import csv
import pandas as pd
import requests
import os
import sys
from twocaptcha import TwoCaptcha

user_data_dir = r"C:\Users\Monster\AppData\Local\Google\Chrome\User Data\Default"

# username = os.getlogin()

def wait_and_find_element(driver, by, value, timeout=20):
    """Wait for an element to be present and return it."""
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, value))
    )
def wait_and_find_elements(driver, by, value, timeout=20):
    """Wait for elements to be present and return them."""
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_all_elements_located((by, value))
    )
def safe_click(element):
    for _ in range(3):
        try:
            element.click()
            return True
        except StaleElementReferenceException:
            continue
    return False
def login(passwd="", userid=""):
    formElement = wait_and_find_element(driver, By.TAG_NAME, "form")
    userIdInputElement = formElement.find_element(By.ID, "card-login")
    passwordInputElement = formElement.find_element(By.ID, "card-password")
    captchaInputElement = formElement.find_element(By.ID, "card-captcha")
    sumitButtonElement = formElement.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    code = captcha()
    userIdInputElement.clear()
    userIdInputElement.send_keys(userid)
    passwordInputElement.clear()
    passwordInputElement.send_keys(passwd)
    captchaInputElement.clear()
    captchaInputElement.send_keys(code)
    
    if safe_click(sumitButtonElement):
        time.sleep(2)
        erroMessages = wait_and_find_element(driver, By.ID, "getListMessages").find_element(By.TAG_NAME, "script")
        if erroMessages:
            print("Authorization Error!")
            return False
        else:
            print("sdfsdfsdf")
        
    return False
def captcha():
    imageElement = wait_and_find_element(driver, By.ID, "resset-captcha_img")
    solver = TwoCaptcha("2f26ebdfbb20ac7f124b8f0592fb312b")
    imageElement.screenshot("aa.png")
    result = solver.normal("./aa.png")
    return result["code"]
        
driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()));
try:
    driver.get('https://premiuminfo.cc/')
    login("Kaduucti1234", "olanprimotivo", )
   
finally:
    driver.quit()
    