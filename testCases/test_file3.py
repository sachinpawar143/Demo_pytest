import time

import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")


class Test_002:

    def test_sum_005(self):
        a = 3
        b = 4
        sum = a + b
        if sum == 7:
            assert True
        else:
            assert False

    def test_credence(self):

        #driver = webdriver.Chrome()
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://credence.in/")
        offers = driver.find_element(By.XPATH, "//span[@class='text-white b label']").text
        print(offers)
        print(driver.title)
        if driver.title == "Credence":
            driver.close()
            assert True  # test case status -->Pass
        else:
            driver.close()
            assert False  # test cases status --> Fail



    def test_credence_(self):

        #driver = webdriver.Chrome()
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://credence.in/")
        time.sleep(1)
        driver.find_element(By.XPATH, "//img[@src='/website/images/enquiry.png']").click()
        time.sleep(2)
        l= len(driver.find_elements(By.XPATH, "//div[@class ='quickfinder-description gem-text-output']//p//a"))
        list =[]
        for r in range (1, l+1):
                contact = driver.find_element(By.XPATH, "//div[@class ='quickfinder-description gem-text-output']//p//a["+str(r)+"]").text
                #print(contact)
                list.append(contact)

        if "+91 9091929355" in list:
            assert True
        else:
            assert False

