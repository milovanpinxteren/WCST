
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

#####################################################Passing#######################################################

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