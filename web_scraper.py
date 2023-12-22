import requests
from bs4 import BeautifulSoup

url = "https://www.codewithtomi.com/"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

titles = soup.find_all("h2", {"class": "post-title"})


for t in titles:
    print(t.getText())

    

