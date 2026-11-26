"""Tests für das Beweissystem."""

import sys
sys.path.insert(0, '../src')

from espionage.evidence import evaluate_evidence, can_file_lawsuit, get_lawsuit_threshold


def test_evaluate_empty_evidence():
    """Testen der Bewertung leerer Beweise."""
    assert evaluate_evidence([]) == 0


def test_evaluate_single_evidence():
    """Testen der Bewertung eines einzelnen Beweises."""
    evidence = [{"type": "bookkeeping", "quality": 3}]
    # bookkeeping: 10 * 3 = 30
    assert evaluate_evidence(evidence) == 30


def test_evaluate_multiple_evidence():
    """Testen der Bewertung mehrerer Beweise."""
    evidence = [
        {"type": "bookkeeping", "quality": 2},   # 10 * 2 = 20
        {"type": "tax_evasion", "quality": 3}    # 25 * 3 = 75
    ]
    assert evaluate_evidence(evidence) == 95


def test_can_file_lawsuit_threshold():
    """Testen der Prozessschwelle."""
    threshold = get_lawsuit_threshold()
    
    assert can_file_lawsuit(threshold - 1) == False
    assert can_file_lawsuit(threshold) == True
    assert can_file_lawsuit(threshold + 10) == True


def test_evidence_value_range():
    """Testen des Wertebereichs."""
    from espionage.evidence import get_evidence_value_range
    
    min_val, max_val = get_evidence_value_range()
    
    assert min_val > 0
    assert max_val > min_val


if __name__ == "__main__":
    test_evaluate_empty_evidence()
    print("✓ test_evaluate_empty_evidence")
    
    test_evaluate_single_evidence()
    print("✓ test_evaluate_single_evidence")
    
    test_evaluate_multiple_evidence()
    print("✓ test_evaluate_multiple_evidence")
    
    test_can_file_lawsuit_threshold()
    print("✓ test_can_file_lawsuit_threshold")
    
    test_evidence_value_range()
    print("✓ test_evidence_value_range")
    
    print("\nAlle Beweis-Tests bestanden!")