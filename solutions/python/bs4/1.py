# pip3 install bs4
from bs4 import BeautifulSoup as bs

html_doc = """
<html>
<head>
<title>Demo</title>
</head>
<body>
<h1>Demo BeautifulSoup</h1>
<p>LoL</p>
<p>Leaguage of Legends</p>
<h2>Buồn ơi là buồn</h2>
</body>
</html>
"""

html = bs(html_doc, "html.parser")

title = html.find("title")
h1_tags = html.find_all("h1")
p_tags = html.find_all("p")
print(p_tags[0].text)
print(len(p_tags[0].text))
