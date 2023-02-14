
IMPORTANCE_CHOICES = (
    (1, ("Very low importance")),
    (2, ("Low importance")),
    (3, ("Medium importance")),
    (4, ("High importance")),
    (5, ("Very high importance")),
)
#Every choicefield except IMPORTANCE_CHOICES is on a 0-3 scale

#################################################Goals and Shooting#####################################################
GOALS_CHOICES = (
    (0, ("No preference")),
    (1, ("Low amount of goals")),
    (2, ("Medium amount of goals")),
    (3, ("High amount of goals")),
)

SHOTS_CHOICES = (
    (0, ("No preference")),
    (1, ("Low amount of shots")),
    (2, ("Medium amount of shots")),
    (3, ("High amount of shots")),
)

SHOTS_ON_TARGET_CHOICES = (
    (0, ("No preference")),
    (1, ("Low percentage of shots on target")),
    (2, ("Medium percentage of shots on target")),
    (3, ("High percentage of shots on target")),
)

GOALS_PER_SHOT_CHOICES = (
    (0, ("No preference")),
    (1, ("Low percentage of goals per shot")),
    (2, ("Medium percentage of goals per shot")),
    (3, ("High percentage of goals per shot")),
)

PENALTY_KILLER_CHOICES = (
    (0, ("No preference")),
    (1, ("Misses most of his penalties")),
    (2, ("Scores most of his penalties")),
    (3, ("Scores (almost) all of his penalties"))
)

#####################################################Passing############################################################

PASSES_PER_90_MINS_CHOICES = (
    (0, ("No preference")),
    (1, ("Low amount of passes")),
    (2, ("Medium amount of passes")),
    (3, ("High amount of passes")),
)

PASSES_COMPLETED_CHOICES = (
    (0, ("No preference")),
    (1, ("Low amount of passes completed")),
    (2, ("Medium amount of passes completed")),
    (3, ("High amount of passes completed")),
)

PASSES_SHORT_CHOICES = (
    (0, ("No preference")),
    (1, ("Low amount of short passes")),
    (2, ("Medium amount of short passes")),
    (3, ("High amount of short passes")),
)

PASSES_MEDIUM_CHOICES = (
    (0, ("No preference")),
    (1, ("Low amount of medium passes")),
    (2, ("Medium amount of medium passes")),
    (3, ("High amount of medium passes")),
)

PASSES_LONG_CHOICES = (
    (0, ("No preference")),
    (1, ("Low amount of long passes")),
    (2, ("Medium amount of long passes")),
    (3, ("High amount of long passes")),
)

ASSISTS_PER_90_MINS_CHOICES = (
    (0, ("No preference")),
    (1, ("Low amount of assists")),
    (2, ("Medium amount of assists")),
    (3, ("High amount of assists")),
)

ASSISTED_SHOTS_PER_90_MINS_CHOICES = (
    (0, ("No preference")),
    (1, ("Low amount of assisted shots")),
    (2, ("Medium amount of assisted shots")),
    (3, ("High amount of assisted shots")),
)

CROSSES_PER_90_MINS_CHOICES = (
    (0, ("No preference")),
    (1, ("Low amount of crosses")),
    (2, ("Medium amount of crosses")),
    (3, ("High amount of crosses")),
)

#####################################################Defense############################################################
TACKLES_PER_90_MINS_CHOICES = (
    (0, ("No preference")),
    (1, ("Low amount of tackles")),
    (2, ("Medium amount of tackles")),
    (3, ("High amount of tackles")),
)

TACKLES_WON_PER_90_MINS_CHOICES = (
    (0, ("No preference")),
    (1, ("Low amount of tackles won")),
    (2, ("Medium amount of tackles won")),
    (3, ("High amount of tackles won")),
)

BLOCKS_PER_90_MINS_CHOICES = (
    (0, ("No preference")),
    (1, ("Low amount of blocks")),
    (2, ("Medium amount of blocks")),
    (3, ("High amount of blocks")),
)

