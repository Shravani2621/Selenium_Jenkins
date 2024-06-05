# Create a promotion request
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
    time.sleep(3)
    driver.find_element(By.XPATH, "//span[contains(.,'New')]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//span[contains(.,'New Promotion Request')]").click()
    time.sleep(3)
    p = driver.current_window_handle
    chwd = driver.window_handles
    for w in chwd:
        if w != p:
            driver.switch_to.window(w)
    time.sleep(3)
    # driver.find_element(By.ID, "name1250206631266200").clear() driver.find_element(By.ID,
    # "name1250206631266200").send_keys("Promotion Req 1") driver.find_element(By.INPUT,
    # "#name1250206631266200.required").send_keys("Promotion Request 1") driver.find_element(By.NAME,
    # "tcomp$attributesTable$VR:wt.part.WTPart:1292906$___name_col_name___textbox").clear() driver.find_element(
    # By.NAME, "tcomp$attributesTable$VR:wt.part.WTPart:1292906$___name_col_name___textbox").send_keys(
    # "PromotionReq1") time.sleep(2)
    driver.find_element(By.ID, "PJL_wizard_next").click()
    time.sleep(5)
    driver.find_element(By.NAME, "promotionRequest$promotionStateSelection$$___maturityState___combobox").click()
    # driver.find_element(By.XPATH, "//span[contains(.,'Released')]").click()
    driver.find_element(By.ID, "maturityState_RELEASED").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".x-grid3-row-checker").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".x-btn-text.blist").click()
    time.sleep(5)
    driver.find_element(By.ID, "PJL_wizard_next").click()
    time.sleep(5)
    # driver.find_element(By.NAME, "APPROVER#OR:wt.org.WTUser:1182376#53").click()
    # time.sleep(3)
    # driver.find_element(By.CSS_SELECTOR, ".x-grid3-cell-inner.x-grid3-col-REVIEWER > "
    #                                      "#REVIEWER#OR:wt.org.WTUser:1182376#53").click()
    # driver.find_element(By.NAME, "REVIEWER#OR:wt.org.WTUser:1182376#53").click()
    driver.find_element(By.ID, "PJL_wizard_ok").click()
    time.sleep(5)
