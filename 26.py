# circumference - obwód
# diameter - średnica

circumference = input('Enter tree circumference in cm: ')
tree_diameter = float(circumference) / 3.14
can_be_cut = float(tree_diameter) >= 50
print(f'Tree can be cut down: {can_be_cut}')