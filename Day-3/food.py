def washhands():
    print("Wash your hands")
def servefood():
    print("Serve the food")
def eatfood():
    washhands()
    servefood()
    print("Eat the food")
    washhands()
def pay():
    print("pay the bill")

eatfood()
pay()