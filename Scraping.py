import pandas as pd 
import requests
from bs4 import BeautifulSoup

Product_name=[]
Prices=[] #for prices 'cN1yYO'
Reviews=[] # for Reviews " _5OesEi"
Descriptions=[] # for Descriptions " G4BRas"

for i in range(2,12):

    url="https://www.flipkart.com/search?q=mobiles+under+50000+rupees&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_2_19_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_2_19_na_na_na&as-pos=2&as-type=RECENT&suggestionId=mobiles+under+50000+rupees&requestId=97dc4c77-2bba-4575-ba7e-525d8e1d7ea9&as-searchtext=mobiles%20under%2050000%20rupees"+str(i)
    r=requests.get(url)
    #print(r)

    soup=BeautifulSoup(r.text,"lxml")
    box=soup.find("div",class_ = "DOjaWF gdgoEp")






    # np=soup.find("a",class_ = '_9QVEpD').get("href")
    # cnp="https://www.flipkart.com/"+np
    # print(cnp)


    # url=cnp
    # r=requests.get(url)
    # soup= BeautifulSoup(r.text,"lxml")

    names=box.find_all("div",class_ = 'KzDlHZ')

    for i in names:
        name=i.text
        Product_name.append(name)

    #print(Product_name)

    prices=box.find_all("div",class_ = '_4b5DiR')

    for i in prices:
        name=i.text
        Prices.append(name)

    #print(Prices)

    review=box.find_all("div",class_ = "XQDdHH" )

    for i in review:
        name=i.text
        Reviews.append(name)

    #print(len(Reviews))

    desc=box.find_all("ul",class_= "G4BRas")

    for i in desc:
        name=i.text
        Descriptions.append(name)
    #print(Descriptions)


df=pd.DataFrame({"Product Name":Product_name,"Prices":Prices,"Reviews":Reviews,"Descriptions":Descriptions})
print(df)

df.to_csv("flipcart_product_data.csv")



