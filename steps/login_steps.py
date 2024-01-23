from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from config.config import Config


@given('the user is on the login page')
def step_user_on_login_page(context):
    context.driver.get(Config.BASE_URL)git
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.visibility_of_element_located((By.NAME, 'email')))


@when('the user enters valid username and password')
def step_user_enters_credentials(context):
    username = 'vojyxyjini@mailinator.com'
    password = 'admin0101'
    context.driver.find_element(By.NAME, 'email').send_keys(username)
    context.driver.find_element(By.NAME, 'password').send_keys(password)
    context.driver.find_element(By.NAME, 'submit_2').click()


@then('the user should either be successfully logged in or see the another session page')
def step_user_logged_in_or_sees_another_session_page(context):
    try:
        # Check if the another session page is visible

        wait = WebDriverWait(context.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[normalize-space()='Another Session Detected']")))
        another_session_page = context.driver.find_element(By.XPATH,
                                                           "//h2[normalize-space()='Another Session Detected']")

        context.driver.find_element(By.XPATH, "//button[normalize-space()='Continue Here']").click()

        wait.until(EC.visibility_of_element_located((By.XPATH, "//h4[normalize-space()='Product Selection']")))

        success_message = context.driver.find_element(By.XPATH, "//h4[normalize-space()='Product Selection']").text

        assert 'Product Selection' in success_message

    except:

        wait.until(EC.visibility_of_element_located((By.XPATH, "//h4[normalize-space()='Product Selection']")))
        success_message = context.driver.find_element(By.XPATH, "//h4[normalize-space()='Product Selection']").text
        assert 'Product Selection' in success_message



