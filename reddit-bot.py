# Reddit is not allowing the registration request, still working on a fix (connection closed by remotehost)
import requests
import random
import time
import json
from urllib.parse import urlencode
import re
import pytest
import string
import nopecha
from bs4 import BeautifulSoup
import ssl
import threading
from anticaptchaofficial.recaptchav2proxyless import *
from faker import Faker

ssl.PROTOCOL_TLS = ssl.PROTOCOL_TLSv1_2
password_length = 12
characters = string.ascii_letters + string.digits + string.punctuation

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

    proxy_host = 'proxyip'
    proxy_port = proxyport
    proxy_username = 'username'
    proxy_password = 'password'

    # Captchasolver
    solver = recaptchaV2Proxyless()
    solver.set_verbose(1)
    solver.set_key("YOURAPIKEY")
    solver.set_website_url("https://www.reddit.com/register")
    solver.set_website_key("6LeTnxkTAAAAAN9QEuDZRpn90WwKk_R1TRW_g-JC")

    # Request to get the CSRF TOKEN
    response = requests.get('https://www.reddit.com/account/register/', proxies={"http": f"http://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}"})
    print(response.status_code)
    # Extract CSRF TOKEN
    soup = BeautifulSoup(response.content, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrf_token'})['value']
    print(csrf_token)  

    solver.set_soft_id(0)

    g_response = solver.solve_and_return_solution()
    if g_response != 0:
        print("g-response: "+g_response)
    else:
        print("")

    # Loop until captcha is solved
    while g_response == 0:
        time.sleep(5)
        g_response = solver.solve_and_return_solution()

    session = requests.Session()
    session.proxies = {
        "http": f"http://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}",
        "https": f"http://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}",
    }

    url = "https://www.reddit.com/register"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0",
        "Accept": "*/*",
        "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://www.reddit.com",
        "DNT": "1",
        "Connection": "keep-alive",
        "Referer": "https://www.reddit.com/account/register/?dest=https%3A%2F%2Fwww.reddit.com%2F%3FnewUser%3Dtrue%26signup_survey%3Dtrue"
    }

    data = {
        'csrf_token': csrf_token,
        'g-recaptcha-response': g_response,
        'password': password,
        'dest': "https://www.reddit.com/?newUser=true&signup_survey=true",
        'email_permission': "false",
        'lang': "de-DE",
        'username': username,
        'email': email
    }

    response = session.post(url, headers=headers, data=data, proxies=session.proxies)
    time.sleep(5)

threads = []
while True:
    for i in range(1):
        t = threading.Thread(target=register)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
