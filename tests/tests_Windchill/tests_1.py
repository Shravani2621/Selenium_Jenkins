# create new part

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
    driver.find_element(By.CSS_SELECTOR, "#object_main_navigation_nav > .mnemonic").click()
    time.sleep(5)
    driver.find_element(By.ID, "ext-gen35").click()
    time.sleep(5)
    driver.implicitly_wait(20)
    driver.find_element(By.CSS_SELECTOR, ".x-tree-ec-icon").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR,
                        ".x-tree-node:nth-child(1) > .x-tree-node-leaf > .x-tree-node-anchor > span").click()
    time.sleep(5)
    driver.find_element(By.ID, "infoPagedetailsPageActionsMenu").click()
    time.sleep(5)
    driver.find_element(By.ID, "object_folderbrowser_toolbar_new_submenu_infoPagedetailsPageActionsMenu_menu").click()
    time.sleep(5)
    # driver.find_element(By.ID, "ext-comp-1174").click()
    driver.find_element(By.ID, "ext-comp-1058").click()
    time.sleep(5)
    p = driver.current_window_handle
    chwd = driver.window_handles
    for w in chwd:
        # switch focus to child window
        if w != p:
            driver.switch_to.window(w)

    time.sleep(5)
    driver.find_element(By.ID, "ext-gen37").click()
    time.sleep(5)
    driver.find_element(By.ID, "!~objectHandle~partHandle~!createType").click()
    dropdown = driver.find_element(By.ID, "!~objectHandle~partHandle~!createType")
    time.sleep(5)
    dropdown.find_element(By.ID,
                          "_u33__u126_objectHandle_u126_partHandle_u126__u33_createType_wt_u46_part_u46_WTPart").click()
    driver.find_element(By.ID,
                        "_u33__u126_objectHandle_u126_partHandle_u126__u33_createType_wt_u46_part_u46_WTPart").click()
    driver.find_element(By.NAME, "tcomp$attributesTable$OR:wt.pdmlink.PDMLinkProduct:1186180$___null!~objectHandle"
                                 "~partHandle~!_col_name___textbox").click()
    driver.find_element(By.NAME, "tcomp$attributesTable$OR:wt.pdmlink.PDMLinkProduct:1186180$___null!~objectHandle"
                                 "~partHandle~!_col_name___textbox").send_keys("newSeleniumTest")
    time.sleep(5)
    driver.find_element(By.ID, "ext-gen38").click()
    driver.find_element(By.ID, "PJL_wizard_ok").click()
