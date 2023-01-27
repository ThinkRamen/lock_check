#!/usr/bin/python

# imports
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from lock_check import serial_number
# variable declaration

enterKey = "\ue007"
# user details
email = 'alejandro.ramos@no.email'
password = 'AssetRecovery1'
serial = serial_number()

# Write activationLock output to text file


def firefox_automation(txt_file):
    # application -->
    driver = webdriver.Firefox()

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
    search_element.send_keys(serial)
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
    upload_document_element_input.send_keys(txt_file)

    upload_document_button_element = driver.find_element(
        "xpath", "/html/body/div[3]/div/div/div/div/div/div[2]/div/div[2]/div/div[3]/div[2]/div/form/footer/button[1]")
    upload_document_button_element.click()
    time.sleep(3)
    image_link_element = driver.find_element(
        "xpath", f"//a[normalize-space()='{serial}.txt']")
    image_link_element.click()
    ###
