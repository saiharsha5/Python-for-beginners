balance=10000

try:
    amount = int(input("Enter withdrawal amount: "))
    if amount>balance:
        raise ValueError("Insufficient balance")
    print("Withdrawal successful")
except ValueError as e:
    print("Transaction Failed: ",e)
