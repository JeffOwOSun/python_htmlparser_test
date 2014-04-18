import urllib
from lxml import html

url='http://dict.youdao.com/search?q='+'dictionary'
page = html.fromstring(urllib.urlopen(url).read())
collins = page.xpath('//*[@id="collinsResult"]/div/div/div/div')[0]
print "collins result: ", html.tostring(collins)
#print "type of collins", type(collins)
#print "type of page", type(page)
html.open_in_browser(collins)
