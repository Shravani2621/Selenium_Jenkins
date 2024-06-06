# Advanced Search: Search a part with criteria and saving the search
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
    time.sleep(2)
    driver.find_element(By.ID, "ext-gen63").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".ng-pristine.ng-untouched.ng-valid.ng-empty").send_keys("newSeleniumTest")
    time.sleep(5)
    driver.find_element(By.ID, "saveThisSearchLink").click()
    time.sleep(5)
    driver.find_element(By.NAME, "searchName").send_keys("new test")
    time.sleep(2)
    driver.find_element(By.ID, "ext-comp-1027").click()
    # driver.find_element(By.ID, "ext-comp-1143").click()
    time.sleep(2)
    driver.find_element(By.ID, "extSearchButtonDiv").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".x-grid3-cell-inner.x-grid3-col-infoPageAction").click()
    time.sleep(10)
    # driver.find_element(By.XPATH, "//td[9]/div/a/img").click()
    # time.sleep(25)
