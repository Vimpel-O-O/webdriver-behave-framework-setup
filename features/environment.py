from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from components.base import Base


def before_all(context):
    PATH = "/Users/sk/Documents/Code/webdriver-behave-framework-setup/chromedriver"
    service = Service(PATH)
    options = Options()

    context.browser = webdriver.Chrome(service=service, options=options)
    context.element = Base(context.browser)


def after_all(context):
    context.browser.quit()
