from behave import *
from pages.projectUpdatePage import ProjectUpdatePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


@when(u'click on settings gear image')
def step_impl(context):
    time.sleep(3)
    context.PUP = ProjectUpdatePage(context.driver)
    context.PUP.click_settings_button()


@when(u'click on email templates and Add template')
def step_impl(context):
    global wait
    wait = WebDriverWait(context.driver, 30)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Email Templates']"))).click()
    time.sleep(2)
    # clicking add template
    wait.until(EC.element_to_be_clickable((By.ID, 'openModal'))).click()


@when(u'fill email template details')
def step_impl(context):
    global name
    name = "Payment Template"
    wait.until(EC.visibility_of_element_located((By.ID, 'templateName'))).send_keys(name)
    context.driver.find_element(By.ID, "subject").send_keys("Pay in Time")
    context.driver.find_element(By.XPATH, "//button[text()=' Placeholder ']").click()
    context.driver.find_element(By.XPATH, "(//app-select-dropdown/div/div/div/div/label)").click()
    time.sleep(3)
    e=context.driver.find_element(By.XPATH, "(//*[name()='svg'][@class='w-4 h-4'])[2]")
    context.driver.execute_script("arguments[0].scrollIntoView();", e)
    time.sleep(2)
    e.click()
    time.sleep(2)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//div[2]/div[1]/div[3]/div/div/div/input'))).click()
    context.driver.find_element(By.XPATH, "(//button[normalize-space()='Save'])").click()
    time.sleep(2)


@when(u'save email template')
def step_impl(context):
    context.driver.find_element(By.XPATH, "(//button[normalize-space()='Save'])").click()
    time.sleep(3)


@when(u'go to leads list and click bulk actions send mail')
def step_impl(context):
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Settings')]"))).click()
    act = ActionChains(context.driver)
    (act
     .move_to_element(context.driver.find_element(By.XPATH, "//span[contains(text(),'Sales')]"))

     .move_to_element(context.driver.find_element(By.XPATH, "//a[normalize-space()='Leads']"))
     .click()
     .perform())
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Bulk Actions']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Message']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//p[normalize-space()='Email']"))).click()


@then(u'Verify whether the template you created is present in the templates selection')
def step_impl(context):
    flag = False
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Templates')]"))).click()
    elements = context.driver.find_elements(By.XPATH, "//app-select-dropdown/div/div/div/div")
    for i in elements:
        if i.text == name:
            flag = True

            break
    assert flag


@when(u'close modal')
def step_impl(context):
    wait.until(EC.element_to_be_clickable((By.XPATH, "//form/div[1]/div[1]/div/div[2]//*[name()='svg']"))).click()


@when(u'click on email templates')
def step_impl(context):
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Email Templates']"))).click()
    time.sleep(2)


@when(u'click on delete on email template')
def step_impl(context):
    ele = context.driver.find_elements(By.XPATH, "//tbody/tr/td[1]/span")
    for i in range(1, len(ele) + 1):
        c = context.driver.find_element(By.XPATH, f"//tbody/tr[{i}]/td[1]/span").text
        if c == name:
            context.driver.find_element(By.XPATH, f"//tbody/tr[{i}]/td[4]/div//*[name()='svg']").click()
            context.driver.find_element(By.XPATH, "//button[normalize-space()='Delete']").click()
            context.driver.find_element(By.XPATH, "(//button[normalize-space()='Yes'])[1]").click()
            time.sleep(3)
            break


@Then(u'validate email template deleted or not')
def step_impl(context):

    flag = True
    ele = context.driver.find_elements(By.XPATH, "//tbody/tr/td[1]/span")
    for i in range(1, len(ele) + 1):
        c = context.driver.find_element(By.XPATH, f"//tbody/tr[{i}]/td[1]/span").text
        if c == name:
            flag = False
            break

    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Settings')]"))).click()
    assert flag


@when(u'click disable on template')
def step_impl(context):
    ele = context.driver.find_elements(By.XPATH, "//tbody/tr/td[1]/span")
    for i in range(1, len(ele) + 1):
        c = context.driver.find_element(By.XPATH, f"//tbody/tr[{i}]/td[1]/span").text
        if c == name:
            context.driver.find_element(By.XPATH, f"//tbody/tr[{i}]/td[1]/div/span").click()
            time.sleep(3)
            break


@Then(u'Verify whether the template you disabled is not present in the templates selection')
def step_impl(context):
    flag = True
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Templates')]"))).click()
    elements = context.driver.find_elements(By.XPATH, "//app-select-dropdown/div/div/div/div")
    for i in elements:
        if i.text == name:
            flag = False

            break
    assert flag


@when(u'click on edit and update it')
def step_impl(context):
    ele = context.driver.find_elements(By.XPATH, "//tbody/tr/td[1]/span")
    for i in range(1, len(ele) + 1):
        c = context.driver.find_element(By.XPATH, f"//tbody/tr[{i}]/td[1]/span").text
        if c == name:
            context.driver.find_element(By.XPATH, f"//tbody/tr[{i}]/td[4]/div//*[name()='svg']").click()
            context.driver.find_element(By.XPATH, "//button[normalize-space()='Edit']").click()
            time.sleep(2)
            context.driver.find_element(By.XPATH, " //div[@class='angular-editor-textarea']").clear()
            context.driver.find_element(By.XPATH, "//button[normalize-space()='Update']").click()
            time.sleep(2)
            break


@Then(u'validate the toaster of update')
def step_impl(context):
    cc = context.driver.find_element(By.XPATH,
                                     "//app-toasts-container/div/div/div/div/div/div[2]/p[2]").text
    assert cc == 'Email template updated successfully'
