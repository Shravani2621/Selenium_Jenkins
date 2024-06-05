# check out, edit, check in
import time
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome

# @pytest.mark.login
def test():
    driver = Chrome()
    username = "traininguser"
    password = "traininguser"
    domain = "inblrwks-247927.tatatechnologies.com:8090/Windchill/app/"
    # domain = "inblrwks-247927.tatatechnologies.com:8080/Windchill/app/#ptc1/homepage"
    driver.get("http://{}:{}@{}".format(username, password, domain))

    driver.find_element(By.ID, "ext-gen112").click()
    time.sleep(5)
    driver.find_element(By.ID, "ext-gen63").click()
    time.sleep(5)
    driver.find_element(By.ID, "keywordkeywordField_SearchTextBox").send_keys("newSeleniumTest")
    time.sleep(5)
    driver.find_element(By.ID, "searchExt").click()
    time.sleep(8)
    driver.find_element(By.CSS_SELECTOR, ".x-grid3-cell-inner.x-grid3-col-infoPageAction").click()
    time.sleep(10)
    # driver.find_element(By.XPATH, "//td[9]/div/a/img").click()
    # time.sleep(5)
    driver.find_element(By.ID, "infoPagedetailsPageActionsMenu").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//span[contains(.,'Check Out and Edit')]").click()
    time.sleep(5)
    p = driver.current_window_handle
    chwd = driver.window_handles
    for w in chwd:
        if w != p:
            driver.switch_to.window(w)
    time.sleep(15)
    # driver.find_element(By.ID, "PTC_WC_DESCRIPTION").click()
    # driver.find_element(By.ID, "PTC_WC_DESCRIPTION").send_keys("Selenium Testing")
    # time.sleep(2)
    # driver.find_element(By.ID, "edit_wizard_save").click()
    driver.find_element(By.ID, "edit_wizard_checkin").click()
    time.sleep(5)
    driver.find_element(By.ID, "PJL_wizard_ok").click()
    time.sleep(5)
