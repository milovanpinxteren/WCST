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

        for criterium in criterea_list:
            if criterium['value'] == '0':
                filtered_queryset = queryset
            if criterium['field'] == 'player_position':
                filtered_queryset = queryset.filter(position_id=criterium['value'])
            elif criterium['field'] == 'player_age_min':
                filtered_queryset = queryset.filter(player_age__gte=criterium['value'])
            elif criterium['field'] == 'player_age_max':
                filtered_queryset = queryset.filter(player_age__lte=criterium['value'])
            elif criterium['field'] in self.shooting_fields:
                filtered_id_list = self.shootingfilter.filter_players(criterium)
                filtered_queryset = queryset.filter(id__in=filtered_id_list)
        #TODO: do this for passing, possession etc
            if len(filtered_queryset) >= 5:
                queryset = filtered_queryset
            elif len(filtered_queryset) < 5:
                return queryset
        return queryset
