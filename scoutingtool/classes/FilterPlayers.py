from scoutingtool.classes.filterclasses.ShootingFilter import ShootingFilter
from scoutingtool.models import GeneralPlayerInfo


class FilterPlayers():
    def filter_players(self, criterea_list):
        shooting_fields = ['goals_per_90_mins', 'shots', 'shots_on_target', 'goals_per_shot', 'penalty_killer']
        shootingfilter = ShootingFilter()
        # same for passing etc
        queryset = GeneralPlayerInfo.objects.all()
        filtered_id_list = GeneralPlayerInfo.objects.all().values_list('id', flat=True)
        for criterium in criterea_list:
            if criterium['field'] == 'player_position':
                if criterium['value'] == '0':
                    queryset = queryset
                else:
                    queryset = queryset.filter(position_id=criterium['value'])
            elif criterium['field'] == 'player_age_min':
                queryset = queryset.filter(player_age__gte=criterium['value'])
            elif criterium['field'] == 'player_age_max':
                queryset = queryset.filter(player_age__lte=criterium['value'])
            #get list of ids based on players who perform better than average
            elif criterium['field'] in shooting_fields:
                filtered_id_list = shootingfilter.filter_players(criterium)

            if len(queryset.filter(id__in=filtered_id_list)) > 5: #To ensure that the there are at least 5 players left
                queryset = queryset.filter(id__in=filtered_id_list)
            elif len(queryset.filter(id__in=filtered_id_list)) <= 5:
                return queryset
        # TODO sort on most important criterea and select top 5
        return queryset
