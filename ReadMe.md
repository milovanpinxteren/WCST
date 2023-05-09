# World Cup Scouting Tool (WCST) ReadMe

## Setting up
- Clone this repository
- Open it in your IDE (Pycharm is used for this ReadMe)
- Connect a Postgres database (https://blog.nextideatech.com/how-to-create-a-django-app-and-connect-it-to-a-database/)
- Fill the database with the .csv files provided by the project developers
- Configure the main process and run it.
- Create an account in your IDE terminal with `python manage.py createsuperuser`
- Login with your account
- Remaining flow is explained in the video


## Database structure:
- GeneralPlayerInfo (stats + misc)
- Shooting
- Passing (passing + passing_types)
- Defense
- Possession
- DuelsandOffside

## Flow and use case
- User logs in and redirects to critereaselection page
- User selects criterea for player
  - e.g. Left back, younger than 25, attacking (lots of crosses), not aggresive (least yellow/red cards)
- Model finds player (by filtering/querying based on the passed criterea)
- Model finds info on external site and internal database and makes a dict of dicts of dicts with all relevant info
- Passes to frontend, JS + HTML + ChartJS + Django template language do visualizations and interactions


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


##Logic and how it works
- Criterea are passed to views.py
- views.py checks if form is valid and initiates the Selection and filtering procedure
- In Selection, the attributes are sorted on importance. 
- All players are filtered on passed position and age range
- This selection is filtered by only keeping the players that perform better than average for the first criterea
- Same for second, third, fourth and fifth criterea or if the list of players =< 5
- The list with the 5 best players is passed back to the view
- After this the InfoGetter is initialized.
- The Infogetter gets data from www.transfermarkt.com, a very reliable and big football database
- The Infogetter queries the database to get the values for each criterea for each player
- After this the selection is sorted on values for the most important criterea
- The information is stored in a dict of dicts of dicts/JSON and passed to frontend
- Visualizations are made in frontend (ChartJS, JS, Django template Language, HTML, CSS)
