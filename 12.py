amount = input('Enter amount :' )
vat = 0.23
vat_amount = float(amount) * vat
total_amount = float(amount) + vat_amount
print(f'Vat amount is {vat_amount}.')
print(f'Total amount with VAT is {total_amount}.')
