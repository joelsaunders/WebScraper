from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


# Initialise dict to store rates in
rates_d = {}


# Function to create list of countries to search for.
def input_list_create(in_str):
    return in_str.split(", ")


def start_browser():
    chromedriver_path ='C:\\Users\knowhow\Desktop\Python Learning\chromedriver'
    browser = webdriver.Chrome(executable_path = chromedriver_path)
    return browser

# Open Webpage    
def open_page(url):
    browser.get(url)
    

# Main function that finds and prints data
def main_loop(in_list):
    for x in range(len(in_list)):
    
        # Find country entry box & clear it
        country = browser.find_element_by_id('countryName')
        country.clear()

        # Enter country name and dismiss autocomplete
        country.send_keys(in_list[x])
        country.send_keys(Keys.RETURN)

        # Avoid being flagged and make sure link clickable
    
        seconds = 5 + (random.random() * 5)
        time.sleep(seconds)

        # Click pay monthly tab
        paymonthly = browser.find_element_by_id('paymonthly')
        paymonthly.click()

        # Find rate and store in variable then add to dict
        rate = browser.find_element_by_xpath\
               ('//*[@id="standardRatesTable"]/tbody/tr[1]/td[2]')
        cost = rate.text
    
        rates_d[in_list[x]] = str(cost)
    
    
        # Set cost to Error for problems in next iteration.
        cost = "Error"
    return (rates_d)

# Call functions
if __name__ == "__main__":

    in_list = input_list_create(input("Enter string of countries separated \
by a comma then space: "))
    browser = start_browser()
    open_page('http://international.o2.co.uk/internationaltariffs/\
calling_abroad_from_uk')
    print (main_loop(in_list))
    

