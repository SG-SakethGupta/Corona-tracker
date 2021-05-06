import requests
from bs4 import BeautifulSoup
from tkinter import *

win = Tk()
page = requests.get("https://covid19.who.int/")
cont = BeautifulSoup(page.text, "html.parser")
cases = cont.find_all(class_="sc-prOVx jYOhWU")
deaths = cont.find_all(class_="sc-prOVx cpmqbh")
vaccine = cont.find_all(class_="sc-prOVx fSlcrp")
Label(win, text = f"{cases[2].text}\n\n{deaths[0].text}\n\n{vaccine[1].text}").pack()
Label(win, text = "Information directed from WHO").pack()
mainloop()