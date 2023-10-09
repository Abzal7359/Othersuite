from behave import *

from pages.PartnersPage import PartnerPage

from dataproviders import data


@when(u'click on setting to go back to dadshboard')
def step_impl(context):
    context.PP = PartnerPage(context.driver)
    context.PP.click_settings_link()



@when(u'click on partners')
def step_impl(context):
    context.PP.click_partners_link()



@when(u'click add partner')
def step_impl(context):
    context.PP = PartnerPage(context.driver)
    context.PP.click_add_partner_button()



@when(u'fill details with new mail and phone')
def step_impl(context):
    global emaill
    global mobile
    global fname
    global lname
    for i in context.table:

        lname = data.partner_name[1]
        fname = data.partner_name[0]
        emaill = data.partner_mail
        mobile = data.partner_phone

        context.PP.fill_partner_details(fname, lname, emaill, mobile)


@then(u'validate partner is added or not')
def step_impl(context):
    assert context.PP.validate_partner_added(emaill, mobile)


@when(u'fill details with same mail and other phone')
def step_impl(context):
    context.PP = PartnerPage(context.driver)
    for i in context.table:
        context.PP.fill_partner_detailss(fname, lname, emaill, data.partner_other_phone)



@then(u'validate the toaster message of duplicate')
def step_impl(context):
    assert context.PP.validate_duplicate_toaster_message()

@when(u'fill details with other mail and same phone')
def step_impl(context):
    context.PP = PartnerPage(context.driver)
    for i in context.table:
        context.PP.fill_partner_detailss(fname, lname, data.partner_other_mail, mobile)



@when(u'click on edit button on partner')
def step_impl(context):
    context.PP = PartnerPage(context.driver)
    context.PP.click_edit_button()


@when(u'edit details phone')
def step_impl(context):
    global edit_number
    for i in context.table:
        edit_number = data.update_phone
        context.PP.fill_phone_number(data.update_phone)



@then(u'validate updates got reflected or not')
def step_impl(context):
    assert context.PP.validate_updated_phone(edit_number)

