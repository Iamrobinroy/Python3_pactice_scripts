import db_helper


def main():
    run = 1
    db_helper.create_table()

    while run:
        print("\n")
        print('1. INSERT A TASK \n'
              '2. View tasks \n'
              '3. Delete tasks \n'
              '4. EXIT \n')
        x = input(" Enter your choice: ")

        if x == "1":
            task = str(input("Enter your task: "))
            db_helper.data_entry(task)

        elif x == "2":
            db_helper.print_data()

        elif x == "3":
            IndexToDelete = int(print('enter the Task index to delete:'))
            db_helper.delete_task(IndexToDelete)

        elif x == "4":
            run = 0

        else:
            print('choose a valid option')

    db_helper.close_cursor()


if __name__ == '__main__': main()
