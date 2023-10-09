import time

from behave import *
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.projectUpdatePage import ProjectUpdatePage


@when(u'click on the settings button')
def step_impl(context):
    context.PUP = ProjectUpdatePage(context.driver)
    context.PUP.click_settings_button()


@when(u'click on edit button')
def step_impl(context):
    edit = context.driver.find_element(By.XPATH, "//button[normalize-space()='Edit']")
    context.driver.execute_script("arguments[0].click()", edit)


@when(u'fill details which are editable')
def step_impl(context):
    for i in context.table:
        global projectname
        global TotalArea
        global description
        projectname=i["projectname"]
        TotalArea=i["TotalArea"]
        description=i["description"]

        context.driver.find_element(By.XPATH, "//button[normalize-space()='Remove']").click()
        context.driver.find_element(By.XPATH, "//input[@class='hidden']").send_keys("C://Users/abzalhussain/Desktop/building.jpg")
        context.driver.find_element(By.XPATH, "(//button[normalize-space()='Save'])[1]").click()
        # project name
        context.driver.find_element(By.XPATH, "(//input[@id='name'])[1]").clear()
        context.driver.find_element(By.XPATH, "(//input[@id='name'])[1]").send_keys(projectname)
        context.driver.find_element(By.XPATH, "(//input[@id='totalArea'])[1]").clear()
        context.driver.find_element(By.XPATH, "(//input[@id='totalArea'])[1]").send_keys(TotalArea)
        context.driver.find_element(By.XPATH, "(//input[@id='address'])[1]").clear()
        context.driver.find_element(By.XPATH, "(//input[@id='address'])[1]").send_keys(i["location"], Keys.ENTER)
        ele=context.driver.find_element(By.XPATH, "(//textarea[@id='description'])[1]")
        context.driver.execute_script("arguments[0].scrollIntoView();", ele)
        context.driver.find_element(By.XPATH, "(//textarea[@id='description'])[1]").clear()
        context.driver.find_element(By.XPATH, "(//textarea[@id='description'])[1]").send_keys(i["description"])


@when(u'edit contact details')
def step_impl(context):
    for j in context.table:
        global phonenumberone
        global phonenumbertwo
        global emailone
        global emailtwo
        phonenumberone=j["phonenumberone"]
        phonenumbertwo=j["phonenumbertwo"]
        emailone=j["emailone"]
        emailtwo=j["emailtwo"]

        # phone number
        context.driver.find_element(By.XPATH, "(//input[@id='phone-number'])[1]").clear()
        context.driver.find_element(By.XPATH, "(//input[@id='phone-number'])[1]").send_keys(phonenumberone)
        if len(context.driver.find_elements(By.XPATH, "(//input[@id='phone-number'])")) == 2:
            pass
        else:
            context.driver.find_element(By.XPATH, "//span[normalize-space()='+ Add Mobile Number']").click()
        context.driver.find_element(By.XPATH, "(//input[@id='phone-number'])[2]").clear()
        context.driver.find_element(By.XPATH, "(//input[@id='phone-number'])[2]").send_keys(phonenumbertwo)

        context.driver.find_element(By.XPATH, "(//input[@type='email'])[1]").clear()
        context.driver.find_element(By.XPATH, "(//input[@type='email'])[1]").send_keys(emailone)
        if len(context.driver.find_elements(By.XPATH, "(//input[@type='email'])")) == 2:
            pass
        else:
            context.driver.find_element(By.XPATH, "//span[normalize-space()='+ Add Email']").click()
        context.driver.find_element(By.XPATH, "(//input[@type='email'])[2]").clear()
        context.driver.find_element(By.XPATH, "(//input[@type='email'])[2]").send_keys(emailtwo)



@when(u'image uploading and clicking update button')
def step_impl(context):
    # images uploading
    context.driver.find_element(By.XPATH, "(//input[@id='file-upload'])[1]").send_keys(
        "C://Users/abzalhussain/Desktop/builldingone.jpg")
    time.sleep(3)

    # update
    js = context.driver.find_element(By.XPATH, "(//button[normalize-space()='Update'])[1]")
    context.driver.execute_script("arguments[0].click()", js)
    time.sleep(2)

@when(u'select Amenities in edit')
def step_impl(context):
    global n
    n = 10
    for i in range(1, n + 1):
        if i % 2 == 0:
            c = f"(//form/div/div/div[10]/div[3]/div)[{i}]"
            context.driver.find_element(By.XPATH, c).click()



@then(u'check all editied details got updated or not')
def step_impl(context):
    flags=[]
    y=True
    z=False

    # validation
    projectnameupdated = context.driver.find_element(By.XPATH, "//div[@class='mt-14']//label").text
    if projectname == projectnameupdated:
        flags.append(y)
    else:
        flags.append(z)
    TotalareaUpdated = context.driver.find_element(By.XPATH, "//app-project-onboard/div/div[2]/main/div[2]/div/div/div/div[1]/div[2]/div").text
                                                            #//app-project-onboard/div/div[2]/main/div[2]/div/div/div/div[1]/div[2]/div
    if TotalareaUpdated == TotalArea:
        flags.append(True)
    else:
        flags.append(z)
    mailsUpdated = context.driver.find_element(By.XPATH, "//app-project-onboard/div/div[2]/main/div[2]/div/div/div/div[2]/div").text
    if emailone and emailtwo in mailsUpdated:
        flags.append(True)
    else:
        flags.append(z)

    phonenumberupdated = context.driver.find_element(By.XPATH,
                                             "//app-project-onboard/div/div[2]/main/div[2]/div/div/div/div[3]/div").text
    if phonenumberone and phonenumbertwo in phonenumberupdated:
        flags.append(True)
    else:
        flags.append(z)

    descriptionchanged = context.driver.find_element(By.XPATH,
                                             "//app-project-onboard/div/div[2]/main/div[2]/div/div/div/div[4]/div").text
    if description == descriptionchanged:
        flags.append(True)
    else:
        flags.append(z)

    count = n / 2
    amenitiescount = len(context.driver.find_elements(By.XPATH, "//app-project-onboard/div/div[2]/main/div[2]/div/div/div/div[5]/div[2]/span"))

    if amenitiescount <= count:
        flags.append(True)
    else:
        flags.append(False)

    updatedimagescount = len(context.driver.find_elements(By.XPATH, "//app-project-onboard/div/div[2]/main/div[2]/div/div/div/div[6]/span/div/div/img"))
    if updatedimagescount >= 1:
        flags.append(True)
    else:
        flags.append(z)

    # print(flags)
    assert False not in flags




