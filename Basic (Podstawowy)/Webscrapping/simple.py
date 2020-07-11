from bs4 import BeautifulSoup


with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')


# soup.element returns first element with that name
# for example soup.title will return first title element
#match = soup.title.text
#print(match)

# soup.find('element') returns first element with that name too
# but we can specify class_, so we can get other output
# for example soup.find('div', class_='footer') will return last element
# in this html file
#match = soup.find('div', class_='footer')
#print(match)

for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    print()
