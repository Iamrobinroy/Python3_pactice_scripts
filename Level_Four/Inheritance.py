class Samsung():
    # creating constructor
    def __init__(self):
        print('i am samsung')

    def makes_Screen(self):
        print('i make screen')

    def test(self):
        print('TEST1 : OK')
        print('TEST2 : OK')
        print('TEST3 : OK')
        print('TEST4 : OK')

#
# class iPhone(Samsung): #class name starts withcapital #giving access to the class Samsung
#     def __init__(self):
#         print('i am iPhone')
#
#     def a3chips(self):
#         print('i make a3 bionic chips')
#         #iPhone wants to use Samsung's test code
#     def itest(self):
#         print('A3: TEST : OK')
#         #super().test()
#
#         #method overridding
#     def makes_Screen(self):
#         print('i makes screen: Apple')


#creatting objects from the classes
# user = iPhone()
#
# user.a3chips()
# user.makes_Screen() #gets from class Samsung
#
user2 = Samsung()
user2.makes_Screen()

# user.itest()
# user.makes_Screen() #overridden

