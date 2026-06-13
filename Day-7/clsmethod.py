class Mobile():
    @classmethod    #Decorator
    def show_model(cls):
        print("REAL ME")

realme=Mobile()
Mobile.show_model()