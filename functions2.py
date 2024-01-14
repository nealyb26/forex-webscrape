#Neal Bagai
#Selenium Automated NZD Exchange Rate Values
#Summer 2023

from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time


#This form of the function can be used to scrap values from KiwiBank, TSB, ANZ, BNZ, HSBC, and ICBC
def find_exch_rate_0(url, xpath1, xpath2):
    driver = webdriver.Chrome()
    driver.get(url)

    buyValue = ""
    sellValue = ""
    max_attempts = 5

    if url in ("https://nz.icbc.com.cn/en/column/1438058489829540039.html", "https://www.hsbc.com.vn/en-vn/foreign-exchange/rate/"):
        time.sleep(4)
    
    if xpath1 != "":
        # # <OPTIONAL>
        # wait = WebDriverWait(driver, 10) # wait max of 10 seconds for dropdown
        # sellRate = wait.until(EC.presence_of_element_located((By.XPATH, xpath1)))
        # time.sleep(3)

        for attempt in range(max_attempts):
            try:
                # Using Absolute X-Path to find exchange rate.
                sellRate = driver.find_element(By.XPATH, xpath1)
            except NoSuchElementException:
                print(f"Attempt {attempt+1} failed. Retrying...")
                time.sleep(5)

        # # Using Absolute X-Path to find exchange rate.
        # sellRate = driver.find_element(By.XPATH, xpath1)
        sellValue = sellRate.text

    if xpath2 != "":
        # <OPTIONAL>
        # wait = WebDriverWait(driver, 10) # wait max of 10 seconds for dropdown
        # buyRate = wait.until(EC.presence_of_element_located((By.XPATH, xpath2)))
        # time.sleep(3)

        for attempt in range(max_attempts):
            try:
                # Using Absolute X-Path to find exchange rate.
                buyRate = driver.find_element(By.XPATH, xpath2)
            except NoSuchElementException:
                print(f"Attempt {attempt+1} failed. Retrying...")
                time.sleep(5)

        # Using Absolute X-Path to find exchange rate.
        # buyRate = driver.find_element(By.XPATH, xpath2)
        buyValue = buyRate.text

    print("Sell Rate: ", sellValue, "Buy Rate: ", buyValue)

    return sellValue, buyValue

# This form of the function can be used with Wells Fargo, OCBC, and possibly BOFA
# xpath4 is for buy rate
def find_exch_rate_1(url, xpath1, xpath2, xpath3, xpath4):
    sellValue = ""
    buyValue = ""

    driver = webdriver.Chrome()
    driver.get(url)

    # <OPTIONAL>
    wait = WebDriverWait(driver, 10) # wait max of 10 seconds for dropdown
    wait.until(EC.presence_of_element_located((By.XPATH, xpath1)))

    # Click the button that brings up the dropdown menu
    dropdown_button = driver.find_element(By.XPATH, xpath1)
    dropdown_button.click()

    # <OPTIONAL>
    time.sleep(3)
    wait = WebDriverWait(driver, 10) # wait max of 10 seconds for dropdown
    wait.until(EC.presence_of_element_located((By.XPATH, xpath2)))

    #Click the the dropdown element
    dropdown_option = driver.find_element(By.XPATH, xpath2)
    dropdown_option.click()

    if xpath3 != '':

        # <OPTIONAL>
        time.sleep(3)
        wait = WebDriverWait(driver, 10) # wait max of 10 seconds for dropdown
        wait.until(EC.presence_of_element_located((By.XPATH, xpath3)))

        #find the page element following the dropdown selection
        sellRate = driver.find_element(By.XPATH, xpath3)
        sellValue = sellRate.text

    if xpath4 != '':
        # <OPTIONAL>
        time.sleep(3)
        wait = WebDriverWait(driver, 10) # wait max of 10 seconds for dropdown
        wait.until(EC.presence_of_element_located((By.XPATH, xpath4)))

        #find the page element following the dropdown selection
        buyRate = driver.find_element(By.XPATH, xpath4)
        buyValue = buyRate.text

    print("Buy Rate:", end = " ")
    print(buyValue)
    print("Sell Rate: ", end = " ")
    print(sellValue)

    return sellValue, buyValue

# I got lazy so this next function is exclusively for BOFA
# includes a dropdown + click, and then value scrape
def find_exch_rate_2(url, id1, id2, id3, xpath1):
    
    driver = webdriver.Chrome()
    driver.get(url)

    wait = WebDriverWait(driver, 10)
    dropdown_element = wait.until(EC.presence_of_element_located((By.ID, id1)))

    button = driver.find_element(By.ID, id1)
    button.click()

    wait = WebDriverWait(driver, 10)
    dropdown_element = wait.until(EC.presence_of_element_located((By.ID, id2)))

    dropdown = Select(dropdown_element)
    desired_option_value = 'New Zealand'
    # dropdown.select_by_value(desired_option_value)
    dropdown.select_by_visible_text(desired_option_value)

    wait = WebDriverWait(driver, 10)
    dropdown_element = wait.until(EC.presence_of_element_located((By.ID, id3)))

    button2 = driver.find_element(By.ID, id3)
    button2.click()

    time.sleep(3)

    BOFAExchRate = driver.find_element(By.XPATH, xpath1)

    print("BOFA Rate:", end = " ")
    print(BOFAExchRate.text)
    exchValue = BOFAExchRate.text

    return exchValue


