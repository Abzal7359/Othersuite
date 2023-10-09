from behave import *
from selenium.webdriver.common.by import By

from pages.OpportunityAssignmentRulePage import OpportunityAssignmentRulePage


@when(u'click on leads under Assignment Rules')
def step_impl(context):
    context.driver.find_element(By.XPATH, "(//a[text()='Leads'])[1]").click()


@when(u'click on Add new _rule')
def step_impl(context):
    context.OAP = OpportunityAssignmentRulePage(context.driver)
    context.OAP.click_add_new_rule()


@when(u'fill details rule_name and integration_type is _source')
def step_impl(context):
    context.OAP.fill_rule_details()

@when(u'fill source details and select users and click _save')
def step_impl(context):
    context.OAP.fill_source_detials()

@then(u'validate rule added or _not')
def step_impl(context):
    assert context.OAP.is_rule_added()


@when(u'drag and drop the created rule one position _minus')
def step_impl(context):
    context.OAP = OpportunityAssignmentRulePage(context.driver)
    context.OAP.drag_and_drop_rule()

@then(u'validate it is droped or _not')
def step_impl(context):
    assert context.OAP.is_rule_dropped()

@when(u'click disable button on created _rule')
def step_impl(context):
    context.OAP = OpportunityAssignmentRulePage(context.driver)
    context.OAP.click_disable_on_rule()

@then(u'check the rule is in bootom in list or _not')
def step_impl(context):
    assert context.OAP.is_rule_disabled()


@when(u'click on delete option on rule and _delete')
def step_impl(context):
    context.OAP = OpportunityAssignmentRulePage(context.driver)
    context.OAP.click_delete_rule_button()

@then(u'validate rule is deleted or not by checking the rule name in rule _list')
def step_impl(context):
    assert context.OAP.is_rule_deleted()

@when(u'fill details  integration_type is _source')
def step_impl(context):
    context.OAP = OpportunityAssignmentRulePage(context.driver)
    context.OAP.select_integration_type_source()

@then(u'validate rule is not _added')
def step_impl(context):
    assert context.OAP.is_rule_not_added()
    c = context.driver.find_element(By.XPATH, "//tbody")
    context.driver.execute_script("arguments[0].click()", c)

@when(u'fill details rule_name integration_type is _Campaign')
def step_impl(context):
    context.OAP = OpportunityAssignmentRulePage(context.driver)
    context.OAP.fill_rule_details_campaign()


@when(u'select users and click _save')
def step_impl(context):
    context.OAP.select_users_and_save()


@when(u'click on _assigne')
def step_impl(context):
    context.OAP = OpportunityAssignmentRulePage(context.driver)
    context.OAP.click_on_assigne()


@when(u'update details you want to change and click _update')
def step_impl(context):
    context.OAP.click_to_update()



@Then(u'validate the toaster displayed or not after _updation')
def step_impl(context):
    assert context.OAP.is_toast_message_displayed()

@when(u'click on clone option of _rule')
def step_impl(context):
    context.OAP = OpportunityAssignmentRulePage(context.driver)
    context.OAP.click_on_clone_option()


@when(u'click clone _button')
def step_impl(context):
    context.OAP.click_clone_button()

@then(u'validate by name or in which the text "{string}" is _added')
def step_impl(context,string):
    assert context.OAP.is_rule_cloned(string)
