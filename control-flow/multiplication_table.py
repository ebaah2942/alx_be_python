number = int(input("Enter a number to see its multiplication table: "))

for user_number in range(1, 11):
    product = number * user_number
    print(f"{number} x {user_number} = {product}")