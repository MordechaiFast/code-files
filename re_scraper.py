# coding: utf-8
import re
from urllib.request import urlopen


url = 'http://olympus.realpython.org/profiles/dionysus'
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) #Remove HTML tags
print(title)

text = re.sub("<.*?>", "", html)
name_index = text.find("Name: ") + len("Name: ")
name_end = text[name_index:].find('\n')
name = text[name_index:name_index + name_end]
print(name)