import requests
import pandas as pd
from bs4 import BeautifulSoup

# testing
from pprint import pprint

file_list = [
    "attorneyexcellist",
    "caexcellist",
    #"repexcellist",
    "orgsexcellist"
]

def convert_to_csv():
    data = []
    for file_name in file_list:
        # for getting the header from
        # the HTML file
        list_header = []
        soup = BeautifulSoup(open("data/" + file_name),'html.parser')
        header = soup.find_all("table")[0].find("tr")
        
        for items in header:
            try:
                list_header.append(items.get_text())
            except:
                continue
        
        # for getting the data
        HTML_data = soup.find_all("table")[0].find_all("tr")[1:]

        for element in HTML_data:
            sub_data = []
            for sub_element in element:
                try:
                    sub_data.append(sub_element.get_text())
                except:
                    continue
            data.append(sub_data)
        
        # Storing the data into Pandas
        # DataFrame
        list_header = [i for i in list_header if i != '\n']

        data = [[ele for ele in sub if ele != '\n'] for sub in data]

        # if file_name == 'repexcellist':
        #     print(list_header)
        #     for row in data:
        #         #print(len(row))
        #         if len(row) != len(list_header):
        #             print(row)
        #             exit()

        try:
            dataFrame = pd.DataFrame(data = data, columns = list_header)
        except ValueError as e:
            print(e)
            print(file_name + " failed to parse properly")

        # Converting Pandas DataFrame
        # into CSV file
        dataFrame.to_csv("data/%s.csv" % file_name)
    return True

def pull_data():
    base_url = "https://www.va.gov/ogc/apps/accreditation/"
    end_url = ".asp"

    for file_name in file_list:
        url = base_url + file_name + end_url
        r = requests.get(url, verify=False)
        f = open("data/" + file_name, 'wb')
        for chunk in r.iter_content(chunk_size=512 * 1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
        f.close()
    return True

pull_data()
convert_to_csv()