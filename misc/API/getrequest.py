"""
You don’t need to use a browser to fetch the contents of a page, though.
In Python, there’s a module available, called requests.
You can use the get function in the requests module to fetch the contents of a page.
"""

#http://www.datamuse.com/api/ is the doc for the api 


import requests
import json

# page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
kval_pairs = {'rel_rhy': 'funny'}
#the full url is built inside the call to requests.get
page = requests.get("https://api.datamuse.com/words", params=kval_pairs)
print(page.text[:150]) # print the first 150 characters
print(page.url) # print the url that was fetched


page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
print(type(page))
print(page.text[:150]) # print the first 150 characters
print(page.url) # print the url that was fetched
print("------")
x = page.json() # turn page.text into a python objectjust like json.loads(page.text)
print(type(x))
print("---first item in the list---")
print(x[0])
print("---the whole list, pretty printed---")
print(json.dumps(x, indent=2)) # pretty print the results
