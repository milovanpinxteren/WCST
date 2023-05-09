from scoutingtool.classes.filterclasses.DefenseFilter import DefenseFilter
from scoutingtool.classes.filterclasses.DuelsandOffsideFilter import DuelsandOffsideFilter
from scoutingtool.classes.filterclasses.PassingFilter import PassingFilter
from scoutingtool.classes.filterclasses.PossessionFilter import PossessionFilter
from scoutingtool.classes.filterclasses.ShootingFilter import ShootingFilter
from scoutingtool.models import GeneralPlayerInfo, Shooting, Passing, Defense, Possession, DuelsandOffside


class FilterPlayers():
    def __init__(self):
        self.shooting_fields = []
        self.passing_fields = []
        self.defense_fields = []
        self.possession_fields = []
        self.duelsandoffside_fields = []

        for shooting_field in Shooting._meta.get_fields():
            self.shooting_fields.append(shooting_field.attname)
        for passing_field in Passing._meta.get_fields():
            self.passing_fields.append(passing_field.attname)
        for defense_field in Defense._meta.get_fields():
            self.defense_fields.append(defense_field.attname)
        for possession_field in Possession._meta.get_fields():
            self.possession_fields.append(possession_field.attname)
        for duelsandoffside_field in DuelsandOffside._meta.get_fields():
            self.duelsandoffside_fields.append(duelsandoffside_field.attname)

        self.shootingfilter = ShootingFilter()
        self.passingfilter = PassingFilter()
        self.defensefilter = DefenseFilter()
        self.possessionfilter = PossessionFilter()
        self.duelsandoffsidefilter = DuelsandOffsideFilter()

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
            elif criterium['field'] in self.passing_fields:
                filtered_id_list = self.passingfilter.filter_players(criterium)
                filtered_queryset = queryset.filter(id__in=filtered_id_list)
            elif criterium['field'] in self.defense_fields:
                filtered_id_list = self.defensefilter.filter_players(criterium)
                filtered_queryset = queryset.filter(id__in=filtered_id_list)
            elif criterium['field'] in self.possession_fields:
                filtered_id_list = self.possessionfilter.filter_players(criterium)
                filtered_queryset = queryset.filter(id__in=filtered_id_list)
            elif criterium['field'] in self.duelsandoffside_fields:
                filtered_id_list = self.duelsandoffsidefilter.filter_players(criterium)
                filtered_queryset = queryset.filter(id__in=filtered_id_list)

            if len(filtered_queryset) >= 5:
                queryset = filtered_queryset
            elif len(filtered_queryset) < 5:
                return queryset
        return queryset
