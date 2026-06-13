num=int(input("number: "))
for i in range(1,11):
    print(f"Multiplication table of {i}: ")
    print('===============================')
    for j in range (10,0,-1):
        print(f"{i} * {j} = {i*j}")

