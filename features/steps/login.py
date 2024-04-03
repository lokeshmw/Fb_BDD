from behave import *
from selenium.common import NoSuchElementException

from features.pages.login_page import LoginPage


@given(u'I navigated to Login page')
def step_impl(context):
    context.login_page = LoginPage(context.driver)


@when(u'I enter valid email as "{email}" and valid password as "{password}" into the fields')
def step_impl(context, email, password):
    context.login_page.enter_email(email)
    context.login_page.enter_password(password)


@when(u'I click on Login button')
def step_impl(context):
    context.login_page.click_login()


@then(u'I should get logged in for valid email and password')
def step_impl(context):
    context.login_page.verify_login("Welcome to Facebook")


@when(u'I enter valid email as "{email}" and invalid password as "{password}" into the fields')
def step_impl(context, email, password):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email(email)
    context.login_page.enter_password(password)


@then(u'I should get a proper warning message on password Error for valid email')
def step_impl(context):
    context.login_page.verify_password_error("The password you've entered is incorrect.")


@when(u'I enter invalid email as "{email}" and valid password as "{password}" into the fields')
def step_impl(context, email, password):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email(email)
    context.login_page.enter_password(password)


@then(u'I should get a proper warning message on email Error for valid password')
def step_impl(context):
    context.login_page.verify_phone_error("The email address you entered isn't connected to an account. ")


@when(u'I enter valid phone as "{phone}" and valid password as "{password}" into the fields')
def step_impl(context, phone, password):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_phone(phone)
    context.login_page.enter_password(password)


@then(u'I should get logged in for valid phone and password')
def step_impl(context):
    context.login_page.verify_login("Welcome to Facebook")


@when(u'I enter valid phone as "{phone}" and invalid password as "{password}" into the fields')
def step_impl(context, phone, password):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_phone(phone)
    context.login_page.enter_password(password)


@then(u'I should get a proper warning message on password Error for valid phone')
def step_impl(context):
    try:
        context.login_page.verify_password_error("The password you've entered is incorrect.")
    except NoSuchElementException:
        context.login_page.verify_Password_error_phone("Log in as Kane Williams")


@when(u'I enter invalid phone as "{phone}" and valid password as "{password}" into the fields')
def step_impl(context, phone, password):
    context.login_page.enter_phone(phone)
    context.login_page.enter_password(password)


@then(u'I should get a proper warning message on phone number Error for valid password')
def step_impl(context):
    try:
        context.login_page.verify_password_error("The password you've entered is incorrect.")
    except NoSuchElementException:
        context.login_page.verify_Password_error_("Log in to Facebook")


@when(u'I enter empty email and empty password into the fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)


@then(u'I should get a proper warning message on email/phone number Error for empty')
def step_impl(context):
    context.login_page.verify_phone_error("The email address or mobile number you entered isn't connected to an "
                                          "account. Find your account and log in.")


@when(u'I enter invalid email format as "{email}" and valid password as "{password}" into the fields')
def step_impl(context, email, password):
    context.login_page.enter_email(email)
    context.login_page.enter_password(password)


@then(u'I should get a proper warning message on email error for invalid email format')
def step_impl(context):
    context.login_page.verify_email_error("We couldn't find an account that matches what you entered, but we've found "
                                          "one that closely matches.")


@when(u'I enter valid email as "{email}" and empty password into the fields')
def step_impl(context, email):
    context.login_page.enter_email(email)


@then(u'I should get a proper warning message on password error for empty password/valid email')
def step_impl(context):
    context.login_page.verify_email_error("We couldn't find an account that matches what you entered, but we've found "
                                          "one that closely matches.")


@when(u'I enter valid phone as "{phone}" and empty password into the fields')
def step_impl(context, phone):
    context.login_page.enter_phone(phone)


@then(u'I should get a proper warning message on password error for empty password/valid phone')
def step_impl(context):
    context.login_page.verify_phone_error("The email address or mobile number you entered isn't connected to an "
                                          "account. Find your account and log in.")


@when(u'I clicked on the forgot password')
def step_impl(context):
    context.login_page.click_on_forgot_password()


@then(u'verify that functionality is working properly for forgot password')
def step_impl(context):
    context.login_page.verify_forgotPass("Please enter your email address or mobile number to search for your account")


@when(u'I clicked on the signup')
def step_impl(context):
    context.login_page.click_on_createAccount()


@then(u'verify that functionality is working properly for signups')
def step_impl(context):
    context.login_page.verify_createAccount("Sign Up")
