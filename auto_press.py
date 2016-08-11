import json
import random
import time

import pyautogui
import sys
import selenium

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.

class ProTyper:
    def __init__(self, lesson, exercise, type_speed=0.1, type_speed_randomize=0.1):
        """ With this tool type like a boss."""
        self.lesson = lesson
        self.exercise = exercise
        self.type_speed = type_speed
        self.type_speed_randomize = type_speed_randomize
        self.driver = None

    @staticmethod
    def json_read(filename=''):
        """ Loads a .json file that contains all the key chains."""
        if not filename:
            print 'filename cannot be empty.'
            return

        try:
            with open('resources\\' + filename) as chain_json:
                chain_data = json.load(chain_json)
        except IOError:

            filename += '.json'

            try:
                with open('resources\\' + filename) as chain_json:
                    chain_data = json.load(chain_json)
            except IOError as e:
                print e
                return

        return chain_data

    def execute_chain(self):
        """ presses on keyes retrieved from json data with given speed."""
        # read complete document with all key chains
        chain = self.json_read('document')

        # prints keys to press for comparison
        print 'Keys to Press: ' + chain[self.lesson][self.exercise]

        # shows all pressed keys
        print 'Keys Pressed: ',

        # retrieve current lessons and exercise keychain
        for key in chain[self.lesson][self.exercise]:
            print key,
            # press on current key
            pyautogui.press(key)
            # calculate sleep time based on speed and a randomise factor
            r = random.uniform(self.type_speed - self.type_speed_randomize, self.type_speed + self.type_speed_randomize)

            # never drop below or equal to zero
            if r <= 0:
                r = 0.1
            # delay before next key press
            time.sleep(r)

    def execute_chain_fake(self):
        """
        Fake key typing with errors to simulate a real user and not be suspicious with too good results.
        Usually user will have a few tries before having a good result. So this method helps to keep everything
        under the radar.
        """

        # read complete document with all key chains
        chain = self.json_read('document')

        # prints keys to press for comparison
        print 'Keys to Press: ' + chain[self.lesson][self.exercise]

        # shows all pressed keys
        print 'Keys Pressed: ',
        count = 0
        # retrieve current lessons and exercise keychain
        for key in chain[self.lesson][self.exercise]:
            print key,
            count += 1
            if count > random.randint(10,30):
                print '\nRestarting'
                print '-----------------------------------------------\n'
                #self.restart()
                break
            # press on current key
            r = random.randint(0,5)
            # press intentionally on wrong key
            if r == 0:
                pyautogui.press(chr(ord(key) + 1))
                # simulate user who try to understand what went wrong
                time.sleep(.5)
            # press correct key
            pyautogui.press(key)

            # calculate sleep time based on speed and a randomise factor
            r = random.uniform(self.type_speed - self.type_speed_randomize, self.type_speed + self.type_speed_randomize)

            # never drop below or equal to zero
            if r <= 0:
                r = 0.1
            # delay before next key press
            time.sleep(r)

    def start_auto_type(self):
        """ counts down before starting auto typing. """
        # Be prepared call to user
        print '\n\nGet Ready!'
        print '-----------------------------------------------\n'

        # counts down 3 seconds
        for x in range(3, 0, -1):
            # prints current left seconds
            print 'Auto type starts in : ' + str(x)
            time.sleep(1)

        # prints a new line
        print '\n'

        # starts typing
        self.execute_chain()
"""
    def navigate_page(self):
        # Create a new instance of the Firefox driver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # go to the google home page
        #self.driver.get('http://www.ratatype.com/')

        self.driver.find_element_by_class_name('submit').click()

        self.start_auto_type()

    def restart(self):
        self.driver.find_element_by_class_name('navAnew').click()
"""

def init(*args,**kwargs):
    pro_typer = ProTyper(args[0], args[1], args[2], args[3])
    pro_typer.start_auto_type()

#if __name__ == '__main__':
    #pro_typer = ProTyper('lesson_1', 0, 0.01, 0.0)
    #pro_typer.start_auto_type()

exec(''.join(sys.argv[1:]))