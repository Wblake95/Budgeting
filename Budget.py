#tracking money saved
months = 1
savings = 0
income = 0
spent = 0

income += int(input("Enter income for January: "))
spent += int(input("Enter spent for January: "))

print(f"month: {months}")
print(f"You have saved: ${savings + income - spent}")
print(f"You have earned: ${income}")
print(f"You have spent: ${spent}")

savings = savings + income - spent

while savings <= 10000:
    months += 1
    savings += income
    savings -= spent

if savings >= 10000:
    print(f"month: {months}")
    print(f"You have saved: ${savings + income - spent}")
    print(f"You have earned: ${income}")
    print(f"You have spent: ${spent}")
