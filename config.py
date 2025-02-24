config = {
    "command_prefix": "!",
    "cogs": [
        "cogs.leaderboard.leaderboard",
        "cogs.fun.fun",
        "cogs.velocidrone.velocidrone",
        "cogs.util.util",
    ],
    "leaderboard": {
        "level_up_XP": 800,
        "random_xp_range": [15, 50],
        "delay_XP_seconds": 10,
        "leaderboard_save_interval_seconds": 25,
        "leaderboard_delete_after_seconds": 120,
        "save_location": "cogs/leaderboard/json/",
    },
    "velocidrone": {
        "track_update_interval": 200,
        "track_deprioritize_time": 86400,
        "velocidrone_edit_role": "Researcher",
        "save_location": "cogs/velocidrone/json/",
    },
    "util": {
        "save_location": "cogs/util/json/",
        "util_edit_role": "Researcher",
    },
}