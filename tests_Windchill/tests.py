# Search and Open a Relevant wt.Document
import time
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome

def wait_for_window(self, timeout=2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
        return set(wh_now).difference(set(wh_then)).pop()


@pytest.mark.login
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
    driver.find_element(By.ID, "keywordkeywordField_SearchTextBox").send_keys("NewSeleniumTest")
    time.sleep(5)
    driver.find_element(By.ID, "searchExt").click()
    time.sleep(80)
    driver.find_element(By.CSS_SELECTOR, ".x-grid3-cell-inner.x-grid3-col-infoPageAction").click()
    time.sleep(10)
