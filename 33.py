###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

celsius = input('Enter temperature in Celsius: ')
fahrenheit = round((9 / 5) * float(celsius) + 32, 2)
print(f'Temperature in Celsius: {celsius}, equals Fahrenheit: {fahrenheit}')
  