"""Calculate and display combined miles per gallon obtained for all tankfuls.
Total miles driven divided by total gallons used"""

total_gallons = 0
total_miles = 0

current_gallons = float(input("Enter the gallons used (-1 to end): "))

while current_gallons != -1:
    current_miles = int(input("Enter the miles driven: "))
    current_ratio = current_miles / current_gallons
    print(f"The ration miles/gallons for this tank is: {current_ratio:.3f}")
    total_gallons += current_gallons
    total_miles += current_miles
    current_gallons = float(input("Enter the gallons used (-1 to end): "))

if total_gallons == 0:
    print("No data entered")
else:
    total_ratio = total_miles / total_gallons
    print(f"Overall average is: {total_ratio:.3f}")
