outside_fee = 30 
kill = False #to easily stop the code

print("Please no capital letters input.")
try :
  weight = float(input("Enter Weight (in kg): "))
  if weight > 20:
    print('Too heavy (max 20 kg)')
    kill = True
  if weight <= 0:
    print('Please enter a valid weight')
    kill = True
except ValueError :
  print('Please enter a valid weight')
  kill = True

if kill == False :
  destin = str(input("Enter Destination (bangkok or other): "))
  if destin != "bangkok" and destin != "other" :
    print('Unknown destination')
    kill = True

if kill == False :
  express = str(input("Express (yes or no): "))
  if express != "yes" and express != "no" :
    print('Please enter a valid option') #Add this just in case. 
    kill = True


if weight > 5 and kill == False: #cost determination.
  cost = 150
elif weight > 1 :
  cost = 80
elif weight <= 1 :
  cost = 40


if destin == "other" and kill == False: #final output.
  cost += outside_fee
  if express == "yes" :
    cost = cost*2
  print(f"Shipping cost: {cost} baht")
elif kill == False :
  if express == "yes" :
    cost = cost*2
  print(f"Shipping cost: {cost} baht")
