from bs4 import BeautifulSoup
import requests


url= "https://www.dolarhoy.com/"
page = requests.get(url)
soup=BeautifulSoup(page.content,"html.parser")

dolar = soup.find_all("div", class_="val")

cotizacion=[]

for i in dolar:
    cotizacion.append(i.text)

moneda=cotizacion[8]

dolarSoli=(float("".join(d for d in moneda if d.isdigit())))/100

