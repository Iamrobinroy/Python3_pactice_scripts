# def main():
#     print('hai')
#
# if __name__ == '__main__':
#     main()

def main(): #creating and reading the file
    file = open('myfile.txt', 'w+')
    for i in range(10):
        file.write('hi robin %d \n' %(i))
    file.close()

#READING A FILE
try:
    file = open('myddfile.txt', 'r')
    print('file read')
except IOError:
    print('error in reading file')
print('task done')
if file.mode == 'r':
    filecontent = file.read()
print(filecontent)



if __name__ == '__main__':
    main()