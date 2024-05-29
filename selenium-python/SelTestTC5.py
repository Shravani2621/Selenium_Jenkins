# Editing and Modifying Attributes
import time
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import openpyxl


def wait_for_window(self, timeout=2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
        return set(wh_now).difference(set(wh_then)).pop()


@pytest.mark.login
def test():
    driver = webdriver.Edge()
    domain = "http://inbr2wks-249497:3000/"
    driver.get(domain)
    driver.set_window_size(1500, 1100)
    time.sleep(2)

    path = r"C:\Users\sss927879\Desktop\Book1.xlsx"
    b = openpyxl.load_workbook(path)
    sheet = b.active
    c1 = sheet.cell(row=5, column=1)
    driver.find_element(By.NAME, "username").send_keys(c1.value)
    driver.find_element(By.NAME, "password").send_keys(c1.value)
    time.sleep(5)

    # driver.find_element(By.NAME, "username").send_keys("infodba")
    # driver.find_element(By.NAME, "password").send_keys("infodba")
    # time.sleep(5)
    # driver.find_element(By.CSS_SELECTOR, ".sw-button.accent-caution").click()
    # time.sleep(10)
    # driver.find_element(By.CSS_SELECTOR,
    #                     ".sw-column.aw-tile-tileContainer.aw-theme-locationsTile.aw-tile-smallSize").click()
    # time.sleep(15)
    # driver.find_element(By.CSS_SELECTOR, ".sw-aria-border:nth-child(4)").click()
    # time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".sw-button.accent-caution").click()
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, ".aw-uiwidgets-searchBox").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".aw-search-globalSearchLinksPanel1").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".aw-panel-header svg").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div["
                                  "2]/div[1]/div[1]/div[1]/aside[1]/div[2]/form[1]/div[2]/div[1]/div[1]/div[1]/label["
                                  "1]/div[1]/input[1]").clear()
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div["
                                  "2]/div[1]/div[1]/div[1]/aside[1]/div[2]/form[1]/div[2]/div[1]/div[1]/div[1]/label["
                                  "1]/div[1]/input[1]").send_keys("Item..")
    # driver.find_element(By.CSS_SELECTOR, "li:nth-child(6) > .sw-aria-border > .sw-row").click()
    time.sleep(5)
    keyboard = Controller()
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, ".sw-property:nth-child(2) > .sw-property-val").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".sw-property:nth-child(2) > .sw-property-val").send_keys("TestItemEP")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".sw-button > div").click()
    time.sleep(10)
    # driver.find_element(By.CSS_SELECTOR, ".aw-commands-commandIconButton.aw-commands-command.aw-commandId"
    #                                      "-Awp0OpenGroup.aw-commands-commandWrapperVertical").click()
    # time.sleep(5)
    # driver.find_element(By.CSS_SELECTOR, ".aw-popup-command-bar:nth-child(1)").click()
    # time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".aw-commandId-Awp0OpenGroup").click()
    time.sleep(15)
    driver.find_element(By.CSS_SELECTOR, ".aw-list-command:nth-child(1)").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".aw-commandId-Awp0EditGroup").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".aw-list-command:nth-child(2)").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".aw-commandId-Awp0EditGroup").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".aw-list-command:nth-child(1) > .sw-aria-border").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".aw-layout-workareaMain").click()
    time.sleep(5)
    driver.find_element(By.NAME, "object_name").clear()
    driver.find_element(By.NAME, "object_name").send_keys("NewItemTest")
    time.sleep(5)
    driver.find_element(By.NAME, "object_desc").send_keys("New Item to test.")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".aw-commandId-Awp0EditGroup").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".aw-list-command:nth-child(1)").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".aw-commandId-Awp0EditGroup").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".aw-list-command:nth-child(2)").click()
    time.sleep(10)
