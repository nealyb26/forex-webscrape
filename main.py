from functions2 import *
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

exchange_dict = {}


kiwi_URL = "https://www.kiwibank.co.nz/personal-banking/accounts/international/foreign-exchange-rates-and-fees/"

TSB_URL = "https://www.tsb.co.nz/rates-fees-agreements/foreign-exchange/rates"

ANZ_URL = "https://tools.anz.co.nz/foreign-exchange/fx-rates/"

BNZ_URL = "https://www.bnz.co.nz/personal-banking/international/exchange-rates"

HSBC_URL = "https://www.hsbc.com.vn/en-vn/foreign-exchange/rate/"

ICBC_URL = "https://nz.icbc.com.cn/en/column/1438058489829540039.html"

WF_URL = "https://www.wellsfargo.com/foreign-exchange/currency-rates/"

OCBC_URL = "https://www.ocbc.com/business-banking/foreign-exchange-rates"

BOFA_URL = "https://www.bankofamerica.com/foreign-exchange/currency-converter/"

BOFA_URL_2 = "https://www.bankofamerica.com/foreign-exchange/exchange-rates/"

ROYAL_URL = "https://apps.royalbank.com/apps/foreign-exchange-calculator"

CITI_URL = "https://www1.citibank.com.sg/wealth-management/investments/investment-products/foreign-exchange/fx-calculator"

IG_URL = "https://www.tradingview.com/symbols/NZDUSD/"

kiwiSell, kiwiBuy = find_exch_rate_0(kiwi_URL, "/html/body/div[2]/div[3]/div[3]/div/div/div/div/div[2]/table/tbody/tr[4]/td[2]/p/span/span/span", "")
exchange_dict['Kiwi'] = (kiwiSell, kiwiBuy)

TSBSell, TSBBuy = find_exch_rate_0(TSB_URL, "/html/body/div[1]/div[2]/main/div/div/div/div/article/div/div[1]/div[2]/table/tbody/tr[4]/td[8]", "/html/body/div[1]/div[2]/main/div/div/div/div/article/div/div[2]/div[2]/table/tbody/tr[4]/td[8]")
exchange_dict['TSB'] = (TSBSell, TSBBuy)

ANZSell, ANZBuy = find_exch_rate_0(ANZ_URL, "/html/body/main/div[3]/div/div/div/form/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[4]/div", "/html/body/main/div[3]/div/div/div/form/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/div")
exchange_dict['ANZ'] = (ANZSell, ANZBuy)

BNZSell, BNZBuy = find_exch_rate_0(BNZ_URL, "/html/body/div[3]/div[1]/div/main/div[3]/div/div/div/div/div/div/table[1]/tbody/tr[2]/td[3]", "/html/body/div[3]/div[1]/div/main/div[3]/div/div/div/div/div/div/table[1]/tbody/tr[2]/td[2]")
exchange_dict["BNZ"] = (BNZSell, BNZBuy)

HSBCSell, HSBCBuy = find_exch_rate_0(HSBC_URL, '/html/body/main/div[2]/div/div[5]/div/div/div/div/div/table/tbody/tr[2]/td[2]', '/html/body/main/div[2]/div/div[5]/div/div/div/div/div/table/tbody/tr[2]/td[3]')
exchange_dict["HSBC"] = (HSBCSell, HSBCBuy)

ICBCSell, ICBCBuy = find_exch_rate_0(ICBC_URL, '/html/body/div/table[2]/tbody/tr/td[3]/table[2]/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr/td/table/tbody/tr[5]/td[2]/label','/html/body/div/table[2]/tbody/tr/td[3]/table[2]/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr/td/table/tbody/tr[5]/td[3]/label')
exchange_dict["ICBC"] = (ICBCSell, ICBCBuy)

WFSell, WFBuy = find_exch_rate_1(WF_URL, '/html/body/div[1]/div[2]/div/div[1]/div/div/div[1]/select', '/html/body/div[1]/div[2]/div/div[1]/div/div/div[1]/select/optgroup[1]/option[10]', '', '/html/body/div[1]/div[2]/div/div[1]/div/div/p[2]')
exchange_dict["WF"] = (WFSell, WFBuy[17:24])

OCBCSell, OCBCBuy = find_exch_rate_3_5(OCBC_URL, '/html/body/div[2]/section/div/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/span', '/html/body/span/span/span[2]/ul/li[6]', "/html/body/div[2]/section/div/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[4]/div", "/html/body/div[2]/section/div/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div", "/html/body/div[2]/section/div/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[4]/div")
exchange_dict["OCBC"] = (OCBCSell[8:14], OCBCBuy[8:14])

BOFASell = find_exch_rate_2(BOFA_URL_2, 'addCurrencyLink', 'dropDown', 'addCurrencyButton', '/html/body/div[1]/div[1]/div/section[3]/div/div[1]/div/div[2]/div/div[3]/div/div/div/div[2]/div[2]/label')

BOFABuy = find_exch_rate_2(BOFA_URL, 'addCurrencyLink', 'dropDown', 'addCurrencyButton', "/html/body/div[1]/div[1]/div/section[3]/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div/div[2]/div[3]/label")
exchange_dict["Bofa"] = (BOFASell, BOFABuy[5:11])

ROYALSell, ROYALBuy = find_exch_rate_3(ROYAL_URL)
exchange_dict["RBC"] = (ROYALSell, ROYALBuy)

CITISell, CITIBuy = find_exch_rate_4(CITI_URL)
exchange_dict["Citi"] = (CITISell, CITIBuy)

#Live Exchange Rate (IG Group)======================================================================

#the price we get from this is the buy price from IG
IGSell, IGBuy = find_exch_rate_0(IG_URL, "", "/html/body/div[3]/div[4]/div[2]/div[1]/div[1]/div/div/div/div[3]/div[1]/div/div[1]/span[1]")
exchange_dict["IG"] = (IGSell, IGBuy)


print(exchange_dict)