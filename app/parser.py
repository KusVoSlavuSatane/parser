import requests
import datetime
from bs4 import BeautifulSoup



def parse_html(url: str):
    r = requests.get(url)
    print(r.status_code)
    return r.text

def sort_arrays(names, values):
    if len(names) != len(values):
        raise ValueError("Массивы должны иметь одинаковую длину.")
    combined = list(zip(values, names))
    combined.sort(reverse=True, key=lambda item: item[0])
    sorted_values, sorted_names = zip(*combined)
    return list(sorted_names), list(sorted_values)


def parse_timetable(name: str):
    html = parse_html(f"https://www.giantbomb.com/new-games")
    soup = BeautifulSoup(html, 'html.parser')
    games = soup.find_all('h3', class_ = 'title')
    types = soup.find_all('ul', class_ = 'system-list')
    times = soup.find_all ('time', class_ = 'date')
    quantypes = 10
    quangames = 0
    contentgame = []
    contenttype = []
    arrtypesname = ["NSW", "PS4", "PS5", "PC", "XONE", "XSX", "MAC", "ANDR", "IPHN", "IPAD"]
    arrtypesnumber = []
    for element in games:
        contentgame.append(str(element))
        quangames = quangames + 1
        print (str(element))
    for element in types:
        contenttype.append(str(element))
    print (contenttype)
    arrtypesnumber.append(str(contenttype).count('NSW') / 2)
    arrtypesnumber.append(str(contenttype).count('PS4') / 2)
    arrtypesnumber.append(str(contenttype).count('PS5') / 2)
    arrtypesnumber.append(str(contenttype).count('PC') / 2)
    arrtypesnumber.append(str(contenttype).count('XONE') / 2)
    arrtypesnumber.append(str(contenttype).count('XSX') / 2)
    arrtypesnumber.append(str(contenttype).count('MAC') / 2)
    arrtypesnumber.append(str(contenttype).count('ANDR') / 2)
    arrtypesnumber.append(str(contenttype).count('IPHN') / 2)
    arrtypesnumber.append(str(contenttype).count('IPAD') / 2)
    sortedtypesname, sortedtypesnumber = sort_arrays(arrtypesname, arrtypesnumber)
    print (sortedtypesname)
    print (sortedtypesnumber)
    input()
    return list(sortedtypesname), list(sortedtypesnumber)

contents = parse_timetable("pivogdumengo") 
input()