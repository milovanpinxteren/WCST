from urllib.request import urlopen, Request

from bs4 import BeautifulSoup

from scoutingtool.classes.visualizationclasses.PlayerInfoDictMaker import PlayerInfoDictMaker


class PlayerInfoScraper:
    def __init__(self):
        print('PLAYERINFOSCRAPER')

    def scrape_info(self, player):
        player_info_dict = {}
        player_for_search = player.player_name.replace(' ', '+')
        search_url = "https://www.transfermarkt.nl/schnellsuche/ergebnis/schnellsuche?query=" + player_for_search
        search_request = Request(search_url, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            search_return = urlopen(search_request)
        except UnicodeEncodeError:
            player_info_dict['Geboortedatum'] = "Geen info bekend"
            return player_info_dict
        resultsoup = BeautifulSoup(search_return)
        resultset = resultsoup.select(
            'div.large-12 > div.box > div.responsive-table > div.grid-view table.items > tbody > tr.odd > td > table.inline-table > tr > td')
        try:
            player_url = "https://www.transfermarkt.nl" + resultset[1].find('a', href=True)['href']
        except IndexError: #no player found on https://www.transfermarkt.nl
            player_info_dict['Geboortedatum'] = "Geen info bekend"
            return player_info_dict
        player_page = Request(player_url, headers={'User-Agent': 'Mozilla/5.0'})
        player_page_return = urlopen(player_page)
        player_resultsoup = BeautifulSoup(player_page_return)
        player_info_div = player_resultsoup.find(class_="info-table")
        player_info_resultset = player_info_div.select('span.info-table__content')

        resultset_counter = 0
        playerinfodictmaker = PlayerInfoDictMaker()
        for tag in player_info_resultset: #TODO: string cleaning
            playerinfodictmaker.make_dict(tag, resultset_counter, player_info_resultset, player_info_dict)
        return player_info_dict


