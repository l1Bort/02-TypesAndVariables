speed_kmh = input('Enter vehicle speed: ')
speed_kmh = int(speed_kmh)
speed_valid = speed_kmh > 40 and speed_kmh < 140
print(f'Speed is valid: {speed_valid}')
