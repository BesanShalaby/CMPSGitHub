


"""
Write a program that calculates the total amount of a meal purchased 
at a restaurant. The program should ask the user to enter the charge 
for the food, then calculate the amounts of a 18 percent tip 
and 7 percent sales tax. Display each of these amounts and the total.
    """

food_charge = float(input("Enter the charge for the food: QR "))

# Calculate the tip, tax, and total amount
tip = food_charge * 0.18
tax = food_charge * 0.07
total = food_charge + tip + tax

# Display the amounts
print(f"Tip: QR{tip:.2f}")
print(f"Sales Tax: QR{tax:.2f}")
print(f"Total Amount: QR{total:.2f}")