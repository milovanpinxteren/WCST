from scoutingtool.classes.visualizationclasses.DatabaseQuerier import DatabaseQuerier
from scoutingtool.classes.visualizationclasses.PlayerInfoScraper import PlayerInfoScraper


class InfoGetter():
    def __init__(self):
        print('INFO GETTER')


    def get_transfermarkt_data(self, player):
        player_name = player
        playerinfoscraper = PlayerInfoScraper()
        player_info = playerinfoscraper.scrape_info(player_name)
        return player_info

    def get_database_data(self, player, criterea_list):
        print('GET DATABASE INFO')
        #criterea_list is sorted, remove age and position and keep the 5 most important criterea
        databasequerier = DatabaseQuerier()
        important_criterea = criterea_list[3:8]
        criterea_values_dict = databasequerier.get_values_from_criterea(player, important_criterea)
        return criterea_values_dict


