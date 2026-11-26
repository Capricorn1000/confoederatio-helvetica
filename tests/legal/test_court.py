"""Tests für das Rechtssystem."""

import sys
sys.path.insert(0, '../src')

from legal.court import CourtCase, Witness


def test_court_case_creation():
    """Testen der Fall-Erstellung."""
    plaintiff = type('Player', (), {'name': 'Spieler'})()
    defendant = type('Rival', (), {'name': 'Hans Fugger'})()
    
    case = CourtCase(plaintiff, defendant)
    
    assert case.status == "filed"
    assert case.verdict is None
    assert len(case.evidence_plaintiff) == 0
    assert len(case.witnesses_plaintiff) == 0


def test_add_evidence():
    """Testen des Hinzufügens von Beweisen."""
    plaintiff = type('Player', (), {'name': 'Spieler'})()
    defendant = type('Rival', (), {'name': 'Hans Fugger'})()
    
    case = CourtCase(plaintiff, defendant)
    
    evidence = {"type": "bookkeeping", "quality": 3}
    case.add_evidence("plaintiff", evidence)
    
    assert len(case.evidence_plaintiff) == 1
    assert case.evidence_plaintiff[0] == evidence


def test_add_witness():
    """Testen des Hinzufügens von Zeugen."""
    plaintiff = type('Player', (), {'name': 'Spieler'})()
    defendant = type('Rival', (), {'name': 'Hans Fugger'})()
    
    case = CourtCase(plaintiff, defendant)
    
    witness = Witness("Anna Bauer", 7)
    case.add_witness("plaintiff", witness)
    
    assert len(case.witnesses_plaintiff) == 1
    assert case.witnesses_plaintiff[0].name == "Anna Bauer"


def test_calculate_verdict():
    """Testen der Urteilsberechnung."""
    plaintiff = type('Player', (), {'name': 'Spieler'})()
    defendant = type('Rival', (), {'name': 'Hans Fugger'})()
    
    case = CourtCase(plaintiff, defendant)
    
    # Beweise für Kläger hinzufügen (soll gewinnen)
    for i in range(5):
        case.add_evidence("plaintiff", {"type": "tax_evasion", "quality": 4})
    
    verdict, details = case.calculate_verdict(bribery_enabled=False)
    
    assert verdict == "plaintiff_wins"
    assert case.status == "verdict"


def test_witness_impact():
    """Testen der Zeugenwirkung."""
    witness = Witness("Test", 5)
    # credibility * 2 = 10
    assert witness.impact == 10


if __name__ == "__main__":
    test_court_case_creation()
    print("✓ test_court_case_creation")
    
    test_add_evidence()
    print("✓ test_add_evidence")
    
    test_add_witness()
    print("✓ test_add_witness")
    
    test_calculate_verdict()
    print("✓ test_calculate_verdict")
    
    test_witness_impact()
    print("✓ test_witness_impact")
    
    print("\nAlle Gerichts-Tests bestanden!")