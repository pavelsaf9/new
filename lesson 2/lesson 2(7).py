buying_a_car = 11000
part = 4
percent_bank = 25
percent_spending = 15

summ_total = buying_a_car*part
bank_account = (summ_total*percent_bank)/100
outlay = (summ_total*percent_spending)/100
spent = buying_a_car + bank_account + outlay
balance = summ_total - spent

print("Остаток наличных у Пети:", balance)
