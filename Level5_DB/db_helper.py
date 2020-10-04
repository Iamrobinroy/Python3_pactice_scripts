import sqlite3

db = "my_todo.db"
table_name = "task"
conn = sqlite3.connect(db) #db is database name

#creating a cursor
c = conn.cursor() #for putting up all the operations
#we use the referance of this cursor


def create_table():
    sql = 'CREATE A TABLE IF NOT EXISTS ' + table_name \
    + '(ID INTEGER PRIMARY KEY AUTOINCREMENT, Taskname'\
      ' text)'
    c.execute(sql) #either we call cll the abobe sql statement inside the c.execute or we can write in in c.execute

#pass method is a statment for futire code


def data_entry():
    c.execute("INSERT INTO " + table_name + " (TaskName) VALUES (?)", [task])
    print('task is added in db')
    conn.commit()

# * means all


def print_data():
    sql = "SELECT * FROM " + table_name
    c.execute(sql)
    for row in c.fetchall():
        print(row[0], "-->", row[1])


def delete_task(index):
    c.execute('DELETE FROM ' + table_name + ' WHERE ID=?', (index, ))
    print('deleted')


def close_cursor():
    c.close()
    conn.close()

