# Exercise in basic functions and control flow

get_weight = input('Enter the weight of your package in lbs: ')
weight = float(get_weight)


# Ground shipping
def ground_ship_calc(lbs):
    cost = 0
    if lbs <= 2:
        cost = 1.50 * lbs
    elif 2 < lbs <= 6:
        cost = 3.00 * lbs
    elif 6 < lbs <= 10:
        cost = 4.00 * lbs
    elif lbs > 10:
        cost = 4.75 * lbs
    return round(cost, 2) + 20


# Drone Shipping
def drone_ship_calc(lbs):
    cost = 0
    if lbs <= 2:
        cost = round((4.50 * lbs), 2)
    elif 2 < lbs <= 6:
        cost = round((9.00 * lbs), 2)
    elif 6 < lbs <= 10:
        cost = round((12.00 * lbs), 2)
    elif 10 < lbs <= 25:
        cost = round((14.25 * lbs), 2)
    elif lbs > 25:
        cost = ''
    return cost


ground = ground_ship_calc(weight)
prem_ground = 125
drone = drone_ship_calc(weight)

print(f'Ground shipping: £{ground:.2f}')
print(f'Premium ground shipping: £{prem_ground:.2f}')
if type(drone) == float:
    print(f'Drone shipping: £{drone}')
else:
    print('Weight exceeds maximum drone capacity of 25lbs')
