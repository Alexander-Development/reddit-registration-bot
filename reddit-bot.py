import requests

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
    # Include your data parameters here
}

response = requests.post(url, headers=headers, data=data)