#tracking money saved
month = "January"
savings = 0
income = 0
spent = 0

income += int(input("Enter income for January: "))
spent += int(input("Enter spent for January: "))

print(month)
print(f"You have saved: ${savings + income - spent}")
print(f"You have earned: ${income}")
print(f"You have spent: ${spent}")
