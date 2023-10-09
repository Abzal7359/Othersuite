import configparser
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

config = configparser.ConfigParser()
config.read(r'config.txt')

class ProjectUpdatePage:
    def __init__(self,driver):
        self.driver=driver

    SETTINGS_BUTTON = (By.XPATH, "//app-topbar/div/div/div[2]/div[1]/img[@alt='Settings logo']")
    PROJECT_UPDATES_TAB = (By.XPATH, "//a[text()=' Project Updates ']")
    TOWER_SELECTION_BUTTON = (By.XPATH, "//form/div/div[2]/div[1]/div/div/div/button[1]")
    TOWER_SELECT_LABEL = (By.XPATH, "(//app-select-dropdown/div/div/div/div/label)[1]")
    DATE_INPUT = (By.XPATH, "//input[@type='date']")
    MILESTONE_DESCRIPTION_INPUT = (By.XPATH, "//input[@placeholder='Enter MileStone Here']")
    FILE_UPLOAD_INPUT = (By.XPATH, "//input[@id='file-upload - ']")
    SAVE_BUTTON =(By.XPATH, "//button[normalize-space()='Save']")
    Mile_News_video_button=(By.XPATH,"(//div[@class='flex justify-between'])[1]")
    NEWSLETTERS_TAB = (By.XPATH, "//a[@id='NEWSLETTER']")
    NEWSLETTER_TITLE_INPUT = (By.XPATH, "//form/div/div[2]/div[1]/input")
    DESCRIPTION_INPUT = (By.XPATH, "//input[@placeholder='Enter Description Here']")
    NEWSLETTER_ITEM =(By.XPATH, "//app-project-updates/div/div/div[2]/div/div/span")
    VIDEOS_TAB = (By.XPATH, "//a[@id='VIDEO']")
    EMBEDDED_VIDEO_LINK_INPUT = (By.XPATH, "//input[@placeholder='Place the Embedded Video Link Here']")
    VIDEO_ITEM = (By.XPATH, "//app-project-updates/div/div/div[2]/div/div/span")
    PROJECT_DOCUMENTS_TAB = (By.XPATH, "//a[@id='property-documents']")
    DOCUMENTS_LIST = (By.XPATH, "//app-project-documents/div/div[2]/div")


    def check_document_uploaded(self):
        documentslist_after = len(self.driver.find_elements(*self.DOCUMENTS_LIST))
        # self.driver.find_element(By.XPATH,"//div[text()='Settings']").click()
        return documentslist_after > documentslist_before


    def fill_data_to_AddDocuments(self):
        self.driver.find_element(By.XPATH, "(//button[contains(@class,'w-full border border-gray-300 ')])[1]").click()
        self.driver.find_element(By.XPATH, "//app-select-dropdown/div/div/div/div[3]").click()
        self.driver.find_element(*self.FILE_UPLOAD_INPUT).send_keys(
            "C://Users/abzalhussain/Desktop/building.jpg")
        wt = WebDriverWait(self.driver, 10)
        element = wt.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']")))
        element.click()
        time.sleep(2)
    def click_On_Add_document(self):
        self.driver.find_element(*self.Mile_News_video_button).click()

    def click_project_documents_tab(self):
        global documentslist_before
        self.driver.find_element(*self.PROJECT_DOCUMENTS_TAB).click()
        time.sleep(2)
        documentslist_before = len(self.driver.find_elements(*self.DOCUMENTS_LIST))

    def fill_video_data(self, date,  video_link):
        # date addding
        self.driver.find_element(*self.DATE_INPUT).send_keys(date)

        self.driver.find_element(*self.DESCRIPTION_INPUT).send_keys("video collection")

        self.driver.find_element(*self.EMBEDDED_VIDEO_LINK_INPUT).send_keys(video_link)
        wt = WebDriverWait(self.driver, 10)
        element = wt.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']")))
        element.click()
        time.sleep(2)

    def check_video_added(self):
        zz = len(self.driver.find_elements(*self.VIDEO_ITEM))
        return zz > video_list


    def click_add_video_button(self):
        self.driver.find_element(*self.Mile_News_video_button).click()

    def click_videos_tab(self):
        global video_list
        self.driver.find_element(*self.VIDEOS_TAB).click()
        time.sleep(float(config.get('waiting_time', 'min_wait')))
        video_list = len(self.driver.find_elements(*self.VIDEO_ITEM))

    def check_newsletter_added(self):
        zz = f"(//app-project-updates/div/div/div[2]/div/div/span)[{list_len + 1}]"
        c = self.driver.find_element(By.XPATH, zz).text
        return News_letter_tittle in c

    def fill_newsletter_data(self,  date, file_path):
        global News_letter_tittle
        News_letter_tittle = "news of new tower"
        self.driver.find_element(*self.NEWSLETTER_TITLE_INPUT).send_keys(News_letter_tittle)
        # date addding
        self.driver.find_element(*self.DATE_INPUT).send_keys(date) #"10-09-2023"
        self.driver.find_element(*self.DESCRIPTION_INPUT).send_keys("all flats are under construction")
        self.driver.find_element(*self.FILE_UPLOAD_INPUT).send_keys(file_path)
        #"C://Users/abzalhussain/Desktop/building.jpg"
        # for clicking save
        wt = WebDriverWait(self.driver, 10)
        element = wt.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']")))
        element.click()
        time.sleep(float(config.get('waiting_time', 'min_wait')))




    def click_add_newsletter_button(self):
        self.driver.find_element(*self.Mile_News_video_button).click()

    def click_newsletters_tab(self):
        global list_len
        self.driver.find_element(*self.NEWSLETTERS_TAB).click()
        time.sleep(float(config.get('waiting_time', 'min_wait')))
        list_len = len(self.driver.find_elements(*self.NEWSLETTER_ITEM))

    def click_settings_button(self):
        self.driver.find_element(*self.SETTINGS_BUTTON).click()
        time.sleep(float(config.get('waiting_time', 'min_wait')))


    def click_project_updates_tab(self):
        self.driver.find_element(*self.PROJECT_UPDATES_TAB).click()
        time.sleep(1)

    def click_AddMileStone(self):
        global lenth
        lenth = len(self.driver.find_elements(By.XPATH, "//app-project-updates/div/div/div[2]/div[2]/div"))

        self.driver.find_element(*self.Mile_News_video_button).click()

    def fill_data_inMilestone(self):
        global gett
        self.driver.find_element(*self.TOWER_SELECTION_BUTTON).click()
        gett = self.driver.find_element(*self.TOWER_SELECT_LABEL).text
        self.driver.find_element(*self.TOWER_SELECT_LABEL).click()
        # date addding
        self.driver.find_element(*self.DATE_INPUT).send_keys("10-09-2023")
        self.driver.find_element(*self.MILESTONE_DESCRIPTION_INPUT).send_keys("all flats are sold")
        self.driver.find_element(*self.FILE_UPLOAD_INPUT).send_keys("C://Users/abzalhussain/Desktop/building.jpg")
        # for clicking save
        wt = WebDriverWait(self.driver, 10)
        element = wt.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']")))
        element.click()
        time.sleep(float(config.get('waiting_time', 'min_wait')))

    def check_mileStone_isAdded(self):
        zz = f"//app-project-updates/div/div/div[2]/div[2]/div[{lenth + 1}]/div/span"
        c = self.driver.find_element(By.XPATH, zz).text
        return gett == c