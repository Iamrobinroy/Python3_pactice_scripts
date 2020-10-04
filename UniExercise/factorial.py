##TODO
#factorails are only available for positive integers
# for 0:1
#
#1*2*3*4*5
#
#5*4*3*2*1


number = int(input('enter a number: '))
factorial = 1
if number < 0:
    print('cant take -ve input: ')
elif number == 0:
    print('factorial is 1')
else:
    for i in range(1, number + 1):
        factorial = factorial * i #factorial value chnages and stores and multiply
    print('the result is', factorial)


