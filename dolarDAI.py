
from bs4 import BeautifulSoup
import requests


url= "https://www.buenbit.com/"
page = requests.get(url)
soup=BeautifulSoup(page.content,"html.parser")

div=soup.find("span", attrs={"id":'daiars-selling-price'})
spans=div.find_all("span")

#dolar = soup.find("span", {"id":'daiars-selling-price'})

print (spans)

#cotizacion=[]

#for i in dolar:
#    cotizacion.append(i.text)

#moneda=cotizacion[1]

#dolarsinredondeo=(float("".join(d for d in moneda if d.isdigit())))/100000

#dolarDAI=round(dolarsinredondeo,2)
