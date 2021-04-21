from bs4 import BeautifulSoup
import requests


url= "https://www.dolarhoy.com/cotizaciondolarblue"
page = requests.get(url)
soup=BeautifulSoup(page.content,"html.parser")

dolar = soup.find_all("div", class_="value")

cotizacion=[]

for i in dolar:
    cotizacion.append(i.text)

moneda=cotizacion[1]

dolarblue=(float("".join(d for d in moneda if d.isdigit())))/100


