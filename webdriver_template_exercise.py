from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.set_window_size(1024, 600)
driver.maximize_window()
driver.delete_all_cookies()
action = ActionChains(driver)


driver.get("link")
driver.execute_script("window.scrollTo(0, 50);")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from info import *



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.maximize_window()
driver.delete_all_cookies()
wait = WebDriverWait(driver, 10)

driver.get("https://mhrs.gov.tr/vatandas/#/")
driver.implicitly_wait(30)
driver.find_element(By.ID, "LoginForm_username").send_keys(tc_id)
driver.find_element(By.ID, "LoginForm_password").send_keys(password)
driver.find_element(By.XPATH, "//*[@id=\"vatandasApp\"]/div[2]/div[2]/div[2]/form/div[4]/div/div/span/button").click()
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[2]/button[1]")))
driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[2]/button[1]").click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"vatandasApp\"]/section/main/div/div[1]/div[1]/div[1]/div[3]/div/div/div[2]")))
driver.find_element(By.XPATH, "//*[@id=\"vatandasApp\"]/section/main/div/div[1]/div[1]/div[1]/div[3]/div/div/div[2]").click()
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div:nth-child(10) > div > div.ant-modal-wrap > div > div.ant-modal-content > div > div > div.ant-modal-confirm-body > div > div > button.ant-btn.randevu-turu-button.genel-arama-button.ant-btn-lg")))
driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(10) > div > div.ant-modal-wrap > div > div.ant-modal-content > div > div > div.ant-modal-confirm-body > div > div > button.ant-btn.randevu-turu-button.genel-arama-button.ant-btn-lg").click()
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ant-select-selection__placeholder")))
driver.find_element(By.CLASS_NAME, "ant-select-selection__placeholder").click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"rc-tree-select-list_1\"]/ul/li[1]/span[2]")))
driver.find_element(By.XPATH, "//*[@id=\"rc-tree-select-list_1\"]/ul/li[1]/span[2]").click()

sleep(3000)
