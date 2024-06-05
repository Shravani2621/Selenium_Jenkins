# Create a document
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
    driver.find_element(By.CSS_SELECTOR, "#object_main_navigation_nav > .mnemonic").click()
    driver.find_element(By.ID, "ext-gen35").click()
    driver.implicitly_wait(20)
    driver.find_element(By.CSS_SELECTOR, ".x-tree-ec-icon").click()
    driver.find_element(By.CSS_SELECTOR,
                        ".x-tree-node:nth-child(1) > .x-tree-node-leaf > .x-tree-node-anchor > span").click()
    driver.find_element(By.ID, "infoPagedetailsPageActionsMenu").click()
    time.sleep(5)
    driver.find_element(By.ID, "object_folderbrowser_toolbar_new_submenu_infoPagedetailsPageActionsMenu_menu").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//span[contains(.,'New Document')]").click()
    time.sleep(5)
    p = driver.current_window_handle
    chwd = driver.window_handles
    for w in chwd:
        if w != p:
            driver.switch_to.window(w)

    driver.find_element(By.NAME, "document$create$OR:wt.pdmlink.PDMLinkProduct:1186180$|components$loadWizardStep$OR"
                                 ":wt.pdmlink.PDMLinkProduct:1186180$"
                                 "|document$createDocumentSetTypeAndAttributesWizStep$OR:wt.pdmlink.PDMLinkProduct"
                                 ":1186180$___createType___combobox").click()
    time.sleep(5)
    driver.find_element(By.ID, "createType_wt_u46_doc_u46_WTDocument").click()
    time.sleep(5)
    driver.find_element(By.ID, "primary0contentSourceList").click()
    time.sleep(5)
    driver.find_element(By.ID, "primary0contentSourceList_NONE").click()
    # driver.find_element(By.ID, "NameInputId548121795397200").click()
    driver.find_element(By.NAME, "tcomp$attributesTable$OR:wt.pdmlink.PDMLinkProduct:1186180$___name_col_name___textbox").send_keys("Selenium")
    time.sleep(5)
    driver.find_element(By.NAME, "tcomp$attributesTable$OR:wt.pdmlink.PDMLinkProduct"
                                 ":1186180$___Location_col_overrideFolder___radio").click()
    time.sleep(2)
    driver.find_element(By.ID, "PJL_wizard_ok").click()
    time.sleep(5)
