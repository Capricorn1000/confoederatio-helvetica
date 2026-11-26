"""
Kartenansicht - Schweizer Karte mit Städten und Handelsrouten.
"""


class MapView:
    """Kartenansicht."""
    
    def __init__(self):
        self.cities = []
        self.routes = []
    
    def add_city(self, city):
        """Stadt zur Karte hinzufügen."""
        self.cities.append(city)
    
    def show(self):
        """Karte anzeigen (vereinfacht als Text)."""
        print("Schweizer Karte")
        print("=" * 30)
        for city in self.cities:
            print(f"  {city.name}")