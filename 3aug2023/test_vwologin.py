import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_vwologin():
    logger = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    email_address_ele = driver.find_element(By.ID, "login-username")
    password_ele = driver.find_element(By.NAME, "password")
    sign_in_btn_ele = driver.find_element(By.ID, "js-login-btn")
    email_address_ele.send_keys("93npu2yyb0@esiix.com")
    password_ele.send_keys("Wingify@123")
    sign_in_btn_ele.click()
    time.sleep(5)
    assert "Dashboard" in driver.title
