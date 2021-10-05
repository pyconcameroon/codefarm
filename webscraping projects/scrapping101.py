from  bs4 import BeautifulSoup as bs


helloworld = "<p>Hello people </p>"
soup_l = bs(helloworld)
print(soup_l)