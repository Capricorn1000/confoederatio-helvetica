"""
Confoederatio Helvetica - Game Balance Configuration
Centralized tuning values for economy, military, and events.
Optimized for fair multiplayer competition (2-4 players).
"""

# Economy Settings
ECONOMY = {
    "base_prices": {
        "grain": 10,
        "wine": 25,
        "cheese": 15,
        "wool": 20,
        "iron": 30,
        "silver": 50,
    },
    "price_volatility": 0.15,  # ±15% price fluctuation
    "distance_factor": 0.001,  # Price increase per distance unit
    "trade_tax_rate": 0.05,  # 5% trade tax
    "initial_wealth": 1000,
}

# Military Settings
MILITARY = {
    "troop_costs": {
        "halberdier": 50,
        "crossbowman": 40,
        "cavalry": 80,
    },
    "troop_strengths": {
        "halberdier": 10,
        "crossbowman": 8,
        "cavalry": 15,
    },
    "upkeep_per_troop": 2,  # Gold per troop per year
    "battle_loss_factor": 0.3,  # 30% casualties in battle
}

# Event Settings
EVENTS = {
    "event_frequency": 0.15,  # 15% chance of random event per turn
    "historical_event_years": [1513, 1527, 1531, 1548, 1600],
    "adventure_cooldown": 3,  # Turns between adventures
}

# Multiplayer Settings
MULTIPLAYER = {
    "max_players": 4,
    "win_threshold_wealth": 50000,
    "game_duration_years": 100,
}

# UI Settings
UI = {
    "screen_width": 1024,
    "screen_height": 768,
    "target_fps": 30,
}
