"""
Bankwesen - Kredite, Zinsen und Wechselgeschäfte.
"""


class Loan:
    """Kredit."""
    
    def __init__(self, player, amount, interest_rate, duration_years):
        self.player = player
        self.amount = amount
        self.interest_rate = interest_rate
        self.duration_years = duration_years
        self.interest = amount * interest_rate * duration_years
    
    def total_repayment(self):
        """Gesamt-Rückzahlungsbetrag."""
        return self.amount + self.interest


class Bank:
    """Bank in einer Stadt."""
    
    def __init__(self, city, interest_rate=0.08):
        self.city = city
        self.interest_rate = interest_rate  # 8% Jahreszins (historisch realistisch)
        self.loans = []
    
    def take_loan(self, player, amount, duration_years):
        """Kredit aufnehmen."""
        loan = Loan(player, amount, self.interest_rate, duration_years)
        self.loans.append(loan)
        return loan
    
    def repay_loan(self, loan_id):
        """Kredit zurückzahlen."""
        for i, loan in enumerate(self.loans):
            if id(loan) == loan_id:
                repayment = loan.total_repayment()
                del self.loans[i]
                return repayment
        return 0