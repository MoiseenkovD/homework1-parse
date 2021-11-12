from parse_cookie import parse_cookie
from parse_url_params import parse

print(parse_cookie('name=Dima;'))  # {'name': 'Dima'}
print(parse_cookie(''))  # {}
print(parse_cookie('name=Dima;age=28;'))  # {'name': 'Dima', 'age': '28'}
print(parse_cookie('name=Dima=User;age=28;'))  # {'name': 'Dima=User', 'age': '28'}

print(parse('https://example.com/path/to/page?name=ferret&color=purple')) # {'name': 'ferret', 'color': 'purple'}
print(parse('https://example.com/path/to/page?name=ferret&color=purple&')) # {'name': 'ferret', 'color': 'purple'}
print(parse('http://example.com/')) # {}
print(parse('http://example.com/?')) # {}
print(parse('http://example.com/?name=Dima')) # {'name': 'Dima'}