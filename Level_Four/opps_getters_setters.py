#object oriented programming

class Phone:
    "A simple class for test"
    #COUPLE OF VARIABLES
    phone_version = "S10"
    brand_name = "samsung"
    user_name = ""
    model = 'S10+'

    #prevent the 'model' from changing
    #getters - get value from class
    def get_model(self):
        return self.model
        #return "S10+"

    #setter - set the value of the model
    def set_model(self, val):
        self.model = "S10+, " + val

    #every class by default create a constructor, it is always good to create ourselves one
    #it is very unique to a class
    #creating a constructor
    def __init__(self, user_name):
        self.user_name = user_name


    #Creating method and accessing any variables
    def BootLogo(self):
        print('SAMSUNG', self.phone_version)


#creating object
robin = Phone("Robin Phone")
# robin.model = "iphone" #changing variables of the class
robin.set_model("iPhone")
print(robin.get_model())

robin.BootLogo()
#accessing the string of the class
#robin.__doc__