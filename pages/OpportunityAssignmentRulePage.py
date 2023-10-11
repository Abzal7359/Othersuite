import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

label_text = []
class OpportunityAssignmentRulePage:
    def __init__(self,driver):
        self.driver=driver




    OPPORTUNITY_LINK = (By.XPATH, "(//a[text()='Opportunity'])[1]")
    DESELECT_ALL_BUTTON = (By.XPATH, "//div/div[2]/div[2]/div/button[1]")
    SELECTED_ITEMS_CHECKBOXES = (By.XPATH, "//input[contains(@id,'selectedItem-')]")
    ADD_NEW_RULE_BUTTON = (By.XPATH, "//div[@class='flex' and text()=' Add New Rule ']")
    RULE_NAME_INPUT = (By.ID, "name")
    INTEGRATION_TYPE_SOURCE_RADIO = (By.XPATH, "//input[@value='SOURCE']")
    INTEGRATION_TYPE_SOURCE_CAMPAIGN=(By.XPATH,"//form/div[1]/div[2]/div/div/div[2]/div/div/div[2]")

    SOURCE_DROPDOWN = (By.XPATH, "//form/div[1]/div[2]/div/div/div[3]/div[1]/div[1]/div/div")
    SELECT_DIGITAL_CHECKBOX = (By.XPATH, "//label[contains(normalize-space(),'Digi')]")
    ADD_SOURCE_BUTTON = (By.XPATH, "//label[normalize-space()='+ Add Source']")
    SELECT_INSTAGRAM_CHECKBOX = (By.XPATH, "//label[contains(normalize-space(),'Insta')]")

    USER_DROPDOWN = (By.XPATH, "//form/div[1]/div[2]/div/div/div[3]/div[2]/div[1]/div/div")
    SELECT_DIGITAL_USER_CHECKBOX = (By.XPATH, "//label[contains(normalize-space(),'Digi')]")
    SELECT_INSTAGRAM_USER_CHECKBOX = (By.XPATH, "//label[contains(normalize-space(),'Insta')]")
    SELECT_USER_BUTTON = (By.XPATH, "//button/span[text()='Select User']")
    SELECT_USER_LABEL = (By.XPATH, "//app-select-dropdown/div/div/div/div[4]/label")
    SAVE_BUTTON = (By.XPATH, "//button[normalize-space()='Save']")

    RULE_ROWS = (By.XPATH, "//tr/td[1]//*[local-name()='svg']")
    RULE_NAME_CELL = (By.XPATH, "//tr/td[3]")
    DELETE_RULE_BUTTON = (By.XPATH, "//p[normalize-space()='Delete']")
    TOAST_MESSAGE = (By.XPATH, "//app-toasts-container//p[1]//following-sibling::p")
    TABLE_BODY = (By.XPATH, "//tbody")
    CLONE_BUTTON = (By.XPATH, "//p[normalize-space()='Clone']")


    def is_rule_cloned(self,string):
        validate_rule_name = self.driver.find_element(By.XPATH, f"//tr[{lenth_rules + 1}]/td[3]").text

        self.driver.find_element(By.XPATH,
                                    f"//tr[{lenth_rules + 1}]/td[7]/div/button//*[local-name()='svg']").click()
        self.driver.find_element(*self.DELETE_RULE_BUTTON).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, f"//tr[{lenth_rules}]/td[7]/div/button//*[local-name()='svg']").click()
        self.driver.find_element(*self.DELETE_RULE_BUTTON).click()
        time.sleep(2)
        return string + rule_name == validate_rule_name







    def click_clone_button(self):
        self.driver.find_element(*self.CLONE_BUTTON).click()
        time.sleep(2)
        self.driver.find_element(*self.SAVE_BUTTON).click()
        time.sleep(2)




    def click_on_clone_option(self):
        self.driver.find_element(By.XPATH, f"//tr[{lenth_rules}]/td[7]/div/button//*[local-name()='svg']").click()

    def is_toast_message_displayed(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(self.TOAST_MESSAGE))
        return element.is_displayed()

    def click_to_update(self):
        self.driver.find_element(By.XPATH, "//form/div[1]/div[2]/div/div/div[3]/div/button[1]").click()
        self.driver.find_element(By.XPATH, "//app-select-dropdown/div/div/div/div[2]/label").click()
        self.driver.find_element(By.XPATH, "//label[normalize-space()='Campaigns']").click()
        self.driver.find_element(By.XPATH, "//form/div[1]/div[2]/div/div/div[4]/div/button[1]").click()
        self.driver.find_element(By.XPATH, "//app-select-dropdown/div/div/div/div[3]/label").click()
        self.driver.find_element(By.XPATH, "(//label[normalize-space()='Select Users'])[1]").click()
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Update']").click()
        time.sleep(2)



    def click_on_assigne(self):
        self.driver.find_element(By.XPATH, f"//tr[{lenth_rules}]/td[3]").click()
        time.sleep(3)

    def select_users_and_save(self):
        self.driver.find_element(*self.SELECT_USER_BUTTON).click()
        self.driver.find_element(*self.SELECT_USER_LABEL).click()
        self.driver.find_element(By.XPATH, "(//label[normalize-space()='Select Users'])[1]").click()
        self.driver.find_element(*self.SAVE_BUTTON).click()
        time.sleep(2)


    def fill_rule_details_campaign(self):
        global rule_name
        rule_name = "AllDigital"
        self.driver.find_element(*self.RULE_NAME_INPUT).send_keys(rule_name)
        self.driver.find_element(*self.INTEGRATION_TYPE_SOURCE_CAMPAIGN).click()
        self.driver.find_element(By.XPATH, "//form/div[1]/div[2]/div/div/div[3]/div/button[1]").click()
        self.driver.find_element(By.XPATH, "//app-select-dropdown/div/div/div/div[3]/label").click()
        self.driver.find_element(By.XPATH, "//label[normalize-space()='Campaigns']").click()

    def is_rule_not_added(self):
        wait = WebDriverWait(self.driver, 10)
        # toaster=(self.TOAST_MESSAGE)
        element = wait.until(EC.visibility_of_element_located((self.TOAST_MESSAGE)))
        if element.is_displayed():

            return True
        else:

            return False



    def select_integration_type_source(self):
        self.driver.find_element(*self.INTEGRATION_TYPE_SOURCE_RADIO).click()

    def is_rule_deleted(self):
        flagone = True
        for j in range(1, lenth_rules):
            v = self.driver.find_element(By.XPATH, f"//tr[{j}]/td[3]").text
            if v == rule_name:
                flagone = False
                break
            else:
                pass
        return flagone

    def click_delete_rule_button(self):
        self.driver.find_element(By.XPATH, f"//tr[{lenth_rules}]/td[7]/div/button//*[local-name()='svg']").click()
        self.driver.find_element(*self.DELETE_RULE_BUTTON).click()
        time.sleep(2)


    def is_rule_disabled(self):
        validate_rule_name = self.driver.find_element(By.XPATH, f"//tr[{lenth_rules}]/td[3]").text
        return rule_name == validate_rule_name

    def click_disable_on_rule(self):
        self.driver.find_element(By.XPATH, f"//tr[{lenth_rules - 1}]/td[2]/label").click()
        time.sleep(2)

    def is_rule_dropped(self):
        validate_rule_name = self.driver.find_element(By.XPATH, f"//tr[{lenth_rules - 1}]/td[3]").text
        return rule_name == validate_rule_name


    def drag_and_drop_rule(self):
        source_element = self.driver.find_element(By.XPATH, f"//tr[{lenth_rules}]/td[1]//*[local-name()='svg']")
        target_element = self.driver.find_element(By.XPATH, f"//tr[{lenth_rules-1}]/td[1]//*[local-name()='svg']")
        action = ActionChains(self.driver)
        (action
         .click_and_hold(source_element)
         .move_to_element(target_element)
         .release(target_element)
         .perform())
        time.sleep(2)


    def is_rule_added(self):

        global lenth_rules
        lenth_rules = len(self.driver.find_elements(By.XPATH, "//tr/td[1]//*[local-name()='svg']"))
        validate_rule_name = self.driver.find_element(By.XPATH, f"//tr[{lenth_rules}]/td[3]").text
        return rule_name == validate_rule_name


    def fill_source_detials(self):
        self.driver.find_element(*self.SOURCE_DROPDOWN).click()
        self.driver.find_element(*self.SELECT_DIGITAL_CHECKBOX).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[1]/div[1]/div[2]/div/button[1]").click()
        self.driver.find_element(By.XPATH, "//label[contains(normalize-space(),'Face')]").click()
        self.driver.find_element(By.XPATH, "//div[1]/div[1]/div[2]/div/button[1]").click()
        self.driver.find_element(*self.ADD_SOURCE_BUTTON).click()

        self.driver.find_element(By.XPATH, "//form/div[1]/div[2]/div/div/div[3]/div[2]/div[1]/div/div").click()
        self.driver.find_element(By.XPATH, "//label[contains(normalize-space(),'Digi')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[2]/div[1]/div[2]/div/button[1]").click()
        self.driver.find_element(*self.SELECT_INSTAGRAM_CHECKBOX).click()
        self.driver.find_element(By.XPATH, "//div[2]/div[1]/div[2]/div/button[1]").click()

        self.driver.find_element(*self.SELECT_USER_BUTTON).click()
        self.driver.find_element(By.XPATH, "//app-select-dropdown/div/div/div/div[4]/label").click()
        self.driver.find_element(By.XPATH, "(//label[normalize-space()='Select Users'])[1]").click()
        self.driver.find_element(*self.SAVE_BUTTON).click()
        time.sleep(2)


    def fill_rule_details(self):
        global rule_name
        rule_name = "AllDigital"
        self.driver.find_element(*self.RULE_NAME_INPUT).send_keys(rule_name)
        self.driver.find_element(*self.INTEGRATION_TYPE_SOURCE_RADIO).click()

    def click_opportunity_link(self):
        self.driver.find_element(*self.OPPORTUNITY_LINK).click()

    def deselect_all_assignees(self):
        global l
        self.driver.find_element(*self.DESELECT_ALL_BUTTON).click()
        time.sleep(2)

        l = self.driver.find_elements(*self.SELECTED_ITEMS_CHECKBOXES)

        for i in range(len(l) - 1):
            if self.driver.find_element(By.XPATH, f"(//input[contains(@id,'selectedItem-{i}')])").is_selected():
                label_text.append(self.driver.find_element(By.XPATH,f"(//input[contains(@id,'selectedItem-{i}')])//following-sibling::label").text)
                self.driver.find_element(By.XPATH, f"(//input[contains(@id,'selectedItem-{i}')])").click()

        self.driver.refresh()
        time.sleep(5)

    def is_last_deselected_person_selected(self):
        flag = True
        self.driver.find_element(*self.DESELECT_ALL_BUTTON).click()
        time.sleep(2)
        for i in range(len(l) - 1):
            checkbox_xpath = f"//input[contains(@id,'selectedItem-{i}')]"
            checkbox = self.driver.find_element(By.XPATH, checkbox_xpath)

            if checkbox.is_selected():
                after_text = checkbox.find_element(By.XPATH, "./following-sibling::label").text
                if after_text == label_text[-1]:
                    flag = True
                    break
                else:
                    flag = False

        return flag

    def select_another_assignee(self):
        global ttext
        for i in range(len(l) - 1):
            checkbox_xpath = f"//input[contains(@id,'selectedItem-{i}')]"
            checkbox = self.driver.find_element(By.XPATH, checkbox_xpath)

            if not checkbox.is_selected():
                ttext = checkbox.find_element(By.XPATH, "./following-sibling::label").text
                checkbox.click()
                break

        self.driver.refresh()
        time.sleep(3)

    def assignee_added_to_default_assignment(self):
        self.driver.find_element(*self.DESELECT_ALL_BUTTON).click()
        time.sleep(2)
        check=True
        for i in range(len(l) - 1):
            if self.driver.find_element(By.XPATH, f"(//input[contains(@id,'selectedItem-{i}')])").is_selected():
                if self.driver.find_element(By.XPATH, f"(//input[contains(@id,'selectedItem-{i}')])//following-sibling::label").text == ttext:
                    self.driver.find_element(By.XPATH, "//div/div[2]/div[2]/div/button[1]").click()
                    return True





    def click_add_new_rule(self):
        # self.driver.refresh()
        time.sleep(3)
        self.driver.find_element(*self.ADD_NEW_RULE_BUTTON).click()
        time.sleep(3)





