from behave import given, when, then
from hamcrest.core import assert_that
from hamcrest.core.core.isequal import equal_to

from pages.home import Home
from pages.base import Base

# EMAIL SIGNUP
@when(u'I enter "{email_address}"')
def step(context, email_address):
    context.rate_checker.set_email_address(email_address)


@when(u'I click the Signup button')
@when(u'I click the Signup button again')
def step(context):
    context.base.click_signup_button()


@then(u'I should see "{expected_text}" displayed')
def step(context, expected_text):
    actual_text = context.base.get_email_label()
    assert_that(actual_text, equal_to(expected_text))


@then(u'I should NOT see multiple "{expected_text}" messages displayed')
def step(context, expected_text):
    error_msg = u'Multiple messages found'
    multiple_labels = context.base.is_multiple_email_labels()
    assert_that(multiple_labels, equal_to(False), error_msg)
