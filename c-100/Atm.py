class Atm:
    def __init__(self, card_no, pin_no):
        self.card_no = card_no
        self.pin_no = pin_no
    def CashWithdrawl(self):
        print('Cash has been withdrawl')
    def BalanceEnquiry(self):
        print('You have 2000 rs')
    def CashDeposite(self):
        print('Cash has been deposited')

card = input('Enter the card number: \t')

pin = input('Enter the pin number: \t')

bank = Atm(card,pin)
while True:
    ans = int(input('Press 1 for Cash Withdrawl, 2 for Cash Deposite and 3 for Balance Enquiry: '))
    if ans == 1:
        bank.CashWithdrawl()
    elif ans == 2:
        bank.CashDeposite()
    elif ans == 3:
        bank.BalanceEnquiry()



        