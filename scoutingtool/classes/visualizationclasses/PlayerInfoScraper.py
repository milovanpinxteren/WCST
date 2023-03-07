from datetime import datetime
import re
from urllib.request import urlopen, Request

import js2xml as js2xml
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
            player_info_dict['Naam'] = player.player_name
            player_info_dict['Geboortedatum'] = "Geen info bekend"
            return player_info_dict
        resultsoup = BeautifulSoup(search_return)
        resultset = resultsoup.select(
            'div.large-12 > div.box > div.responsive-table > div.grid-view table.items > tbody > tr.odd > td > table.inline-table > tr > td')
        try:
            player_url = "https://www.transfermarkt.nl" + resultset[1].find('a', href=True)['href']
        except IndexError: #no player found on https://www.transfermarkt.nl
            player_info_dict['Naam'] = player.player_name
            player_info_dict['Geboortedatum'] = "Geen info bekend"
            return player_info_dict
        player_page = Request(player_url, headers={'User-Agent': 'Mozilla/5.0'})
        player_page_return = urlopen(player_page)
        player_resultsoup = BeautifulSoup(player_page_return)
        player_info_div = player_resultsoup.find(class_="info-table")
        player_info_resultset = player_info_div.select('span.info-table__content')

        #transferwaarde data
        transfer_value_dict = self.get_transfer_data(player_url)

        resultset_counter = 0
        playerinfodictmaker = PlayerInfoDictMaker()
        for tag in player_info_resultset:
            player_info_dict['Naam'] = player.player_name
            playerinfodictmaker.make_dict(tag, resultset_counter, player_info_resultset, player_info_dict)
            resultset_counter += 1
        return player_info_dict, transfer_value_dict

    def get_transfer_data(self, player_url):
        transfer_url = player_url.replace('profil', 'marktwertverlauf')
        transfer_page = Request(transfer_url, headers={'User-Agent': 'Mozilla/5.0'})
        transfer_page_return = urlopen(transfer_page)
        transfer_page_soup = BeautifulSoup(transfer_page_return)
        script = transfer_page_soup.find("script", text=re.compile("Highcharts.Chart")).text
        parsed = js2xml.parse(script)
        datalist = parsed.xpath('//property[@name="data"]//number/@value')
        transfer_datapoint_counter = 0
        transfer_values_dict = {}
        for i in datalist:
            if (transfer_datapoint_counter % 2) == 0: #transfervalue
                epochtime = int(datalist[transfer_datapoint_counter+1]) / 1000
                date = datetime.fromtimestamp(epochtime)
                transfer_values_dict[i] = str(date)
            transfer_datapoint_counter += 1
        return transfer_values_dict





