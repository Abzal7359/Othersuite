import time

from behave import *

from pages.projectUpdatePage import ProjectUpdatePage

#
# @when(u'click on settings button')
# def step_impl(context):
#     context.PUP=ProjectUpdatePage(context.driver)
#     context.PUP.click_settings_button()



@when(u'click on project updates tab')
def step_impl(context):
    context.PUP = ProjectUpdatePage(context.driver)
    context.PUP.click_project_updates_tab()



@when(u'in mile stone section click on AddMileStone')
def step_impl(context):
    context.PUP.click_AddMileStone()

@when(u'fill data in MileStone')
def step_impl(context):
    context.PUP.fill_data_inMilestone()


@then(u'check Mile stone is added or not')
def step_impl(context):
    assert context.PUP.check_mileStone_isAdded()


#--------------------------------------------------------------------
#code to add news letters


@when(u'click on NewsLetters Tab')
def step_impl(context):
    context.PUP = ProjectUpdatePage(context.driver)
    context.PUP.click_newsletters_tab()

@when(u'click on Add NewsLetter button')
def step_impl(context):
    context.PUP.click_add_newsletter_button()


@when(u'fill data in NewsLetter')
def step_impl(context):
    context.PUP.fill_newsletter_data("10-09-2023","C://Users/abzalhussain/Desktop/building.jpg")


@Then(u'check news letter is added or not')
def step_impl(context):
    assert context.PUP.check_newsletter_added()


#------------------------------------------------------------------------------------------------
#code to add videos
@when(u'click on videos Tab')
def step_impl(context):
    context.PUP = ProjectUpdatePage(context.driver)
    context.PUP.click_videos_tab()


@when(u'click on Add videos Button')
def step_impl(context):
    context.PUP.click_add_video_button()

@when(u'fill data in videos pop up')
def step_impl(context):
    context.PUP.fill_video_data("10-09-2023","https://bento.uat.propflo.in/project/onboard?projectEdit=true&projectId=643e4357e8f2f692a50952b3")

@Then(u'check the video is added or not')
def step_impl(context):
    assert context.PUP.check_video_added()
