user_input = int(input('ENTER A NUMBER '))
print('Number = ', user_input)
if user_input >1:
    for i in range(2, user_input):
        if(user_input % i==0):
            print(user_input, 'is not a prime number')
            print(i, 'times', user_input//i, 'is', user_input)
            break
    else:
            print(user_input, 'is a prime number')

