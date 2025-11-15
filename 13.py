price = input('Enter price: ')
discount = input('Enter discount %: ')
discount_amount = float(price) * float(discount) / 100
final_price = float(price) - discount_amount
print(f'Entered price: {price}')
print(f'Entered discount %: {discount_amount}')
print(f'Price with discount: {final_price}.')
print(f'Reduction: {discount_amount}.')