"""
Dialoge & Menüs - Kauf/Verkauf, Gerichtsverfahren, etc.
"""


class TradeDialog:
    """Kauf/Verkauf-Dialog."""
    
    def __init__(self, city, goods):
        self.city = city
        self.goods = goods
    
    def show(self):
        """Dialog anzeigen."""
        print(f"Handel in {self.city}")
        for good in self.goods:
            print(f"  - {good.name}: {good.price} Gulden")


class CourtDialog:
    """Gerichtsverfahrens-Dialog."""
    
    def __init__(self, case):
        self.case = case
    
    def show(self):
        """Dialog anzeigen."""
        print("Gerichtsverhandlung")
        print(f"Klage: {self.case.plaintiff} vs. {self.case.defendant}")