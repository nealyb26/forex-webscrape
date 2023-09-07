#!/usr/bin/env python3

import pygsheets
import time
from main import exchange_dict
#Some code adapted from Medium and Stack Overflow thread written in Java

#gc = pygsheets.authorize(client_secret='client_secret.json')
gc = pygsheets.authorize(service_file='forexsheetsproject.json')

# 3. Open spreadsheet by link
# Test Sheet: 1DNUDEi-WDyRgNGzhHxX-1m8lFgq8W-rZBBW2oswx4QA
sh = gc.open_by_key('1F6tvz2kQc_4aOZZw7Bcu3Wd3o_evS9UEh06cCX_vIvw')


#==========================================================================
def find_first_empty_row(column_values):
    # Find the index of the first empty cell (value is None)
    empty_index = None
    minimum_index = 210 # look for indicies beyond this value

    for idx, value in enumerate(column_values):
        if idx >= minimum_index and not value:
            empty_index = idx + 1  # account for zero indexing
            break
    
    return empty_index

#for the following banks, IG value is in column F
F_SCRUBS = ["Bofa", "OCBC", "TSB", "ANZ", "HSBC", "ICBC", "BNP", "Citi"]

for key in exchange_dict:

    if key != "IG":
        worksheet = sh.worksheet_by_title(key)
        print("Updating Worksheet: ", worksheet.title)

        # Specify the column index you want to check (e.g., column A is index 1)
        column_index = 3

        # Get all values in the specified column
        column_values = worksheet.get_col(column_index)

        empty_index = find_first_empty_row(column_values)
        print(f"Found Index: {empty_index}")

        #for i in range(0, empty_index):
        if key in F_SCRUBS:
            worksheet.update_value(f'D{empty_index}', exchange_dict[key][0])
            worksheet.update_value(f'C{empty_index}', exchange_dict[key][1])
            worksheet.update_value(f'F{empty_index}', exchange_dict["IG"][1]) #<- updates IG value on each page
        else:
            worksheet.update_value(f'C{empty_index}', exchange_dict[key][0])
            worksheet.update_value(f'B{empty_index}', exchange_dict[key][1])
            worksheet.update_value(f'E{empty_index}', exchange_dict["IG"][1]) #<- updates IG value on each page
    print("complete")

#===================================================================================================
# // Don's array approach - checks first column only
# // With added stopping condition & correct result.
# // From answer https://stackoverflow.com/a/9102463/1677912
# function getFirstEmptyRowByColumnArray() {
#   var spr = SpreadsheetApp.getActiveSpreadsheet();
#   var column = spr.getRange('A:A');
#   var values = column.getValues(); // get all data in one call
#   var ct = 0;
#   while ( values[ct] && values[ct][0] != "" ) {
#     ct++;
#   }
#   return (ct+1);
# }



# Test Case for seeing if values appear
# value = 1
# wk1 = sh[0] # Wells Fargo is name of first worksheet
#
# for i in range(1, 11):
#     wk1.update_value(f'A{i}', value)
#     time.sleep(1)
#     value += 1