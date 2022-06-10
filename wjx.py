import logging
import random
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
import numpy as np
import time

import conf


def choose_answer():
    try:
        choose_one(1)  # 各项均为相同概率，可省略不写。
        choose_one(2, [0.1, 0.2, 0.5, 0.2])
        choose_one(3, exclude=[2, 3])  # 排除第 3 题中，第 2, 3 个选项。
        choose_one(4, [0.4, 0.1, 0.2, 0.1, 0.2])
        choose_one(5, [0.2, 0.2, 0.1, 0.3, 0.2])
        choose_one(6, [0.25, 0.25, 0.25, 0.25])
        choose_one(7, [0.3, 0.2, 0.1, 0.4])
        choose_one(8, [0.2, 0.6, 0.2])
        choose_multiple(9, [0.3, 0.25, 0.2, 0.125, 0.125], 3)
        choose_multiple(10, [0.3, 0.25, 0.2, 0.15, 0.1])
        choose_one(11, [0.1, 0.1, 0.2, 0.6])
        choose_one(12, [0.2, 0.8])
        choose_multiple(13, [0.4, 0.2, 0.3, 0.1], 2)
        choose_multiple(14, [0.3, 0.3, 0.3, 0.1])
        choose_multiple(15, [0.2, 0.2, 0.1, 0.2, 0.2, 0.1])
        choose_multiple(16, [0.1, 0.2, 0.1, 0.3, 0.2, 0.1])
        choose_multiple(17, [0.25, 0.25, 0.25, 0.25])
        choose_multiple(18, [0.3, 0.3, 0.3, 0.1])
        choose_multiple(19, [0.2, 0.1, 0.3, 0, 0.1, 0.2, 0.1], 3)  # 非相同概率时，没必要用 exclude。
        choose_multiple(20)  # 各项均为相同概率，可省略不写。
        choose_one(21, [0.2, 0.4, 0.3, 0.1])
    except NoSuchElementException:
        logging.error("任务执行失败，请检查配置。")


def probabilities_generator(choices_num, exclude=None):
    if isinstance(exclude, list):
        choices_num -= len(exclude)
    probability = 1 / choices_num
    res = [probability for i in range(choices_num)]
    if exclude:
        for i in exclude:
            res.insert(i, 0)
    return res


def choose_one(question_number, question_probability=None, exclude=None):
    """
    :param question_number: int
    :param question_probability: [] # If you set it None, It will auto generate an averages list.
    :param exclude: [] # A list which question index you want to exclude.
    """
    el_choices = driver.find_elements(By.XPATH, f"//*[@id=\"div{question_number}\"]/div[2]/div")
    choices_num = len(el_choices)
    if not question_probability:
        question_probability = probabilities_generator(choices_num, exclude=exclude)
    chosen_number = np.random.choice(
        a=list(range(1, choices_num + 1)),
        p=question_probability
    )
    el_checked = driver.find_element(By.XPATH, f"//*[@id=\"div{question_number}\"]/div[2]/div[{chosen_number}]")
    el_checked.click()


def choose_multiple(question_number, question_probability=None, restrict=10000, exclude=None):
    el_options = driver.find_elements(By.XPATH, f"//*[@id=\"div{question_number}\"]/div[2]/div")
    choices_num = len(el_options)
    if not question_number:
        question_probability = probabilities_generator(choices_num, exclude=exclude)
    chosen_number = np.random.choice(
        a=list(range(1, choices_num + 1)),
        p=question_probability,
        size=random.randint(1, min(restrict, choices_num)),
        replace=False
    )
    for i in chosen_number:
        driver.find_element(By.XPATH, f"//*[@id=\"div{question_number}\"]/div[2]/div[{i}]").click()


def slider_move(loop_index, dest=380):
    """
    :param loop_index: int
    :param dest: int # A position where you want to move.
    """
    try:
        el_slider = WebDriverWait(driver, 10).until(
            presence_of_element_located(
                (By.XPATH, "//*[@id='nc_1__scale_text']/span"))
        )
        ActionChains(driver).click_and_hold(el_slider).perform()
        ActionChains(driver).move_by_offset(xoffset=dest, yoffset=0).perform()
        ActionChains(driver).release().perform()
    except (TimeoutException, ElementClickInterceptedException):
        logging.error(f"第{loop_index}次请求执行失败！")


def main():
    try:
        for i in range(loop_count):
            driver.get(question_url)
            try:
                driver.find_element(By.XPATH, '//*[@id="confirm_box"]/div[2]/div[3]/button[1]').click()  # 取消提示
            except NoSuchElementException:
                pass
            choose_answer()
            driver.find_element(By.XPATH, '//*[@id="ctlNext"]').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="alert_box"]/div[2]/div[2]/button').click()
            driver.find_element(By.XPATH, '//*[@id="rectMask"]').click()
            print(f"第 {i} 次任务执行成功。")
            try:
                WebDriverWait(driver, 15).until(
                    ec.url_changes(question_url)
                )
            except TimeoutException:
                slider_move(i, dest=380)  # 若验证码逃逸失败，请自行调教参数 dest
    except Exception:
        logging.error("任务执行错误，正在退出任务。")
    finally:
        driver.close()
        input()


if __name__ == '__main__':
    question_url = conf.QUESTION_URL or input("请输入问卷地址：")
    loop_count = conf.LOOP_COUNT or int(input("请输入填写次数："))
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option('excludeSwitches', ['enable-automation'])
    opt.add_experimental_option('useAutomationExtension', False)
    # driver = webdriver.Chrome(executable_path=r'./chromedriver', options=opt)
    # 库主估计是 Linux 党，鉴于大多数学生党使用 Windows，为了降低使用门槛，注释了该行。
    driver = webdriver.Chrome(options=opt)  # Windows下，将对应版本的 chromedriver 放置在 python 根目录，默认启用该行。
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                           {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})
    np.random.seed(int(time.time()))
    main()
