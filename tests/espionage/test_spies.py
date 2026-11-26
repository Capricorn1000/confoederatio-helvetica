"""Tests für das Spionagesystem."""

import sys
sys.path.insert(0, '../src')

from espionage.spies import Spy, hire_spy, pay_spy_maintenance, get_available_spies


def test_spy_creation():
    """Testen der Spion-Erstellung."""
    spy = Spy("Hans Müller", 5)
    assert spy.name == "Hans Müller"
    assert spy.skill_level == 5
    assert spy.target is None
    assert len(spy.evidence_collected) == 0


def test_spy_hire_cost():
    """Testen der Anstellungskosten."""
    spy = Spy("Test", 1)
    assert spy.hire_cost == 50
    
    spy2 = Spy("Test2", 10)
    assert spy2.hire_cost == 1800


def test_spy_maintenance_cost():
    """Testen der Aufrechterhaltungskosten."""
    spy = Spy("Test", 5)
    # 400 * 0.2 = 80
    assert spy.maintenance_cost == 80


def test_hire_spy_success():
    """Testen des erfolgreichen Anstellens eines Spions."""
    player = type('Player', (), {'cash': 1000, 'spies': []})()
    
    spy, cost = hire_spy(player, skill_level=3)
    
    assert spy is not None
    assert cost == 175
    assert player.cash == 825
    assert len(player.spies) == 1


def test_hire_spy_insufficient_funds():
    """Testen des Anstellens mit unzureichenden Mitteln."""
    player = type('Player', (), {'cash': 100, 'spies': []})()
    
    spy, cost = hire_spy(player, skill_level=5)
    
    assert spy is None
    assert "Nicht genug Geld" in cost


def test_pay_spy_maintenance():
    """Testen der Aufrechterhaltungsbezahlung."""
    player = type('Player', (), {'cash': 1000, 'spies': []})()
    
    spy = Spy("Hans", 5)
    player.spies.append(spy)
    
    cost = pay_spy_maintenance(player)
    
    assert cost == 80
    assert player.cash == 920


def test_get_available_spies():
    """Testen der verfügbaren Spione."""
    available = get_available_spies()
    
    assert len(available) == 10
    assert available[0]['skill_level'] == 1
    assert available[9]['skill_level'] == 10


if __name__ == "__main__":
    test_spy_creation()
    print("✓ test_spy_creation")
    
    test_spy_hire_cost()
    print("✓ test_spy_hire_cost")
    
    test_spy_maintenance_cost()
    print("✓ test_spy_maintenance_cost")
    
    test_hire_spy_success()
    print("✓ test_hire_spy_success")
    
    test_hire_spy_insufficient_funds()
    print("✓ test_hire_spy_insufficient_funds")
    
    test_pay_spy_maintenance()
    print("✓ test_pay_spy_maintenance")
    
    test_get_available_spies()
    print("✓ test_get_available_spies")
    
    print("\nAlle Spionage-Tests bestanden!")