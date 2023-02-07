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

def find_for_html(text, html):
    start_index = html.find(text) + len(text)
    end_offset = html[start_index:].find('<')
    return html[start_index:start_index + end_offset]

print(find_for_html("Name: ", html))