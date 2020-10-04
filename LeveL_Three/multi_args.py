# #function to add two/definite numbers
# def addnums(num1, num2):
#     total = num1 + num2
#     return total
# #my_Val = addnums(3, 5)
# print(addnums(23, 54))

def addnums1(*nums):
    total = 0
    for var in nums:
     total = total + var
    return total

print(addnums1(12,1212,12,12))

