from scoutingtool.classes.filterclasses.ShootingFilter import ShootingFilter
from scoutingtool.models import GeneralPlayerInfo, Shooting


class FilterPlayers():
    def __init__(self):
        self.shooting_fields = []
        for shooting_field in Shooting._meta.get_fields():
            self.shooting_fields.append(shooting_field.attname)
        self.shootingfilter = ShootingFilter()
        #TODO same for passing etc

    def filter_players(self, criterea_list):
        queryset = GeneralPlayerInfo.objects.all()
        filtered_id_list = GeneralPlayerInfo.objects.all().values_list('id', flat=True)

        for criterium in criterea_list:
            if len(queryset) >= 10:
                if criterium['field'] == 'player_position':
                    if criterium['value'] == '0':
                        queryset = queryset
                    else:
                        queryset = queryset.filter(position_id=criterium['value'])
                elif criterium['field'] == 'player_age_min':
                    queryset = queryset.filter(player_age__gte=criterium['value'])
                elif criterium['field'] == 'player_age_max':
                    queryset = queryset.filter(player_age__lte=criterium['value'])
                elif criterium['field'] in self.shooting_fields:
                    filtered_id_list = self.shootingfilter.filter_players(criterium)
            #TODO: do this for passing, possession etc
            elif len(queryset) < 10:
                print(queryset)
                #TODO: get more players/loosen constraints

            queryset = queryset.filter(id__in=filtered_id_list)
        return queryset