INTERCEPTIONS_PER_90_MINS_CHOICES = (
    (0, ("No preference")),
    (1, ("Low amount of interceptions")),
    (2, ("Medium amount of interceptions")),
    (3, ("High amount of interceptions")),
)

CLEARENCES_PER_90_MINS_CHOICES = (
    (0, ("No preference")),
    (1, ("Low amount of clearances")),
    (2, ("Medium amount of clearances")),
    (3, ("High amount of clearances")),
)

ERRORS_PER_90_MINS_CHOICES = (
    (0, ("No preference")),
    (1, ("Low amount of errors")),
    (2, ("Medium amount of errors")),
    (3, ("High amount of errors")),
)

#####################################################Possession#########################################################

SHOT_CREATING_ACTIONS_PER_90_MINS_CHOICES = (
    (0, ("No preference")),
    (1, ("Low amount of shot creating actions")),
    (2, ("Medium amount of shot creating actions")),
    (3, ("High amount of shot creating actions")),
)

GOAL_CREATING_ACTIONS_PER_90_MINS_CHOICES = (
    (0, ("No preference")),
    (1, ("Low amount of goal creating actions")),
    (2, ("Medium amount of goal creating actions")),
    (3, ("High amount of goal creating actions")),
)

TOUCHES_PER_90_MINS_CHOICES = (
    (0, ("No preference")),
    (1, ("Low amount of touches")),
    (2, ("Medium amount of touches")),
    (3, ("High amount of touches")),
)

DRIBBLES_PER_90_MINS_CHOICES = (
    (0, ("No preference")),
    (1, ("Low amount of dribbles")),
    (2, ("Medium amount of dribbles")),
    (3, ("High amount of dribbles")),
)

COMPLETED_DRIBBLES_PER_90_MINS_CHOICES = (
    (0, ("No preference")),
    (1, ("Low amount of completed dribbles")),
    (2, ("Medium amount of completed dribbles")),
    (3, ("High amount of completed dribbles")),
)

MISCONTROLS_PER_90_MINS_CHOICES = (
    (0, ("No preference")),
    (1, ("Low amount of miscontrols")),
    (2, ("Medium amount of miscontrols")),
    (3, ("High amount of miscontrols")),
)

DISPOSSESSED_PER_90_MINS_CHOICES = (
    (0, ("No preference")),
    (1, ("Low amount of dispossessions")),
    (2, ("Medium amount of dispossessions")),
    (3, ("High amount of dispossessions")),
)

#################################################Duels and Offside######################################################

YELLOW_CARDS_PER_90_MINS_CHOICES = (
    (0, ("No preference")),
    (1, ("Low amount of yellow cards")),
    (2, ("Medium amount of yellow cards")),
    (3, ("High amount of yellow cards")),
)

RED_CARDS_PER_90_MINS_CHOICES = (
    (0, ("No preference")),
    (1, ("Low amount of red cards")),
    (2, ("Medium amount of red cards")),
    (3, ("High amount of red cards")),
)

FOULS_PER_90_MINS_CHOICES = (
    (0, ("No preference")),
    (1, ("Low amount of fouls")),
    (2, ("Medium amount of fouls")),
    (3, ("High amount of fouls")),
)

FOULED_PER_90_MINS_CHOICES = (
    (0, ("No preference")),
    (1, ("Low amount of times fouled")),
    (2, ("Medium amount of times fouled")),
    (3, ("High amount of times fouled")),
)

OFFSIDES_PER_90_MINS_CHOICES = (
    (0, ("No preference")),
    (1, ("Low amount of offsides")),
    (2, ("Medium amount of offsides")),
    (3, ("High amount of offsides")),
)

AERIALS_PER_90_MINS_CHOICES = (
    (0, ("No preference")),
    (1, ("Low amount of aerials")),
    (2, ("Medium amount of aerials")),
    (3, ("High amount of aerials")),
)

AERIALS_WON_PER_90_MINS_CHOICES = (
    (0, ("No preference")),
    (1, ("Low amount of aerials won")),
    (2, ("Medium amount of aerials won")),
    (3, ("High amount of aerials won")),
)