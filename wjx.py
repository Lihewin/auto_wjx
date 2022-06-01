from lib2to3.pgen2 import driver
import random
from time import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
import numpy as np
import time

opt = webdriver.ChromeOptions()
opt.add_experimental_option('excludeSwitches', ['enable-automation'])
opt.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(executable_path=r'./chromedriver', options=opt)
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                           {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})

np.random.seed(int(time.time()))

def choose_one(question_number, question_probabilty):
    number_of_choices = len(driver.find_elements(By.XPATH,f"//*[@id=\"div{question_number}\"]/div[2]/div"))
    chosen_number = np.random.choice(list(range(1,number_of_choices+1)),p = question_probabilty)
    driver.find_element(By.XPATH,f"//*[@id=\"div{question_number}\"]/div[2]/div[{chosen_number}]").click()

def choose_multiple(question_number, question_probabilty, restrict = 10000):
    number_of_choices = len(driver.find_elements(By.XPATH,f"//*[@id=\"div{question_number}\"]/div[2]/div"))
    chosen_number = np.random.choice(list(range(1,number_of_choices+1)),p = question_probabilty, size = random.randint(1,min(restrict,number_of_choices)), replace = False)
    for i in chosen_number:
        driver.find_element(By.XPATH,f"//*[@id=\"div{question_number}\"]/div[2]/div[{i}]").click()


try:
    driver.get("https://www.wjx.cn/vm/wE5Js0M.aspx")
    choose_one(1, [0.5,0.5])
    choose_one(2, [0.1,0.2,0.5,0.2])
    choose_one(3, [0.6,0.3,0.1])
    choose_one(4, [0.4,0.1,0.2,0.1,0.2])
    choose_one(5, [0.2,0.2,0.1,0.3,0.2])
    choose_one(6, [0.25,0.25,0.25,0.25])
    choose_one(7, [0.3,0.2,0.1,0.4])
    choose_one(8, [0.2,0.6,0.2])
    choose_multiple(9, [0.3,0.25,0.2,0.125,0.125], 3)
    choose_multiple(10, [0.3,0.25,0.2,0.15,0.1])
    choose_one(11, [0.1,0.1,0.2,0.6])
    choose_one(12, [0.2,0.8])
    choose_multiple(13, [0.4,0.2,0.3,0.1], 2)
    choose_multiple(14, [0.3,0.3,0.3,0.1])
    choose_multiple(15, [0.2,0.2,0.1,0.2,0.2,0.1])
    choose_multiple(16, [0.1,0.2,0.1,0.3,0.2,0.1])
    choose_multiple(17, [0.25,0.25,0.25,0.25])
    choose_multiple(18, [0.3,0.3,0.3,0.1])
    choose_multiple(19, [0.2,0.1,0.1,0.2,0.1,0.2,0.1],3)
    choose_multiple(20, [0.25,0.25,0.25,0.25])
    choose_one(21, [0.2,0.4,0.3,0.1])

    driver.find_element_by_xpath('//*[@id="ctlNext"]').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="alert_box"]/div[2]/div[2]/button').click()
    driver.find_element_by_xpath('//*[@id="rectMask"]').click()
    check = WebDriverWait(driver, 15).until(ec.invisibility_of_element_located((By.XPATH, "//*[@id=\"rectMask\"]")))
    
except:
    pass

driver.close()