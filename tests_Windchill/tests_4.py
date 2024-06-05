# Adding a Document to a wt.Part as Described by Document
import time
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_window(self, timeout=2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
        return set(wh_now).difference(set(wh_then)).pop()


@pytest.mark.login
def test():
    driver = webdriver.Edge()
    username = "traininguser"
    password = "traininguser"
    domain = "inblrwks-247927.tatatechnologies.com:8090/Windchill/app/"
    # domain = "inblrwks-247927.tatatechnologies.com:8080/Windchill/app/#ptc1/homepage"
    driver.get("http://{}:{}@{}".format(username, password, domain))

    driver.find_element(By.ID, "ext-gen112").click()
    driver.find_element(By.CSS_SELECTOR, "#object_main_navigation_nav > .mnemonic").click()
    time.sleep(2)
    driver.find_element(By.ID, "ext-gen35").click()
    driver.implicitly_wait(20)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".x-tree-ec-icon").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,
                        ".x-tree-node:nth-child(2) > .x-tree-node-leaf > .x-tree-node-anchor > span").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".x-grid3-cell-inner.x-grid3-col-infoPageAction").click()
    time.sleep(2)
    driver.find_element(By.ID, "infoPageinfoPanelID__infoPage_myTab_object_partInfoRelatedItemsTab").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".x-btn-text.blist").click()
    time.sleep(5)
    if WebDriverWait(driver, 10).until(EC.alert_is_present()):
        driver.switch_to.alert.accept()
        time.sleep(5)
        p = driver.current_window_handle
    else:
        p = driver.current_window_handle
    chwd = driver.window_handles
    for w in chwd:
        if w != p:
            driver.switch_to.window(w)
    time.sleep(5)
    driver.find_element(By.ID, "name1_SearchTextBox").send_keys("*")
    time.sleep(2)
    driver.find_element(By.NAME, "pickerSearch").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".x-grid3-row-checker").click()
    time.sleep(2)
    driver.find_element(By.ID, "PJL_wizard_ok").click()
    time.sleep(2)
