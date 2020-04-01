from bs4 import BeautifulSoup
import lxml
import requests
import urllib.request
import sys

query_word = str(input("検索ワードを入力してください。"))
print("「"+query_word+"」の画像をダウンロード開始します。")

headers = {"User-Agent": "hoge"}
URL="https://search.yahoo.co.jp/image/search?p={}&ei=UTF-8&ts=1050&aq=-1&ai=XhqawQaKTOmC_GkPQScMSA&fr=top_ga1_sa".format(query_word)
resp=requests.get(URL,timeout=1,headers=headers)

soup = BeautifulSoup(resp.text, "lxml")

imgs = soup.findAll(alt="「"+query_word+"」の画像検索結果")

for i in range(len(imgs)):
  filepath="倉庫/py/scraping/data/{}.jpg".format(i)
  urllib.request.urlretrieve(imgs[i]["src"],filepath)

print("ダウンロード完了しました。")
