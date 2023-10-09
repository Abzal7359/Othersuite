from selenium.webdriver.common.by import By
import time


class PartnerPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators

    SETTINGS_LINK = (By.XPATH, "//div[text()='Settings']")
    PARTNERS_LINK = (By.XPATH, "(//a[text()=' Partners '])[2]")
    ADD_PARTNER_BUTTON = (By.XPATH, "//div[text()=' Add Partner ']")
    FIRST_NAME_INPUT = (By.ID, "first-name ")
    LAST_NAME_INPUT = (By.ID, "last-name")
    EMAIL_INPUT = (By.ID, "email")
    PHONE_NUMBER_INPUT = (By.ID, "phone-number")
    SAVE_BUTTON = (By.XPATH, "//button[normalize-space()='Save']")
    TOASTER_MESSAGE = (By.XPATH, "//app-toasts-container/div/div/div/div/div/div[2]/p[2]")
    EDIT_OPTION_BUTTON = (By.XPATH, "//td[5]/div//*[local-name()='svg']")
    EDIT_BUTTON = (By.XPATH, "//p[text()='Edit']")

    UPDATE_BUTTON = (By.XPATH, "//button[normalize-space()='Update']")

    def click_settings_link(self):
        self.driver.find_element(*self.SETTINGS_LINK).click()
        time.sleep(3)

    def click_partners_link(self):
        self.driver.find_element(*self.PARTNERS_LINK).click()
        time.sleep(1)

    def click_add_partner_button(self):
        self.driver.find_element(*self.ADD_PARTNER_BUTTON).click()
        time.sleep(1)

    def fill_partner_details(self, first_name, last_name, email, phone):
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.PHONE_NUMBER_INPUT).send_keys(phone)
        self.driver.find_element(*self.SAVE_BUTTON).click()
        time.sleep(5)
    def fill_partner_detailss(self, first_name, last_name, email, phone):
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.PHONE_NUMBER_INPUT).send_keys(phone)
        self.driver.find_element(*self.SAVE_BUTTON).click()
        time.sleep(4)

    def validate_partner_added(self, expected_email, expected_phone):
        textt = self.driver.find_element(By.XPATH, "(//td[3])[1]").text
        number = self.driver.find_element(By.XPATH, "(//td[4])[1]").text
        return textt == expected_email and expected_phone in number

    def validate_duplicate_toaster_message(self):
        warn = self.driver.find_element(*self.TOASTER_MESSAGE).text
        return warn == "Channel partner already exist"

    def click_edit_button(self):
        self.driver.find_element(*self.EDIT_OPTION_BUTTON).click()
        self.driver.find_element(*self.EDIT_BUTTON).click()
        time.sleep(1)

    def fill_phone_number(self, phone):
        self.driver.find_element(*self.PHONE_NUMBER_INPUT).clear()
        self.driver.find_element(*self.PHONE_NUMBER_INPUT).send_keys(phone)
        self.driver.find_element(*self.UPDATE_BUTTON).click()
        time.sleep(2)

    def validate_updated_phone(self, expected_phone):
        val_number = self.driver.find_element(By.XPATH, "(//td[4])[1]").text
        return expected_phone in val_number
