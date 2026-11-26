"""
Handelssystem - Kauf, Verkauf und Transport von Gütern.
"""


class TradeOperation:
    """Einzelne Handelsgeschäft."""
    
    def __init__(self, good, quantity, buy_city, sell_city):
        self.good = good
        self.quantity = quantity
        self.buy_city = buy_city
        self.sell_city = sell_city
        self.transport_cost = 0.0
        self.profit = 0.0
    
    def calculate_profit(self, buy_price, sell_price):
        """Gewinn berechnen."""
        revenue = sell_price * self.quantity
        cost = buy_price * self.quantity + self.transport_cost
        self.profit = revenue - cost
        return self.profit


def buy_good(player, city, good_name, quantity, price):
    """Gut in einer Stadt kaufen."""
    total_cost = price * quantity
    
    if player.cash < total_cost:
        return False, "Nicht genug Geld"
    
    # Geld abziehen
    player.cash -= total_cost
    
    # Gut zum Inventar hinzufügen
    if good_name not in player.goods:
        player.goods[good_name] = 0
    player.goods[good_name] += quantity
    
    # Angebot der Stadt reduzieren
    city["supply"][good_name] -= quantity
    
    return True, f"Kaufte {quantity}x {good_name} für {total_cost:.2f} Gulden"


def sell_good(player, city, good_name, quantity, price):
    """Gut in einer Stadt verkaufen."""
    if good_name not in player.goods or player.goods[good_name] < quantity:
        return False, "Nicht genug vom Gut im Inventar"
    
    total_revenue = price * quantity
    
    # Geld hinzufügen
    player.cash += total_revenue
    
    # Gut aus Inventar entfernen
    player.goods[good_name] -= quantity
    if player.goods[good_name] == 0:
        del player.goods[good_name]
    
    # Nachfrage der Stadt reduzieren
    city["demand"][good_name] -= quantity
    
    return True, f"Verkaufte {quantity}x {good_name} für {total_revenue:.2f} Gulden"