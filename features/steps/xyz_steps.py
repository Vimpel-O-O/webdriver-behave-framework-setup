from behave import *
import time


@step('Open main page')
def step_impl(context):
    context.browser.get("https://www.amazon.com/")


@step('Click on {locator}')
def step_impl(context, locator):
    if locator == "cart":
        locator = "//a[@id='nav-cart']"
    context.element.click(locator)


@step('Wait for {num}')
def step_impl(context, num):
    time.sleep(num)