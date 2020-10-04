#object oriented programming

class Phone:
    "A simple class for test"
    #COUPLE OF VARIABLES
    phone_version = "S10"
    brand_name = "samsung"
    user_name = ""
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
robin.BootLogo()
#accessing the string of the class
#robin.__doc__