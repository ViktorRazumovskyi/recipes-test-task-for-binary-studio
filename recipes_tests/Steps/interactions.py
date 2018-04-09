from behave import *
from selenium.webdriver.common.keys import Keys
use_step_matcher("re")


@when('User clicks on Add New Recipe button with xpath "(.*)"')
def step_impl(context, xpath_id):
    context.browser.find_element_by_xpath(xpath_id).click()


@when('User clicks on particular recipe title with xpath "(.*)"')
def step_impl(context, xpath_id):
    context.browser.find_element_by_xpath(xpath_id).click()

@then("User enter data 'Test recipe adding' to the 'Title' field")
def step_impl(context):
    context.browser.find_element_by_name('title').send_keys('Test ricepi adding')

@then("User enter 'Test recipe adding' to the 'Description' field")
def step_impl(context):
    context.browser.find_element_by_name('description').send_keys('Test ricepi adding')

@then("User click on 'Submit' button")
def stp_iml(context):
    context.browser.find_element_by_xpath('/html/body/div[2]/div/form/div[2]/button[2]').click()



