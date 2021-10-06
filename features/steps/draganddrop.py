from behave import given, when, then

@given(u'the user navigate to the URL https://qavbox.github.io/demo/dragndrop/')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user navigate to the URL https://qavbox.github.io/demo/dragndrop/')


@when(u'he drag and drop the grey square in the blue square')
def step_impl(context):
    raise NotImplementedError(u'STEP: When he drag and drop the grey square in the blue square')


@then(u'he sees a message "Dropped!"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then he sees a message "Dropped!"')
