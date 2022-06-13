import requests
from requests import get
from bs4 import BeautifulSoup
def metacritic_web_scrapper(time, platform):
    url = "https://www.metacritic.com/browse/games/score/metascore/%s/%s/filtered?sort=desc" % (time, platform)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    games = soup.findAll('tr')
    ans = "" #change var name
    for i in range (0, len(games), 2):
        ans += str((i + 2)//2) + ". " + games[i].h3.text + ", critics rating: " + games[i].div.findChild('div').text + "\n\n"
    return ans

def write_to_file(games):
    return

def main():
    #time = input("")
    print(metacritic_web_scrapper("all", "wii-u"))

main()