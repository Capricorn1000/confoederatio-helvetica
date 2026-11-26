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