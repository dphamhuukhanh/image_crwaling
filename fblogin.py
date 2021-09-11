import random

from selenium import webdriver
from time import sleep

driver = webdriver.Edge(
    r'D:\PycharmProject\facebook_crawling\edgedriver_win64\msedgedriver.exe'
)

driver.get('https://www.facebook.com')

sleep(random.randrange(3,5,1))

driver.close()