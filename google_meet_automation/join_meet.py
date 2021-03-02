# this join meet function automatically opens a browser and login with your email and password into the gmeet and turn your mic and camera off and joins the meet of the class you have requested

from selenium import webdriver
import passwords
from time import sleep
from selenium.webdriver.chrome.options import Options
from Todays_Classes import *

def join_meet(code):
    opt = Options()
    opt.add_argument('start-maximized')
    opt.add_argument("--disable-extensions")
    opt.add_experimental_option('excludeSwitches', ['enable-logging'])
    # Pass the argument 1 to allow and 2 to block
    opt.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 1,
        "profile.default_content_setting_values.notifications": 1
    })

    driver = webdriver.Chrome(options=opt, executable_path='chromedriver.exe')

    driver.get(
        f'https://accounts.google.com/AccountChooser/identifier?continue=https%3A%2F%2Fmeet.google.com%2Flookup%2F{code}%3Flookupauth%3Dtrue&hl=en_GB&flowName=GlifWebSignIn&flowEntry=AccountChooser')

    username = driver.find_element_by_xpath('//*[@id="identifierId"]')
    username.click()
    username.send_keys(passwords.srm_email)

    next = driver.find_element_by_xpath(
        '//*[@id="identifierNext"]/div/button/div[2]')
    next.click()

    sleep(2)

    password = driver.find_element_by_xpath(
        '//*[@id="password"]/div[1]/div/div[1]/input')
    password.click()
    password.send_keys(passwords.pd)
    nextp = driver.find_element_by_xpath(
        '//*[@id="passwordNext"]/div/button/div[2]')
    nextp.click()

    sleep(8)
    camera = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div')
    camera.click()

    mic = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div/div/div')
    mic.click()

    sleep(3)
    join = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]')
    join.click()

    sleep(7200)
    print('joined requested class')
