#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on May 16, 2017

Course work: 

@author: 

Source:

'''
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random
from selenium.common.exceptions import NoSuchElementException

def get_random_int(start, end):
    return random.randint(start, end)


def get_git_info(driver, git_dev_url):
    
    driver.get(git_dev_url)
    
    time.sleep(get_random_int(5, 10))
    
    wait = WebDriverWait(driver, 100)
    
    
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'numbers-summary')))
    
    for elm in driver.find_elements_by_css_selector(".numbers-summary"):
        
        number_only = re.sub("[^0-9]",  # Search for all non-letters
                              "",          # Replace all non-letters with spaces
                              (elm.text))
        
    num_final = number_only[0:2]
    print("commits:" + num_final)
    num_final_2 = number_only[2:3]
    print("branch:" + num_final_2)
    num_final_3 = number_only[3:4]
    print("releases:" + num_final_3)
    
    num_final_4 = number_only[4:5]
    print("contributer:" + num_final_4)
    
    
    
    #wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'num')))
    
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'pagehead-actions')))
    
    
    for elm1 in driver.find_elements_by_css_selector(".pagehead-actions"):
        number_only_1 = re.sub("[^0-9]",  # Search for all non-letters
                              "",          # Replace all non-letters with spaces
                              (elm1.text))
        #print(number_only_1)
       
        num_final_4 = number_only_1[0:1]
        print("watch:" + num_final_4)
        num_final_5 = number_only_1[1:2]
        print("star:" + num_final_5)
        num_final_6 = number_only_1[2:3]
        print("fork:" + num_final_6)
        git_own_project = ''
        own = ''
        git_fork_project = ''
        other = ''
        if("0" in num_final_6 ):
            
            git_own_project += git_dev_url
            print("own project: ", git_own_project)
        else:
            
            git_fork_project += git_dev_url
            
            print("other project: ",git_fork_project)
                        
def main(git_links):

    # Google Chrome 
    driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
    
    driver.get('https://www.google.com/')
    
    for link in git_links:        
        #print(link)
        # do try catch
        try:
            get_git_info(driver, link)
            
        except NoSuchElementException:
            print('some error')
    
    print("Done!!")    

    
    

git_links= [
     'https://github.com/mateothegreat/k8-byexamples-ingress-controller',
     'https://github.com/rajacsp/sage',
     'https://github.com/rajacsp/drivercheck'
]
    
if __name__ == '__main__':
    main(git_links)
    
    
