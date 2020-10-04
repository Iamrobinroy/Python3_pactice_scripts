import string
import collections


print(string.ascii_uppercase)
print(string.ascii_lowercase)
def main():
    myd = collections.deque(string.ascii_lowercase)
    print('no of elements are: ', str(len(myd)))
    #printing with commas
    for i in myd:
        print(i, end=',')
    myd.pop()
    print(myd)
    myd.popleft()
    myd.rotate()
    print(myd)
    myd.rotate(10)
    print(myd)

#deque is doeuble ended que

#synatx to call the main method
if __name__ == '__main__':
    main()
