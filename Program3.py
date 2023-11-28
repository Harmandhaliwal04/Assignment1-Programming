Penny_value=1
Nickel_value=5  
Dime_value=10
Quarter_value=25
pennies_in_dollar=100
 
    
e=int(input("Enter the number of pennies"))
f=int(input("Enter the number of nickels"))
g=int(input("Enter the number of dimes"))
h=int(input("Enter the number of quarters"))

Totalcents=(e*Penny_value)+(f*Nickel_value)+(g*Dime_value)+(h*Quarter_value)
TotalDollars=Totalcents/pennies_in_dollar


if TotalDollars>1:
    print("Sorry, the amount you entered was more than one dollar.")

elif TotalDollars<1:
    print("Sorry, the amount you entered was less than one dollar.")
else:
    print("Congratulations!The amount you entered was exactly one dollar!You win the game!")    





