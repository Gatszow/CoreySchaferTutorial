import requests

# it's how you can get image from page
result = requests.get('https://imgs.xkcd.com/comics/python.png')
with open('comic.png', 'wb') as f:
    f.write(result.content)

result = requests.get('https://imgs.xkcd.com/comics/python.png')

# Check if you can start webscrapping
print(result.ok)

# Print headers
print(result.headers)

payload = {'username': 'corey', 'password': 'testing'}
result = requests.post('https://httpbin.org/post', data=payload)
result_dict = result.json()
print(result_dict['form'])
