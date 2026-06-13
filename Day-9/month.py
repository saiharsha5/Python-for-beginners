try:
    monthly_sal=float(input("Enter monthly salary: "))
    if (monthly_sal<=0):
        raise ValueError
    annual_sal=monthly_sal*12
    print("annual salary:",annual_sal)
except ValueError:
    print("Please enter a valid salary amount.")