from behave import *
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
use_step_matcher("re")


@given('User on the home page')
def step_impl(context):
    context.browser = webdriver.Chrome('C:\Chrome driver\chromedriver.exe')
    context.browser.get('https://volodymyr-kushnir.github.io/recipes/')
    context.browser.maximize_window()

@then('Add New Recipe window opens with xpath "(.*)"')
def step_impl(context, xpath_id):
    try:
        context.browser.find_element_by_xpath(xpath_id)
    except NoSuchElementException:
        return False
    return True
    context.browser.quit()
@then('Full Recipe View page opens with xpath "(.*)"')
def step_impl(context, xpath_id):
    try:
        context.browser.find_element_by_xpath(xpath_id)
    except NoSuchElementException:
        return False
    return True
    context.browser.quit()
@then("User can see a new recipe with 'Test recipe adding' text")
def step_impl(context):
    all_recipes = context.browser.find_element_by_class_name('Description')
    check_recipe = [x for x in all_recipes if "Test recipe adding"==x.text][0]
    assert len(check_recipe)>0


