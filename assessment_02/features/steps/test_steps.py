from behave import given, when, then
from selenium import webdriver
from pages.login_page import LoginPage

@given('I open the Pickaboo login page')
def open_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.pickaboo.com/login")

@when('I enter valid credentials')
def enter_valid_credentials(context):
    login_page = LoginPage(context.driver)
    login_page.enter_username("valid_username")
    login_page.enter_password("valid_password")

@when('I click on the login button')
def click_login_button(context):
    login_page = LoginPage(context.driver)
    login_page.click_login_button()

@then('I should be logged in successfully')
def verify_successful_login(context):
    assert "dashboard" in context.driver.current_url

@then('I should see an error message')
def verify_error_message(context):
    assert "Invalid username or password" in context.driver.page_source

@then('I close the browser')
def close_browser(context):
    context.driver.quit()
