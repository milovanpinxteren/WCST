from urllib.request import urlopen, Request

from bs4 import BeautifulSoup


class PlayerInfoScraper:
    def __init__(self):
        print('PLAYERINFOSCRAPER')

    def scrape_info(self, player):
        player_for_search = player.player_name.replace(' ', '+')
        search_url = "https://www.transfermarkt.nl/schnellsuche/ergebnis/schnellsuche?query=" + player_for_search
        print(search_url)
        # resultpage = requests.get(search_url)
        # resultsoup = BeautifulSoup(resultpage.content, "html.parser")
        search_request = Request(search_url, headers={'User-Agent': 'Mozilla/5.0'})
        search_return = urlopen(search_request)
        resultsoup = BeautifulSoup(search_return)
        resultset = resultsoup.select(
            'div.large-12 > div.box > div.responsive-table > div.grid-view table.items > tbody > tr.odd > td > table.inline-table > tr > td')

        player_url = "https://www.transfermarkt.nl/" + resultset[1].find('a', href=True)['href']
        print(player_url)
        player_page = Request(player_url, headers={'User-Agent': 'Mozilla/5.0'})

