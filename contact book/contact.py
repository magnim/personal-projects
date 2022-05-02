'''
Author : Magnim

'''

import psycopg2 as pg2

hostname = input('Hostname : ')
database = input('DATABASE : ')
username = input('USER : ')
pwd = input('PASSWORD : ')
port_id = 5432
conn = None
cur = None


def create():
    create_query = '''
    CREATE TABLE IF NOT EXISTS contacts(
        contact_name VARCHAR(40) UNIQUE NOT NULL,
        contact_number VARCHAR(20) UNIQUE NOT NULL,
        work_phone VARCHAR(20),
        email VARCHAR(110)
    )
    '''
    cur.execute(create_query)
    conn.commit()
 

def insert():
    try:
        print("Make sure you give a unique name to the contact or add something to differentiate between contacts")
        contact_name = input('Name:')
        contact_number = input('Contact Number : ')
        contact_work_number = input('Contact Number[Work] : ')
        contact_email = input('Contact email : ')
        insert_query = '''
        INSERT INTO contacts(contact_name,contact_number,work_phone,email) VALUES ('{0}','{1}','{2}','{3}')
        '''.format(contact_name,contact_number,contact_work_number,contact_email)
        cur.execute(insert_query)
        conn.commit()
    except pg2.errors.UniqueViolation as error:
        print('Duplicate Name or Number already exists')
    
    
def update():
    to_update = True
    while to_update:
        name_contact = input('Give the name of contact which you want to update : ') 
        name_query = '''SELECT contact_name FROM contacts WHERE contact_name = '{0}' '''.format(name_contact)
        cur.execute(name_query)
        name_found = cur.fetchall()
        if bool(name_found) == False:
            print("There is no contact {}".format(name_contact))
        while bool(name_found):
            update_choice = int(input('''
                    what do you want to update
                    1.contact_number
                    2.contact number[work]
                    3.email
                    =>  '''))
            try:
                choice_list = ['contact_number', 'work_phone', 'email']
                column = choice_list[update_choice - 1]
                update_info = input("give update information for {0} of {1} : ".format(column,name_contact))
                update_query = '''
                UPDATE contacts SET {0} = '{1}' WHERE contact_name = '{2}'
                '''.format(column,update_info,name_contact)
                cur.execute(update_query)
                conn.commit()
                to_update = name_found = False
            except Exception:
                print('Please select from the above Options')

def read():
    cur.execute("SELECT * FROM contacts")
    list_contacts = cur.fetchall()
    print("\nLIST OF CONTACTS\n")
    for i in list_contacts:
        print("name = {} : number = {} : number[work] = {} : email = {}".format(i[0],i[1],i[2],i[3]))

def delete():
    name_contact = input('Give the name of contact which you want to update : ') 
    cur.execute("DELETE FROM contacts WHERE contact_name = '{}' ".format(name_contact))
    conn.commit()

try:
    conn = pg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )
    print('Connection Establlished')
    cur = conn.cursor()
    
    create()
    read()

    active = True
    while active:
        user_input = input('''
        CHOOSE YOUR CHOICE:
        1.CREATE CONTACT
        2.UPDATE
        3.READ
        4.DELETE
        5.EXIT
        =>
        ''')
        if user_input == '1':
            insert()
        if user_input == '2':
            update()
        if user_input == '3':
            read()
        if user_input == '4':
            delete()
        if user_input == '5':
            active = False

except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:    
        conn.close()

