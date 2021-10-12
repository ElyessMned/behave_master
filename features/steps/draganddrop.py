from behave import given, when, then
from numpy.testing import assert_equal
from selenium import webdriver
from selenium.webdriver import ActionChains


@given(u'the user navigate to the URL https://qavbox.github.io/demo/dragndrop/')
def step_impl(context):
        context.browser.get("https://qavbox.github.io/demo/dragndrop/")


@when(u'he drag and drop the grey square in the blue square')
def step_impl(context):
    context.dd.drag()

@then(u'he sees a message "Dropped!"')
def step_impl(context):
    target1 = context.browser.find_element_by_id('droppable')
    assert_equal("Dropped!", target1.text)