# pip install selenium==3.141.0
# pip install pandas==1.4.2
from selenium import webdriver
import pandas as pd
import time
def main(url):
    driver=webdriver.Chrome("C:\chromedriver.exe")
    driver.get(url)
    time.sleep(2)
    alldata=[]
    for i in range(10):
        request_names=driver.find_elements_by_xpath("""//*[@class="datatable table table-striped table-bordered  dataTable no-footer"]//tbody//tr//td//div//a""")
        data=[]
        name=request_names[i].text
        request_names[i].click()
        time.sleep(2)
        panel1=driver.find_elements_by_xpath("""(//*[@class='panel'])[2]//tbody//tr""")
        closing_date=panel1[0].text.split(":",1)[1]
        est_value_note=panel1[2].text.split(":",1)[1]
        panel2=driver.find_elements_by_xpath("""(//*[@class='panel'])[3]//tbody//tr[3]""")
        description=panel2[0].text.split(":",1)
        # As no of rows in project description is not confirm it check if we are fetching the correct desciption or not.
        if description[0]!="Description":
                panel2=driver.find_elements_by_xpath("""(//*[@class='panel'])[3]//tbody//tr[2]""")
                description=panel2[0].text.split(":",1)
        data=[name,est_value_note,description[1],closing_date]
        alldata.append(data)
        driver.refresh()
        time.sleep(2)
    #making dataframe so to convert data into understandable form.
    df=pd.DataFrame(alldata,columns=['Name','Est. Value Notes','Description','Closing Date'])
    df.to_csv("alldata.csv",index=False)
    # convert the dataframe to excel format
    df.to_excel("alldata_excel.xlsx")
    print(df)
url = "https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787"
main(url)