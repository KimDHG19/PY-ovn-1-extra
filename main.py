
number1 = input('Mata in ett tal ')
number2 = input('Mata in ett till tal ')

if number1 > number2:
    print(f'{number1} is greater than {number2}')

else:
    print(f'{number2} is greater than {number1}')


def c_to_f(c):
    return str((9 / 5) * c + 32) + ' F'


def f_to_c(f):
    return str((5 / 9) * (f - 32)) + ' °C'


degrees = float(input('Degrees: '))
action = input('Convert to Celsius or Fahrenheit? (C/F): ')

action = action.lower()

result = ''

if action == 'f':
    print(c_to_f(degrees))
elif action == 'c':
    print(f_to_c(degrees))

a = 10 > 11
b = 8 < 10
c = 34 == 34

if a == 'true':
    print('true')

elif b == 'true':
    print('true')

else:
    print('false')


if a == 'true' and b == 'true' and c == 'true':
    print('true')

else:
    print('false')


from math import modf

raw_minutes = int(input('Input minutes '))
if raw_minutes > 119:
    raw_minutes = raw_minutes + 1

elif raw_minutes > 63:
    raw_minutes = raw_minutes + 0.5

elif raw_minutes == 61:
    raw_minutes = raw_minutes + 0.5
minutes, hours = modf(raw_minutes / 60)

minutes *= 60

hours, minutes = int(hours), int(minutes)

hour_form = 'hour'
minute_form = 'minute'

if hours == 1:
    hour_form = 'hour'

if minutes == 1:
    minute_form = 'minute'

message = f'It is {hours} {hour_form}'
if minute_form == minutes:
    message += f' and {minutes} {minute_form}'
else:
    message += f' and {minutes} {minute_form}'
message += '.'

print(message)


product = str(input('Input product name: '))
product_price = float(input('Input product price: '))

action = input('Home delivery? (YES/NO): ')

delivery_fee = 0

if product_price < 10:
    delivery_fee = 2.00

else:
    delivery_fee = 3.00

print("Faktura")

print(product + "   " + str(product_price))

action = action.lower()

result = ''

if action == 'yes':
    print("delivery  " + str(delivery_fee))

total_price = product_price + delivery_fee

print("total price: " + str(total_price))



daily_acc = float(input('Input daily account balance: '))
savings_acc = float(input('Input savings account balance: '))

service_fee = 0

if daily_acc < 1000 or savings_acc < 1500:
    service_fee = 0.15

print(f"service fee: {service_fee}")





