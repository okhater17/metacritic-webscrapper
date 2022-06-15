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
    return ans[0: len(ans) - 2]

def write_to_file(games):
    return

def main():
    platforms = ["ps2", "ps3", "ps4", "pc", "xbox360", "xboxone", "xbox-series-x", "n64", "switch", "wii", "wii-u",
                 "3ds"]
    print("1. PS2\n2. PS3\n3. PS4\n4. PC\n5. Xbox 360\n6. Xbox One\n7. Xbox Series X\n8. N64\n9. Switch\n10. Wii\n"
          "11. Wii-U\n12. 3DS")
    platform = int(input("Please pick a platform by typing in the corresponding number"))
    print(platforms[platform - 1])
    print(metacritic_web_scrapper("all", platforms[platform - 1]))

main()