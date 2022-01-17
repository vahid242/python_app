from turtle import st
import requests
from bs4 import BeautifulSoup
import pandas

l=[]

# load page
r= requests.get("https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")

# access to content of this requests object
c=r.content
# make content more readable
soup=BeautifulSoup(c,"html.parser")
all=soup.find_all("div", {"class":"propertyRow"})
page_nr=soup.find_all("a" ,{"class":"Page"})[-1].text

base_url="https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
for page in range(0,int(page_nr)*10,10):
    print(base_url+str(page)+".html")
    r=requests.get(base_url+str(page)+".html")
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("div", {"class":"propertyRow"})
    print(all)
    for item in all:
        d={}
        d["Peice"]=item.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ", "")
        d["Address"]=item.find_all("span",{"class":"propAddressCollapse"})[0].text
        d["Locality"]=item.find_all("span",{"class":"propAddressCollapse"})[1].text
        # if the number of bedroom available print else print none
        try:
            d["Bed"]=item.find("span",{"class":"infoBed"}).find("b").text
        except:
            d["Bed"]=None

        try:
            d["Area"]=item.find("span",{"class":"infoSqFt"}).find("b").text
        except:
            d["Area"]=None

        try:
            d["Full Baths"]=item.find("span",{"class":"infoValueFullBath"}).find("b").text
        except:
            d["Full Baths"]=None
        try:
            d["Area"]=item.find("span",{"class":"infoValueHalfBath"}).find("b").text
        except:
            d["Area"]=None

        for column_group in item.find_all("div", {"class":"columnGroup"}):
            for feature_group, feature_name in zip(column_group.find_all("span", {"class":"featureGroup"}),column_group.find_all("span", {"class":"featureName"})):
                if "Lot Size" in feature_group.text:
                    d["Lot Size"]=feature_name.text

        l.append(d)

df=pandas.DataFrame(l)
df.to_csv("output.csv")


