import socket
import socks
import requests
from lxml import etree

url = "http://www.imgur.com"
print("Requesting {}".format(url))

s = requests.session()

# login
login_url = "https://imgur.com/signin?redirect=http%3A%2F%2Fimgur.com%2F"
login_data = {'username': 'mmktest01', 'password': '123qwe!!'}
headers = {'User-agent': 'Mozilla/5.0', 'referer': ''}
html = s.post(login_url, login_data, headers = headers, timeout = 3)
print(html, type(html))
tree = etree.HTML(html.content)
print(tree.xpath("//div[@class='dropdown-footer']"))
print(tree.xpath("//div[@class='captcha']"), "Captcha")
# html_login = open("html_login.txt", "wb")
# html_login.write(html)

# upload URL http://imgur.com/upload
post_url = "https://imgur.com/upload"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36', 'referer': 'https://imgur.com/'}
files = {'file': open('thumbnail00.png', 'rb')}
print(26, files)
html = s.post(post_url, files=files, headers=headers)
print(html, html.text)

s.close()


# share URL http://imgur.com/ajax/share

# url = "http://my-ip.herokuapp.com/"
# s = requests.session()

# ip = "50.30.164.238"
# port = 45554
# socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, ip, port)
# socket.socket = socks.socksocket

# html = s.get(url)
# print(html.text)

# import socket
# import socks
# import requests
# ip='localhost' # change your proxy's ip
# port = 0000 # change your proxy's port
# socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, ip, port)
# socket.socket = socks.socksocket
# url = u'http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=inurl%E8%A2%8B'
# print(requests.get(url).text)