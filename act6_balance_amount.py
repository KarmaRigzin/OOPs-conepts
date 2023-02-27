from bank_account import *

deposit_amt = SavingAccount()
print(f"Balnce Before Deposit : {deposit_amt.check_balance()}")

deposit_amt.deposit(500)
print(f"Balance after Deposit: {deposit_amt.check_balance()}")


