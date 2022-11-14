# import urllib.request
# import requests
#
# # opener = urllib.request.build_opener()
# # response = opener.open("https://httpbin.org/get")
# # print(response.read())
# response = requests.get("https://httpbin.org/get")
#
# print(f"Datatype - {type(response.content)}")
# print(response.text)
# print(f"Datatype - {type(response.text)}")

# import requests
# response = requests.post("https://httpbin.org/post",
#                          data = "Test data",
#                          headers={"h1": "Test Title"})
# print(response.text)

# import requests
#
# res_parse_list = []
# response = requests.get("https://coinmarketcap.com/")
# #print(response.text)
# response_text = response.text
# response_parse = response_text.split("<span>")
# for parse_elem_1 in response_parse:
#     if parse_elem_1.startswith("$"):
#         for parse_elem_2 in parse_elem_1.split("</span>"):
#             if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
#                 print(parse_elem_2)
#                 res_parse_list.append(parse_elem_2)
#
# bitcoin_exchange_rate = res_parse_list[0]
# print(bitcoin_exchange_rate)

from bs4 import BeautifulSoup
from colorama import Fore, Back, Style
import requests

response = requests.get("https://mixnews.lv/anekdoty/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features = "html.parser")
    soup_list = soup.find_all("div", {"class" : "desc-post"})
G = Fore.GREEN
R = Fore.RED
B = Fore.BLUE
a = 0
    #elem.split("<div>", "</div>", "<p>", "</p>")
for elem in soup_list:
    if a == 0:
        print(G +  "Внимание Анекдот!")
        print(R, elem, end='\n\t\n')
        a = 1
    if a == 1:
        print(R +  "Внимание Анекдот!")
        print(G, elem, end='\n\t\n')
        a = 2
    if a == 2:
        print(G +  "Внимание Анекдот!")
        print(B, elem, end='\n\t\n')
        a = 0
    #res = soup_list[0].find("p")
    #print(res.text)
