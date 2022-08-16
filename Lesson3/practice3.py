# Example 1 (PZ_3)
print("\nExample 1 (multiplication)")
number = int(input("Enter number from 1 to 9: "))

for i in range(1, 11):
    result = number * i
    print(number, "*", i, "=", result)

# Example 2 (PZ_3)
print("\nExample 2 (currency exchange)")
USDUAH = 28.11
EURUAH = 32.00


curr = int(input("Select currency for exchange: \n\t 1 - USD \n\t 2 - EUR \n\t Choice: "))
amount = int(input("\n Enter amount to sell: "))

if curr == 1:
    amount_of_UAH = USDUAH * amount
    print("You have now ", amount_of_UAH, "hryvnas.")
elif curr == 2:
    amount_of_UAH = EURUAH * amount
    print("You have now ", amount_of_UAH, "hryvnas.")


choice = input("Do you want to continue? [Y/N]")

