from xml.etree.ElementPath import xpath_tokenizer
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
import os


def text_answer(url):
    option = ChromeOptions()
    option.add_argument('--disable-dev-shm-usage')
    # option.add_argument("start-maximized") # open Browser in maximized mode
    #option.add_argument('--headless')
    option.add_argument('--no-sandbox')
    #option.add_argument("start-maximized")
    option.binary_location = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
    option.add_argument('--user-data-dir=C:/Users/43440/AppData/Local/Google/Chrome/User Data')
    # driver = webdriver.Chrome(executable_path='C:/Program Files/Google/Chrome/Application/chromedriver.exe')  # Optional argument, if not specified will search path.
    service = ChromeService(executable_path='C:/Program Files/Google/Chrome/Application/chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=option)
#'https://cares-copilot.com/CARES-Copilot'
    driver.get(url)
    time.sleep(3)
    #time.sleep(10000)
    history = driver.find_elements(By.XPATH, "//div[@class='flex justify-start item']")
    # print(history)
    # print(len(history))
    input = driver.find_element(By.XPATH, "//textarea[@class='el-textarea__inner']")
    button = driver.find_element(By.XPATH, "//div[@class='flex items-center justify-center cursor-pointer send-btn']")
    button.click()
    input.send_keys('怎么治疗感冒')
    time.sleep(10)
    if url.__contains__('pro'):
        print("pro")
        time.sleep(10)
    now = driver.find_elements(By.XPATH, "//div[@class='flex justify-start item']")
    div = now[len(now) - 1]
    # if len(now)>2:
    #     div=now[len(now)-2]
    # elif len(now)==0:
    #     div=now
    # print("here")
    # print(type(div))
    # print(div.text)
    time.sleep(10)
    son_div = div.find_element(By.XPATH, "//div[@class='markdown-body']")
   # temp=son_div.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "p")))
    temp = son_div.find_element(By.TAG_NAME, 'p')
    #print(len(temp))
    res=''
    # if len(temp)>=1:
    #     # #for p in temp:
    #     #     #print(p.get_attribute('text-content'))
    #     # print('temp[0]', temp[0])
    #     # print('temp[0].text',temp[0].get_attribute('text'))
    #     res= temp[0].get_attribute('text-content')
    # else:
    time.sleep(5)
    #res= temp.get_attribute('text_content')
    res = temp.get_attribute('innerHTML')
    print('response',res)
    #time.sleep(10000)
    #response=son_div.find_elements(By.TAG_NAME, 'p')
    time.sleep(5)
    driver.quit()
    result = len(now) - len(history)
    if result == 2 and res != '':
        return("pass")
    else:
        print('result',result)
        print('response',res)
        return("fail")

def image_answer(url):
    option = ChromeOptions()
    option.add_argument('--disable-dev-shm-usage')
    # option.add_argument("start-maximized") # open Browser in maximized mode
    # option.add_argument('--headless')
    option.add_argument('--no-sandbox')
    # option.add_argument("start-maximized")
    option.binary_location = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
    option.add_argument('--user-data-dir=C:/Users/43440/AppData/Local/Google/Chrome/User Data')
    # driver = webdriver.Chrome(executable_path='C:/Program Files/Google/Chrome/Application/chromedriver.exe')  # Optional argument, if not specified will search path.
    service = ChromeService(executable_path='C:/Program Files/Google/Chrome/Application/chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=option)
    # 'https://cares-copilot.com/CARES-Copilot'
    driver.get(url)
    time.sleep(3)
    # time.sleep(10000)
    #history = driver.find_elements(By.XPATH, "//div[@class='flex justify-start item']")
    new_chat_button=driver.find_element(By.XPATH, "//div[@class='flex items-center justify-center cursor-pointer new-btn']")
    new_chat_button.click()
    time.sleep(1)
    img_button=driver.find_element(By.XPATH,"//img[@class='cursor-pointer up-btn']")
    img_button.click()
    time.sleep(1)
    img_input=driver.find_element(By.XPATH,"//input[@type='file']")
    img_input.send_keys('C:/Users/43440/OneDrive/Desktop/test.jpg')
    time.sleep(2)
    submit_button=driver.find_element(By.XPATH, "//div[@class='text-center cursor-pointer submit']")
    submit_button.click()
    time.sleep(2)
    #time.sleep(10000)
    img_select=driver.find_element(By.XPATH, "//div[@class='flex items-start']")
    img_select.click()

    input = driver.find_element(By.XPATH, "//textarea[@class='el-textarea__inner']")
    button = driver.find_element(By.XPATH, "//div[@class='flex items-center justify-center cursor-pointer send-btn']")
    button.click()
    input.send_keys('怎么治疗感冒')
    time.sleep(10)
    now = driver.find_elements(By.XPATH, "//div["
                                         "@class='flex justify-start item']")
    div = now[len(now) - 1]
    # if len(now)>2:
    #     div=now[len(now)-2]
    # elif len(now)==0:
    #     div=now
    # print("here")
    # print(type(div))
    # print(div.text)
    time.sleep(10)
    son_div = div.find_element(By.XPATH, "//div[@class='markdown-body']")
    # temp=son_div.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "p")))
    temp = son_div.find_element(By.TAG_NAME, 'p')
    # print(len(temp))
    res = ''
    # if len(temp)>=1:
    #     # #for p in temp:
    #     #     #print(p.get_attribute('text-content'))
    #     # print('temp[0]', temp[0])
    #     # print('temp[0].text',temp[0].get_attribute('text'))
    #     res= temp[0].get_attribute('text-content')
    # else:
    time.sleep(5)
    # res= temp.get_attribute('text_content')
    res = temp.get_attribute('innerHTML')
    print('response', res)
    # time.sleep(10000)
    # response=son_div.find_elements(By.TAG_NAME, 'p')
    time.sleep(5)
    driver.quit()
    result = len(now) - 0
    print('result', result)
    if result == 2 and res != '':
        return ("pass")
    else:
        print('result', result)
        print('response', res)
        return ("fail")




def test_answer():
    url1='https://cares-copilot.com/CARES-Copilot'
    url2='http://cares-copilot-pro.com/cares-copilot/CARES-Copilot'

    assert text_answer(url1) == "pass"
    time.sleep(2)
    assert text_answer(url2) == "pass"
    #pytest_runtest_makereport()
def test_image_answer():
    url1 = 'https://cares-copilot.com/CARES-Copilot'
    url2 = 'http://cares-copilot-pro.com/cares-copilot/CARES-Copilot'
    assert image_answer(url2) == "pass"

# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#      out = yield
#      report =out.get_result()
#      print(out)
#      print("hello")
#      print(report)
#      print(report.when)
#      print(report.nodeid)
#      print(report.outcome)
