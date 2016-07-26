from lxml import html
import requests

page = requests.get("https://uk.finance.yahoo.com/news/hot-abs-market-rolls-big-193246983.html")
#//*[@id="yui_3_9_1_1_1469386206755_1100"]/p[4]/text()[3]
tree = html.fromstring(page.content)
#'//div[class="bd"]/p[' + str(i) + ']/text()[' + str(i) + ']'
#//*[@id="yui_3_9_1_1_1469386206755_1099"]

for i in range(1, 100):
    path = '//div[@class="bd"]/p[1]/text()[2]'
    print(tree.xpath(path))
    print("")
