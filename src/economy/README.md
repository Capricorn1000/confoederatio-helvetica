# Wirtschaftssystem - Analyse & Spezifikation

## Original-Analyse (Fugger II)

Das Wirtschaftssystem von Fugger II ist das Herzstück des Spiels. Es umfasst:

### Handel zwischen Städten
- Spieler kauft Güter in einer Stadt und verkauft sie in einer anderen mit höherem Preis
- Preise variieren basierend auf Angebot, Nachfrage und historischen Ereignissen
- Transportzeit und -kosten müssen berücksichtigt werden
- Eskortierte Transporte schützen vor Räubern (gekennzeichnet durch gekreuzte Schwerter)

### Bankwesen & Finanzen
- Kreditaufnahme bei Banken mit Zinsen
- Wechselgeschäfte für internationale Transaktionen
- Kapitalverwaltung und Investitionsentscheidungen
- Gewinn/Verlust-Berechnung pro Handelsoperation

### Preisbildung
- Dynamische Preise basierend auf:
  - Lokalem Angebot und Nachfrage
  - Saisonalen Schwankungen
  - Historischen Ereignissen (Kriege, Ernten, etc.)
  - Spieleraktivitäten (Massenkauf senkt Preis)

### Auktionen
- Periodische Auktionen für seltene Güter und Kunstwerke
- Gebotsystem mit Zeitdruck
- Möglichkeit, uninteressante Objekte zu überspringen (ESC-Taste)

## Umsetzung in Confoederatio Helvetica

### Schweizer Kontext
Anstatt deutscher Städte werden Schweizer Handelszentren verwendet:
- **Zürich**: Textilien, Bankwesen
- **Basel**: Handel, Chemie (später), Rheinhafen
- **Genf**: Uhren, Seide, Genfersee-Handel
- **Bern**: Verwaltungszentrum, Landwirtschaft
- **Luzern**: Alpenhandel, Transit

### Internationale Handelspartner
- Venedig (Mittelmeerhandel)
- Florenz (Bankwesen, Kunst)
- Antwerpen (Niederlande, Textilien)
- London (England, Wolle)
- Lyon (Frankreich, Seide)

### Güterkategorien
1. **Agrarprodukte**: Getreide, Wein, Käse, Fleisch
2. **Textilien**: Wolle, Leinen, Seide, fertige Stoffe
3. **Metalle & Erze**: Eisen, Kupfer, Silber, Gold
4. **Handwerksgüter**: Waffen, Werkzeuge, Uhren
5. **Luxusgüter**: Gewürze, Farbstoffe, Kunstwerke, Edelsteine
6. **Rohstoffe**: Holz, Salz, Schwefel

### Preisberechnungsformel (Vorschlag)
```python
def calculate_price(good, city, year):
    base_price = good.base_price
    
    # Angebot/Nachfrage-Faktor
    supply_demand_factor = city.supply[good] / city.demand[good]
    
    # Saisonaler Faktor
    seasonal_factor = get_seasonal_factor(good, current_month)
    
    # Historischer Ereignis-Faktor
    event_factor = get_event_price_modifier(city, year)
    
    # Spieleraktivitäts-Faktor (Massenkauf senkt Preis)
    player_activity_factor = 1.0 - (city.player_purchases[good] * 0.01)
    
    final_price = base_price * supply_demand_factor * seasonal_factor * event_factor * player_activity_factor
    
    return max(final_price, good.minimum_price)
```

### Bankwesen-System
```python
class Bank:
    def __init__(self, city):
        self.city = city
        self.interest_rate = 0.08  # 8% Jahreszins (historisch realistisch)
        self.loans = []
    
    def take_loan(self, player, amount, duration_years):
        interest = amount * self.interest_rate * duration_years
        loan = Loan(player, amount, interest, duration_years)
        self.loans.append(loan)
        return loan
    
    def repay_loan(self, loan_id):
        # Zinsen berechnen und zurückzahlen
        pass
```

### Auktionssystem
- Periodische Auktionen (z.B. alle 6 Monate in großen Städten)
- Gebotsystem mit Mindestgebotserhöhung
- Zeitlimit pro Objekt (ESC zum Überspringen)
- Seltene Güter mit hohem Gewinnpotenzial

## Technische Umsetzung

### Dateien
- `trade.py`: Handelssystem, Kauf/Verkauf, Transport
- `banking.py`: Bankwesen, Kredite, Zinsen
- `prices.py`: Preisberechnung und -simulation

### Datenstrukturen
```python
class Good:
    name: str
    base_price: float
    category: str
    minimum_price: float
    
class City:
    name: str
    supply: dict[Good, int]
    demand: dict[Good, int]
    prices: dict[Good, float]
    
class TradeOperation:
    good: Good
    quantity: int
    buy_city: City
    sell_city: City
    transport_cost: float
    profit: float
```

## Offene Fragen
1. Wie komplex soll das Preisbildungssystem sein? (Einfach vs. realistisch)
2. Sollen Spieler eigene Produktionsstätten betreiben können?
3. Wie werden Transportzeiten simuliert? (Rundenbasiert oder Echtzeit?)
4. Soll es eine Börse für Futures/Optionen geben?