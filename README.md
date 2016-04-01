# WebScraper
A Very Simple Web Scraper

This is a quick and dirty web scraper created in my spare time.

It is very specific and can only be used to scrape from the O2 website for landline rates.

To run:

1. Place all files and folders in the same dir and run WebScraper.py

Due to very limited time there are a few rules for use:

1. Initially it can only be used with Chrome

2. Secondly to use it you will have to make sure that the directory of your chromedriver is correct in the scraperprogram.py file

3. Thirdly at the moment it takes input in the form of strings made up of letters in a list form with entires separated by a comma and then a space e.g. South Africa, Croatia, Japan (This could very easliy be changed if you wanted a different input method)
 
TO COMPLETE TASK SET BY YOU: Enter: Canada, Germany, Iceland, Pakistan, Singapore, South Africa (use of caps doesn't matter)

4. It outputs a dictionary with country name and rate for landline calls

I really didn't manage to get much time to do this due to a very large workload in my current job with it being the end of the financial year. I would intend to improve upon it firstly by adding unittest on top of the docctest and secondly by changing to using a headless browser.

I did however find the task very enjoyable and certainly would have liked to spend more time on it.

P.S. I took a list of allowed countries from the page to check the input against, this is quicker for the user than finding out if the country chosen will work by testing on the webpage. To show my code is also robust enough to stand up against incorrect input I have added 'Paul' to this list which is obviously not an allowed country on the website for testing.
You can add any words to this countries.txt to enable their input and test for incorrect country name input which is handled in my main program.

