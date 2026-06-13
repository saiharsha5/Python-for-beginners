slot=list(map(str,input("Time slots: ").split()))
req=(input("Req slot: "))
print("slot already book"if req in slot else "slot is available")
