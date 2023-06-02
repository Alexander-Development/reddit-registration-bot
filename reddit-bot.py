import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.proxy import Proxy, ProxyType
import requests
import os
import re
import string
import time
import random
import json
from lxml.html import fromstring
from random import randint, uniform, shuffle, choice
from password_generator import PasswordGenerator
from selenium_stealth import stealth
from faker import Faker
from fake_headers import Headers
import platform
import threading

password_length = 12
characters = string.ascii_letters + string.digits + string.punctuation

def Type(element: WebElement, text: str):
    for character in text:
        element.send_keys(character)
        time.sleep(uniform(.07, .15))

def Type_Slow(element: WebElement, text: str):
    for character in text:
        element.send_keys(character)
        time.sleep(uniform(.1, .3))

def randsleep(minimum=0.5, maximum=1.3):
    time.sleep(uniform(minimum, maximum))

def register():
    fake = Faker()
    fakeusername = fake.user_name()
    zahl = random.randint(100, 999)
    username = f"{fakeusername}{zahl}"
    password = ''.join(random.choice(characters) for i in range(password_length))
    # Proxies

    # Make a request to the API and save the email address and token
    response = requests.get('https://api.kopeechka.store/mailbox-get-email?api=2.0&site=github.com&sender=github&regex=&mail_type=outlook.com&token=YOURAPIKEY')
    response.raise_for_status()
    data = response.json()
    email = data['mail']
    id = data['id']

    print(email)
    #print(token)

    path = os.path.dirname('./NopeCHA-CAPTCHA-Solver/manifest.json')
    options = uc.ChromeOptions()
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-web-security')
    options.add_argument('--no-sandbox')
    options.add_argument('--log-level=3')
    options.add_argument('--disable-blink-features=AutomationControlled')
    #options.add_argument(f'--user-agent={agent}')
    options.add_argument(f"--load-extension={path}")
    options.add_argument('--screen-size=20000x10000')

    driver = uc.Chrome(options=options, headless=False)
    driver.delete_all_cookies()

    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )

    driver.get('https://reddit.com/register')

    # Enter the email address and click the button
    fields = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="regEmail"]')))
    Type(fields, email)
    randsleep()
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/main/div[1]/div/div[2]/form/fieldset[3]/button')))
    button.click()
    fields = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="regUsername"]')))
    randsleep()
    Type(fields, username)
    randsleep()
    fields = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="regPassword"]')))
    randsleep()
    Type(fields, password)
    time.sleep(10)
    # Sleep until this element is not visible (It's broken code, need to fix)
    while True:
        try:
            fields = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="rc-imageselect"]')))
            randsleep()
            Type(fields, password)
            break
        except:
            break
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/div[2]/div/div/div[3]/button')))
    randsleep()
    button.click()
    time.sleep(5)
    driver.get('PATH TO A COMMENT')
    time.sleep(5)
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="vote-arrows-t1_PUTYOURCOMMENTIDHERE"]/button[1]'))) # Need to change the comment/post id, if you want to upvote something
    button.click()
    randsleep()
threads = []
while True:
    for i in range(1):
        t = threading.Thread(target=register)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
