
from behave import *

from selenium.webdriver.common.by import By

from pages.OpportunityAssignmentRulePage import OpportunityAssignmentRulePage

label_text = []

@when(u'click on opportunity in Assignmnet Rules')
def step_impl(context):
    context.OAP=OpportunityAssignmentRulePage(context.driver)
    context.OAP.click_opportunity_link()


@when(u'deselect all assignes')
def step_impl(context):
    context.OAP.deselect_all_assignees()



@when(u'check last deselcted person is selected or not after refresh page')
def step_impl(context):

    assert context.OAP.is_last_deselected_person_selected()


@when(u'now select another assigne')
def step_impl(context):
    context.OAP = OpportunityAssignmentRulePage(context.driver)
    context.OAP.select_another_assignee()



@then(u'valiadte assigne added or not in default assignment')
def step_impl(context):
    assert context.OAP.assignee_added_to_default_assignment()

@when(u'click on Add new rule')
def step_impl(context):
    context.OAP = OpportunityAssignmentRulePage(context.driver)
    context.OAP.click_add_new_rule()


@when(u'fill details rule_name and integration_type is source')
def step_impl(context):
    context.OAP.fill_rule_details()

@when(u'fill source details and select users and click save')
def step_impl(context):
    context.OAP.fill_source_detials()


@then(u'validate rule added or not')
def step_impl(context):
    assert context.OAP.is_rule_added()

@when(u'drag and drop the created rule one position minus')
def step_impl(context):
    context.OAP = OpportunityAssignmentRulePage(context.driver)
    context.OAP.drag_and_drop_rule()


@then(u'validate it is droped or not')
def step_impl(context):
    assert context.OAP.is_rule_dropped()


@when(u'click disable button on created rule')
def step_impl(context):
    context.OAP = OpportunityAssignmentRulePage(context.driver)
    context.OAP.click_disable_on_rule()

@then(u'check the rule is in bootom in list or not')
def step_impl(context):
    assert context.OAP.is_rule_disabled()


@when(u'click on delete option on rule and delete')
def step_impl(context):
    context.OAP = OpportunityAssignmentRulePage(context.driver)
    context.OAP.click_delete_rule_button()



@then(u'validate rule is deleted or not by checking the rule name in rule list')
def step_impl(context):
    assert context.OAP.is_rule_deleted()


@when(u'fill details  integration_type is source')
def step_impl(context):
    context.OAP = OpportunityAssignmentRulePage(context.driver)
    context.OAP.select_integration_type_source()




@Then(u'validate rule is not added')
def step_impl(context):
    assert context.OAP.is_rule_not_added()
    c=context.driver.find_element(By.XPATH,"//tbody")
    context.driver.execute_script("arguments[0].click()",c)





@when(u'fill details rule_name integration_type is Campaign')
def step_impl(context):
    context.OAP = OpportunityAssignmentRulePage(context.driver)
    context.OAP.fill_rule_details_campaign()

@when(u'select users and click save')
def step_impl(context):
    context.OAP.select_users_and_save()


@when(u'click on assigne')
def step_impl(context):
    context.OAP = OpportunityAssignmentRulePage(context.driver)
    context.OAP.click_on_assigne()


@when(u'update details you want to change and click update')
def step_impl(context):
    context.OAP.click_to_update()




@Then(u'validate the toaster displayed or not after updation')
def step_impl(context):
    assert context.OAP.is_toast_message_displayed()

@when(u'click on clone option of rule')
def step_impl(context):
    context.OAP = OpportunityAssignmentRulePage(context.driver)
    context.OAP.click_on_clone_option()


@when(u'click clone button')
def step_impl(context):
    context.OAP.click_clone_button()



@Then(u'validate by name or in which the text "{string}" is added')
def step_impl(context,string):
    assert context.OAP.is_rule_cloned(string)