#extremely similar to the functions above, but allows for switch button to get exchange rates. Compatable with Royal Bank Website
def find_exch_rate_3(url):
    
    driver = webdriver.Chrome()
    driver.get(url)

    wait = WebDriverWait(driver, 10)
    RBC_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/section[1]/div/div/div[1]/div[2]/div[1]/div[1]/div")))

    # Click the button that brings up the dropdown menu
    RBC_dropdown = driver.find_element(By.XPATH, "/html/body/div[1]/main/section[1]/div/div/div[1]/div[2]/div[1]/div[1]/div")
    RBC_dropdown.click()

    time.sleep(3)

    # Select NZD dropdown element
    RBC_dropdown_option = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[1]/div/div/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[16]')
    RBC_dropdown_option.click()

    time.sleep(5)

    RBCSellRate = driver.find_element(By.XPATH, "/html/body/div[1]/main/section[1]/div/div/div[1]/div[2]/div[1]/p/span")
    RBCSellValue = RBCSellRate.text

    # switch currencies for exchange rate
    RBCButton = driver.find_element(By.XPATH, "/html/body/div[1]/main/section[1]/div/div/div[1]/div[2]/div[2]/div/button")
    RBCButton.click()

    time.sleep(5)

    RBCExchRate = driver.find_element(By.XPATH, "/html/body/div[1]/main/section[1]/div/div/div[1]/div[2]/div[3]/p")

    time.sleep(5)

    RBCBuyValue = RBCExchRate.text[6:15]
    print("Royal Bank Sell Rate:", RBCSellValue, "Royal Bank Buy Rate: ", RBCBuyValue)

    return RBCSellValue, RBCBuyValue

#extremely similar to the functions above, but allows for switch button to get exchange rates. Compatable with Royal Bank Website and adapted for OCBC
def find_exch_rate_3_5(url, xpath1, xpath2, xpath3, xpath4, xpath5):
    
    driver = webdriver.Chrome()
    driver.get(url)

    wait = WebDriverWait(driver, 10)
    OCBC_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, xpath1)))

    # Click the button that brings up the dropdown menu
    OCBC_dropdown = driver.find_element(By.XPATH, xpath1)
    OCBC_dropdown.click()

    time.sleep(3)

    # Select NZD dropdown element
    OCBC_dropdown_option = driver.find_element(By.XPATH, xpath2)
    OCBC_dropdown_option.click()

    time.sleep(5)

    OCBCSellRate = driver.find_element(By.XPATH, xpath3)
    OCBCSellValue = OCBCSellRate.text

    # switch currencies for exchange rate
    OCBCButton = driver.find_element(By.XPATH, xpath4)
    OCBCButton.click()

    time.sleep(5)

    OCBCBuyRate = driver.find_element(By.XPATH, xpath5)

    time.sleep(5)

    OCBCBuyValue = OCBCBuyRate.text
    print("Sell Rate:", OCBCSellValue, "Buy Rate: ", OCBCBuyValue)

    return OCBCSellValue, OCBCBuyValue

# this function does dropdown selection, switches rates, and finds buy and sell. Compatable with CITI Website. 
def find_exch_rate_4(url):
    driver = webdriver.Chrome()
    driver.get(url)

    # for CITI Bank, we must first select NZD as our exchange currency, read a value, and then switch the values to get the buy rate. 

    CITIDropdownMenu = driver.find_element(By.XPATH, '/html/body/app-root/div/div/app-marketing-page-render/div/app-marketing-dynamic-page/msa-currency-convertor/div/div[1]/div[1]/div/div[2]/ui-input-select/div/button')

    CITIDropdownMenu.click()

    CITIDropdownSelect = driver.find_element(By.XPATH, '//*[@id="cdk-overlay-0"]/div/div/div/button[11]')

    time.sleep(5)

    CITIDropdownSelect.click()

    time.sleep(5)

    CITISellRate = driver.find_element(By.XPATH, '/html/body/app-root/div/div/app-marketing-page-render/div/app-marketing-dynamic-page/msa-currency-convertor/div/div[1]/div[2]/div/div[2]/span/span')

    print("CITI Sell Rate is: ", CITISellRate.text)
    sellValue = CITISellRate.text

    CITISwitchButton = driver.find_element(By.XPATH, '/html/body/app-root/div/div/app-marketing-page-render/div/app-marketing-dynamic-page/msa-currency-convertor/div/div[1]/div[1]/div/div[3]')

    time.sleep(3)

    CITISwitchButton.click()

    time.sleep(3)

    CITIBuyRate = driver.find_element(By.XPATH, '/html/body/app-root/div/div/app-marketing-page-render/div/app-marketing-dynamic-page/msa-currency-convertor/div/div[1]/div[2]/div/div[2]/span[1]/span')

    print("CITI Buy Rate is: ", CITIBuyRate.text)
    buyValue = CITIBuyRate.text

    return sellValue, buyValue
