import requests
from bs4 import BeautifulSoup

rs = requests.get("https://news.yahoo.co.jp")

#print(rs.headers)
#print(rs.encoding)
#print(rs.content)

soup = BeautifulSoup(rs.content, "html.parser")
#linkタグを出力している
for result in soup.find_all("link"):
    print(str(result))
