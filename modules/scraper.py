from copy import deepcopy as copy
from selenium import webdriver
from check_results import check_results
from time import sleep
from actions import take_action
import os
import config
import itertools

BASE_URL = os.environ.get('BASE_URL', config.BASE_URL)
BASE_YEAR = os.environ.get('BASE_URL', config.BASE_YEAR)
FIELDS = os.environ.get('FIELDS', config.FIELDS)
DEPARTMENT_FIELD = os.environ.get('DEPARTMENT_FIELD', config.DEPARTMENT_FIELD)
EXCLUDES = os.environ.get('EXCLUDES', config.EXCLUDES)




class scraper:
    def __init__(self):
        #self.driver = webdriver.PhantomJS(executable_path="D:/phantomjs/bin/phantomjs.exe")
        self.driver = webdriver.PhantomJS()
        self.driver.get(BASE_URL)
        self.submit_button = self.driver.find_element_by_id('submit1')
        self.options = {}
        self.courses = {}

    def populate(self):

        for field in FIELDS:
            opList = []
            el = self.driver.find_element_by_id(field)
            for option in el.find_elements_by_tag_name('option'):
                if field in  EXCLUDES and option.text in EXCLUDES[field]:
                    continue
                if field == "lstYearOfExam":
                    if int(option.text)>=2017:
                        opList.append(option)
                else:
                    if len(option.text)>1:
                        opList.append(option)

            self.options[field] = opList

        big_list = [self.options[field] for field in FIELDS]
        self.combinations = list(itertools.product(*big_list))

    def print_population(self):

        for field in self.options:
            print("The field is: {}. The options are:".format(field))
            for option in self.options[field]:
                print(option.text)



    def navigate(self,setup):

        comb_id = 0

        while comb_id < len(self.combinations):
            comb = self.combinations[comb_id]
            comb = list(comb)
            arguments = []
            for option in comb:
                option.click()
                arguments.append(option.text)
                #print(option.text)

            el = self.driver.find_element_by_id(DEPARTMENT_FIELD)
            self.depts = [dept for dept in el.find_elements_by_tag_name('option')]

            i = 0

            while i < len(self.depts):
                #print("dept",i)
                dept = self.depts[i]
                dept.click()
                deptName = dept.text
                self.submit_button.click()
                sleep(0.1)

                source = self.driver.page_source
                outBool = check_results(source)
                print(deptName, arguments[3:5])
                if outBool == True:
                    print("True")
                    args = copy(arguments)
                    args.append(deptName)
                    take_action(args,setup)

                self.driver.back()
                self.submit_button = self.driver.find_element_by_id('submit1')
                el = self.driver.find_element_by_id(DEPARTMENT_FIELD)
                self.depts = [dept for dept in el.find_elements_by_tag_name('option')]

                i += 1

            self.populate()
            comb_id += 1

