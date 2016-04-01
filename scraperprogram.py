# Selenium program v3
# Exception Handling Added

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from utils import check_country
from utils import create_input_list
from selenium.common.exceptions import NoSuchElementException
import sys


def start_browser(url):
    """
    Starts browser and opens url in argument.
    """
    try:
        chromedriver_path =('C:\\Users\knowhow\Desktop'
                            '\Python Learning\chromedriver')
    except FileNotFoundError:
        print("Error: chromedriver not found please check location")
    browser = webdriver.Chrome(executable_path = chromedriver_path)
    browser.get(url)
    return browser
    
# Main function that finds and prints data
def main_loop(in_list):
    """
    Navigates through webpage to find the rate and returns a
    dictionary of the result.

    >>> main_loop(['japan', 'pakistan', 'singapore'])
    {'pakistan': '£1.20', 'japan': '£1.00', 'singapore': '£1.00'}

    >>> main_loop(['paul', 'pakistan', 'singapore'])
    {'pakistan': '£1.20', 'paul': 'Country not found', 'singapore': '£1.00'}
    """
    # Call start browser function
    browser = start_browser('http://international.o2.co.uk/interna'
                            'tionaltariffs/calling_abroad_from_uk')
    # Initialise dict to store rates in
    rates_d = {}
    
    for x in range(len(in_list)):
        # Set error counters to zero for each loop
        element_not_found_error = 0
        rate_not_found_error = 0
        country_not_found = 0
        
        # Find country entry box
        try: 
            country = browser.find_element_by_id('countryName')
        except NoSuchElementException:
            print("Correct page not loaded, check url")
            sys.exit(1)
            
        # Clear then enter country name and dismiss autocomplete
        country.clear()
        country.send_keys(in_list[x])
        country.send_keys(Keys.RETURN)
        
        #Check to make sure country not found error doesn't appear
        not_found_error = browser.find_element_by_xpath\
                              ('//*[@id="countryName"]')
        if not_found_error.get_attribute('value') == ("Please enter "
                                                      "a valid country "
                                                      "name"):
            country_not_found += 1
            

        # Avoid being flagged as bot and make sure link clickable
        seconds = 3 + (random.random() * 5)
        time.sleep(seconds)

        try:# Find pay monthly tab
            paymonthly = browser.find_element_by_id('paymonthly')
        except:
            element_not_found_error += 1
            
        # Click on pay monthly tab
        if element_not_found_error < 1:
            try:
                paymonthly.click()
            except NoSuchElementException:
                element_not_found_error += 1

            # Find rate and store in variable then add to dict
            try:
                rate = browser.find_element_by_xpath('//*[@id="sta'
                                                     'ndardRatesTab'
                                                     'le"]/tbody/tr'
                                                     '[1]/td[2]')
            except NoSuchElementException:
                rate_not_found_error += 1
        
        # Handle the errors by returning an error name      
        if country_not_found > 0:
            cost = "Country not found"
        elif element_not_found_error > 0:
            cost = "Element not found"
        elif rate_not_found_error > 0:
            cost = "Rate not found"
        else:
            cost = rate.text
            
        rates_d[in_list[x]] = str(cost)
    return (rates_d)


if __name__ == "__main__":   
    in_list = create_input_list("Enter string of countries "
                                "separated by a comma then space: ")
    in_list = check_country(in_list)
    print (main_loop(in_list))
    
    

