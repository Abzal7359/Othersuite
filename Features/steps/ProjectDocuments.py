from behave import *

from pages.projectUpdatePage import ProjectUpdatePage




@when(u'click on project documents')
def step_impl(context):
    context.PUP=ProjectUpdatePage(context.driver)
    context.PUP.click_project_documents_tab()


@when(u'click on Add document')
def step_impl(context):
    context.PUP.click_On_Add_document()

@when(u'fill details in upload documents pop up')
def step_impl(context):
    context.PUP.fill_data_to_AddDocuments()

@Then(u'validate document is uploaded or not in project documents')
def step_impl(context):
    assert context.PUP.check_document_uploaded()

