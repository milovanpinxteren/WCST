from scoutingtool.classes.visualizationclasses.PlayerInfoScraper import PlayerInfoScraper


class InfoGetter():
    def __init__(self):
        print('INFO GETTER')


    def get_transfermarkt_data(self, player):
        player_name = player
        playerinfoscraper = PlayerInfoScraper()
        player_info = playerinfoscraper.scrape_info(player_name)
        return player_info

