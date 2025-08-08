n = int(input("Enter a number for which you want to calculate the table: "))
i = int(input("enter till where you want to stop: "))
print(f"\nThe Multiplication table of {n}\n")
for i in range (1,i+1):
    print(f"{n} x {i} = {n*i}")
print("Hope you're satisfied with the tables")