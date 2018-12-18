from selenium import webdriver
import pandas as pd
import sys
import re
data = []  # create an empty list to store data
#naukari_data=[]
freshers_data = []
driver = webdriver.Chrome(executable_path='P:/StudyWork/Python Programs/PythonProg/Web_scrapping/Naukari_WebScrapping/chromedriver')#must be the chromedriver in this specified folder

city = input("please enter city :")


def total_pages(): # calculate total pages
    try:
        driver.get("https://www.naukri.com/python-jobs-in-"+city)
        total_page = driver.find_elements_by_xpath('//span[@class="cnt"]')
        page_no = total_page[0].text.split(' ')[-1]
        pages = int(int(page_no)/50)
        return pages
    except Exception:
        driver.close()
        sys.exit("**********"+city+"is not available on Naukari.com")


def fetch_data():
    a = total_pages()
    for i in range(1, a+2):
        if (i == 1):
            driver.get("https://www.naukri.com/python-jobs-in-"+ city)
            print("@@@@@@@fetching data from page", i)
        else:
            driver.get("https://www.naukri.com/python-jobs-in-" + city + "-"+str(i))
            print("@@@@@@@fetching data from page", i)

            
        job_title = driver.find_elements_by_xpath('//li[@class = "desig"]')
        company = driver.find_elements_by_xpath('//span[@class = "org"]')
        exp = driver.find_elements_by_xpath('//span[@class = "exp"]')
        #sal = driver.find_elements_by_xpath('//span[@class = "salary"]')

        for i in range(int(len(job_title))):
            df = {}
            df["Job-Title"] = job_title[i].text
            df["Company"] = company[i].text
            df["Exprience"] = exp[i].text
            #df["Package"] = sal[i].text
            data.append(df)
    return data

def data_to_csv():
    fetch_data()
    df1 = pd.DataFrame(data)
    df1.to_csv("Python_jobs_"+city+".csv", index=False)

data_to_csv()

def for_freshers():
    for f in data:
        if (re.findall(r'[\d]+', f["Exprience"]))[0] == '0':
            freshers_data.append(f)
    return freshers_data

def freshers_data_csv():
    for_freshers()
    df1 = pd.DataFrame(freshers_data)
    df1.to_csv("Jobs_for_freshers_"+city+".csv", index=False )
freshers_data_csv()




driver.close()
csv_file = pd.read_csv("Python_jobs_"+city+".csv")
csv_file1 = pd.read_csv("Jobs_for_freshers_"+city+".csv")
csv_file
csv_file1
