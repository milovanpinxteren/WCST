# World Cup Scouting Tool (WCST) ReadMe

## Setting up
- Clone this repository
- Open it in your IDE (Pycharm is used for this ReadMe)
- Connect a Postgres database (https://blog.nextideatech.com/how-to-create-a-django-app-and-connect-it-to-a-database/)


 
admin
ww: woutweghorst123


## Database structure:
###### Keepers later toevoegen (beginnen met spelers)

- GeneralPlayerInfo (stats + misc)
- Shooting
- Passing (passing + passing_types)
- Defense
- Possession
- DuelsandOffside

## Flow and use case
Scouts can use this to find the perfect player for the need of the club/team
- User logs in and redirects to critereaselection page
- User selects criterea for player
  - e.g. Left back, younger than 25, attacking (lots of crosses), not aggresive (least yellow/red cards)
- Model finds player
- Model finds info on external site and internal database and makes a dict of dicts of dicts with all relevant info
- Passes to frontend, JS + HTML + ChartJS do visualizations and interactions


## User Input Form stucture
- select important attributes (high/low/no preference (default))
- Give importance weight to attributes (high - low 5 point scale)
  - General
    - Position 
    - Min age
    - Max age
    - Optional: minutes per game
  - Shooting
    - Goals per 90 min
    - Shots per 90 mins
    - Shots on target percentage
    - Goals per shot
    - Free-kick taker
    - Penalty taker
    - Optional: Expected goals per match (kan dit?)
  - Passing
    - passes per 90 min (passes and minutes_90s)
    - passes completed percentage
    - passes short percentage
    - passes medium percentage
    - passes long percentage
    - assists per 90 mins (assists and minutes_90s)
    - assisted shots per 90 mins (assisted_shots and minutes_90s)
    - crosses per 90 mins (from misc table)
    - passes into penalty area per 90 mins (optional)
    - crosses into penalty area per 90 mins (optional)
    - progressive passes per 90 mins (optional)
  - Chance/Goal creation (moved to possession)
  - Defense
      - tackles per 90 mins
      - tackles won per 90 mins
      - blocks per 90 mins
      - interceptions per 90 mins
      - clearences per 90 mins
      - errors per 90 mins
  - Possession
      - Shot creating actions per 90 mins (from gca)
      - Goal creating actions per 90 mins (from gca)
      - touches per 90 mins
      - dribbles per 90 mins
      - completed dribbles percentage
      - miscontrols per 90 mins
      - dispossessed per 90 mins
  - DuelsandOffside
      - yellow cards per 90 mins
      - red cards per 90 mins
      - fouls per 90 mins
      - fouled per 90 mins
      - offsides per 90 mins
      - aerials per 90 mins
      - aerials won percentage

## Dict format (which is passed to front-end)
{1: {'id': 1, 'general_player_info': {'Geboortedatum': 'datum', 'Geboorteplaats': 'plaats', etc},
              'data_for_vis_1': {'skill_1': [data], 'skill_2': [data]},
              'data_for_vis_2': {'skill_1': [data], 'skill_2': [data]}
    }
2: {'id': 2, 'general_player_info': {'Geboortedatum': 'datum', 'Geboorteplaats': 'plaats', etc},
              'data_for_vis_1': {'skill_1': [data], 'skill_2': [data]},
              'data_for_vis_2': {'skill_1': [data], 'skill_2': [data]},
  }
enzovoort voor 5 spelers
}
