Beautiful soup can be used to extract any data from an
Html / xml document.

creating a beautifulsoup object base on an input string.
------------------------------------------
helloworld = "<p>Hello people</p>"
soup_string = beautifulsoup(helloworld)
|
|
Creating a beautifulsoup from a file
===============================
in order to get thelist if the books from a website, in order to reduce the overhead of 
visiting this url from our browser to get this content, it is approprait ti create bs4
object by providing file like object of the url

import urllib2
from bs4 import BeautifulSoup

url = "http://www.packtpub.com/books"
page = urllib2.urlopen(url)
soup_package = BeautifulSoup(page)

