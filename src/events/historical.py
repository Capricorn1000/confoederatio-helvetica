"""
Historische Ereignisse - Jahr-für-Jahr Narrative der Schweizer Geschichte.
"""


# Historische Ereignisse (Beispiele)
HISTORICAL_EVENTS = {
    1499: {
        "title": "Schwabenkrieg",
        "description": "Die Eidgenossen besiegen die Habsburger und gewinnen ihre Unabhängigkeit.",
        "effects": ["trade_boost"]
    },
    1513: {
        "title": "Italienfeldzüge",
        "description": "Schweizer Söldner erobern Mailand. Schweizer Ruf als Kämpfer wächst.",
        "effects": ["mercenary_demand_up"]
    },
    1520: {
        "title": "Reformation in Zürich",
        "description": "Ulrich Zwingli beginnt die Reformation in Zürich.",
        "effects": ["religious_tensions"]
    },
    1531: {
        "title": "Zweiter Kappelkrieg",
        "description": "Konflikt zwischen reformierten und katholischen Kantonen.",
        "effects": ["trade_disruption"]
    }
}


def get_event_for_year(year):
    """Historisches Ereignis für ein bestimmtes Jahr abrufen."""
    return HISTORICAL_EVENTS.get(year, None)