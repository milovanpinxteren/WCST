from scoutingtool.models import GeneralPlayerInfo


class FilterPlayers():
    def filter_players(self, criterea_list):
        queryset = GeneralPlayerInfo.objects.all()
        for criterium in criterea_list:
            if criterium['field'] == 'player_position':
                if criterium['value'] == '1':
                    queryset = queryset
                else:
                    queryset = queryset.filter(position_id=criterium['value'])
            elif criterium['field'] == 'player_age_min':
                queryset = queryset.filter(player_age__gte=criterium['value'])
            elif criterium['field'] == 'player_age_max':
                queryset = queryset.filter(player_age__lte=criterium['value'])
            else: #TODO: now sort the database on most important values
                print(queryset)
        return queryset
