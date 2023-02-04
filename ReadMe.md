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
- GoalCreatingActions
- Defense
- Possession
- PlayingTime

## Flow and use case
Scouts can use this to find the perfect player for the need of the club/team
- User logs in and redirects to critereaselection page
- User selects criterea for player
  - e.g. Left back, younger than 25, attacking (lots of crosses), not aggresive (least yellow/red cards)
- Model finds player
- Show stats/visualization of the player, compared to other players who fit the criterea


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
    - passes per 90 min
    - passes completed percentage
    - passes short percentage
    - passes medium percentage
    - passes long percentage
    - assists per 90 mins
    - assisted shots per 90 mins
    - passes into penalty area per 90 mins
    - crosses into penalty area per 90 mins
    - progressive passes per 90 mins
  - Chance/Goal creation
  - Defense
  - Possesion
  - 