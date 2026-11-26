"""
Preisberechnung und -simulation.
"""

import random


def calculate_price(good, city, year):
    """
    Preis für ein Gut in einer Stadt berechnen.
    
    Basierend auf:
    - Basispreis des Gutes
    - Lokalem Angebot und Nachfrage
    - Saisonalem Faktor
    - Historischen Ereignissen
    - Spieleraktivitäten (Massenkauf senkt Preis)
    """
    base_price = good.base_price
    
    # Angebot/Nachfrage-Faktor
    supply_demand_factor = city.supply.get(good.name, 100) / max(city.demand.get(good.name, 1), 1)
    
    # Saisonaler Faktor (vereinfacht)
    seasonal_factor = random.uniform(0.9, 1.1)
    
    # Historischer Ereignis-Faktor (vereinfacht)
    event_factor = 1.0
    
    # Spieleraktivitäts-Faktor (Massenkauf senkt Preis)
    player_activity_factor = 1.0 - (city.player_purchases.get(good.name, 0) * 0.01)
    
    final_price = base_price * supply_demand_factor * seasonal_factor * event_factor * player_activity_factor
    
    return max(final_price, good.minimum_price)