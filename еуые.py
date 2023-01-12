import requests


url = requests.get('https://github.com/netology-code/python-final-diplom/blob/master/data/shop1.yaml')
print(url.content)
