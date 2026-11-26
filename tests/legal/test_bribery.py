"""Tests für das Bestechungssystem."""

import sys
sys.path.insert(0, '../src')

from legal.bribery import calculate_bribe_effectiveness, risk_of_discovery


def test_bribe_effectiveness_zero():
    """Testen der Wirksamkeit bei null Betrag."""
    assert calculate_bribe_effectiveness(0) == 0


def test_bribe_effectiveness_positive():
    """Testen der positiven Wirksamkeit."""
    effectiveness = calculate_bribe_effectiveness(100, difficulty=5)
    
    # 100 * 0.5 * (1 - 5*0.08) = 50 * 0.6 = 30
    assert effectiveness == 30


def test_bribe_difficulty_reduces_effectiveness():
    """Testen dass Schwierigkeit die Wirksamkeit reduziert."""
    easy = calculate_bribe_effectiveness(100, difficulty=1)
    hard = calculate_bribe_effectiveness(100, difficulty=9)
    
    assert easy > hard


def test_risk_of_discovery_zero():
    """Testen des Entdeckungsrisikos bei null Betrag."""
    assert risk_of_discovery(0) == 0.0


def test_risk_of_discovery_increases_with_amount():
    """Testen dass Risiko mit Betrag steigt."""
    small = risk_of_discovery(50, skill_level=5)
    large = risk_of_discovery(500, skill_level=5)
    
    assert large > small


def test_risk_decreases_with_skill():
    """Testen dass Risiko mit Geschicklichkeit sinkt."""
    low_skill = risk_of_discovery(100, skill_level=1)
    high_skill = risk_of_discovery(100, skill_level=9)
    
    assert low_skill > high_skill


if __name__ == "__main__":
    test_bribe_effectiveness_zero()
    print("✓ test_bribe_effectiveness_zero")
    
    test_bribe_effectiveness_positive()
    print("✓ test_bribe_effectiveness_positive")
    
    test_bribe_difficulty_reduces_effectiveness()
    print("✓ test_bribe_difficulty_reduces_effectiveness")
    
    test_risk_of_discovery_zero()
    print("✓ test_risk_of_discovery_zero")
    
    test_risk_of_discovery_increases_with_amount()
    print("✓ test_risk_of_discovery_increases_with_amount")
    
    test_risk_decreases_with_skill()
    print("✓ test_risk_decreases_with_skill")
    
    print("\nAlle Bestechungs-Tests bestanden!")