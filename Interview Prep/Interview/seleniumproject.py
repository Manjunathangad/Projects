from common_imports import *
driver = webdriver.Chrome()
driver.get("https://www.opencart.com/")
driver.maximize_window()
time.sleep(2)
print(driver.title)
driver.quit()


wb=openpyxl.load_workbook("f:\Trading Journal.xlsx")
sheet=wb.active 
print(sheet.max_row)
print(sheet.max_column)
for r in range(1,sheet.max_row+1):
    for c in range(1,sheet.max_column+1):
        print(sheet.cell(row=r,column=c).value,end=" ")
    print()






