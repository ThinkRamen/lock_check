#!/usr/bin/python

# imports
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os
import sys
import subprocess
import time

thisPath = os.path.dirname(__file__)
print(thisPath)
# variable declaration
GECKO_DRIVER = "{}/required/geckodriver".format(thisPath)
options = Options()
options.binary_location = "{}/required/Firefox.app/Contents/MacOS/firefox-bin".format(
    thisPath)
checkSerial = "system_profiler SPHardwareDataType | awk '/Serial/ {print $4}'"
runSettingScript = "open 'x-apple.systempreferences:com.apple.preference.security?Privacy_ScreenCapture'"
serialNumber = ""
enterKey = "\ue007"
# user details
email = "alejandro.ramos@no.email"
password = "AssetRecovery1"

# terminal commands
proc = subprocess.Popen(checkSerial, shell=True, stdout=subprocess.PIPE, )
output = proc.communicate()[0]
serialNumber = output.decode("UTF-8").strip()
print(serialNumber)


def get_auth():
    URL = 'https://lock-check-backend.herokuapp.com/customers/1/?format=json'
    r = requests.get(url=URL)
    data = r.json()
    if data['authorization'] == False:
        sys.exit('Not Authorized')
    return r.status_code
# FUNCTIONS
# Write activationLock output to text file


def lockStatusToTxt(serial):
    activationLock = "'{}/required/_activation_lock.command'".format(thisPath)
    file = open('{}/output/{}.txt'.format(thisPath, serial), 'w')
    subprocess.Popen(activationLock, shell=True, stdout=file)
    file.close()
    return os.path.abspath(file.name)
    ###


def firefoxAutomation(outputTxtPath):
    # application -->
    driver = webdriver.Firefox(options=options, executable_path=GECKO_DRIVER)
    driver.maximize_window()
    # launch website url
    driver.get('https://smarterp.io/')
    # login
    email_element = driver.find_element(
        "xpath", "//input[@type='text']")
    email_element.send_keys(email)
    password_element = driver.find_element(
        "xpath", "//input[@type='password']")
    password_element.send_keys(password)
    password_element.send_keys(enterKey)
    # search serial number
    driver.implicitly_wait(5)
    search_element = driver.find_element(
        "xpath", "/html/body/div[3]/div/header/div[2]/div/div[1]/div/div/div/div[2]/div/div/div/form/input")
    search_element.send_keys(serialNumber)
    search_element.send_keys(enterKey)
    time.sleep(3)
    attachment_element = driver.find_element(
        "xpath", "/html/body/div[3]/div/div/div/div/div/section/div/div[2]/ul/li[4]/a")
    attachment_element.click()
    time.sleep(1)
    add_new_document_element = driver.find_element(
        "xpath", "/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/span[1]")
    add_new_document_element.click()
    time.sleep(5)
    upload_document_element_input = driver.find_element(
        "xpath", "/html/body/div[3]/div/div/div/div/div/div[2]/div/div[2]/div/div[3]/div[2]/div/form/section/div[2]/label/input")
    upload_document_element_input.send_keys(outputTxtPath)

    upload_document_button_element = driver.find_element(
        "xpath", "/html/body/div[3]/div/div/div/div/div/div[2]/div/div[2]/div/div[3]/div[2]/div/form/footer/button[1]")
    upload_document_button_element.click()
    time.sleep(3)
    image_link_element = driver.find_element(
        "xpath", "//a[normalize-space()='{}.txt']".format(serialNumber))
    image_link_element.click()
    time.sleep(60)
    driver.quit()
    ###


get_auth()
# function returns path of txt file created
outputTxt = lockStatusToTxt(serialNumber)
firefoxAutomation(outputTxt)
