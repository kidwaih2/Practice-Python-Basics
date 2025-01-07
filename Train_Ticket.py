distance = int(input('How many kilometers are you travelling? '))
customer_type = input('Are you a frequent customer? ')

if (distance < 500 and customer_type == 'yes')
  print('The total cost of the ticket $50 CAD')

if (distance > 500 and customer_type == 'yes')
  print('The total cost of the ticket $100 CAD')

if (distance < 300 and customer_type == 'no')
  print('The total cost of the ticket $75 CAD')

if (distance > 300 and distance < 500 and customer_type == 'yes')
  print('The total cost of the ticket $150 CAD')

if (distance < 500 and customer_type == 'no')
  print('The total cost of the ticket $200 CAD')
