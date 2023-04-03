import sqlite3
from datetime import datetime

new_date = datetime.now()
date = new_date.replace(microsecond = 0)

user_dictionary = {'user_id':'User ID','first_name':'First Name','last_name':'Last Name','phone':'Phone Number','email':'Email','password':'Password','date_created':'Date Created','hire_date':'Hire Date','user_type':'User Type','active':'Active'}
competency_dictionary = {'competency_id':'Competency ID','name':'Name','date_created':'Date Created','active':'Active'}

def create_schema():
    with open('schema.sql','rt') as my_schema:
        queries = my_schema.read()
        cursor.executescript(queries)

def create_schema_2():
    with open('schema_2.sql','rt') as my_schema:
        queries = my_schema.read()
        cursor.executescript(queries)
        connection.commit()


def view_all_users_in_a_list():
    pass

def search_for_users_by_first_or_last_name():
    pass

def view_a_report_of_all_users_and_their_competency_levels_for_a_given_competency():
    pass

def view_a_competency_level_for_an_individual_user():
    pass

def view_a_list_of_assessments_for_a_given_user():
    pass





def add_a_user(first_name, last_name, phone, email, password, date, user_type):
    query1 = 'INSERT INTO Users(first_name, last_name, phone, email, password, date_created, hire_date, user_type) VALUES(?,?,?,?,?,?,?,?);'
    cursor.execute(query1, (first_name, last_name, phone, email, password, date, date, user_type))
    # input('Press enter to finish adding each submission: ')
    connection.commit() 
    

def add_a_new_competency(comp_name, date):
    query1 = 'INSERT INTO Competencies(name, date_created) VALUES(?,?);'
    cursor.execute(query1, (comp_name, date))
    # input('Press enter to finish adding each submission: ')
    connection.commit()   
    # 1. Get input for comp name
    # 2. Get date
    # 3. Call function


def add_a_new_assessment_to_a_competency():
    pass

def add_an_assessment_result_for_a_user_for_an_assessment():
    pass





def edit_a_users_information():
    items_list = ['First Name','Last Name','Phone Number','Email','Password','User Type (User) or (Manager)']
    changed_items = []
    query1 = 'SELECT * FROM Users;'
    rows = cursor.execute(query1).fetchall()
    print(f'{user_dictionary["user_id"]:10}{user_dictionary["first_name"]:15}{user_dictionary["last_name"]:15}{user_dictionary["phone"]:15}{user_dictionary["email"]:35}{user_dictionary["password"]:20}{user_dictionary["date_created"]:25}{user_dictionary["hire_date"]:25}{user_dictionary["user_type"]:12}{user_dictionary["active"]:15}')
    for row in rows:
        print(f'{row[0]:<10}{row[1]:15}{row[2]:15}{row[3]:15}{row[4]:35}{row[5]:20}{row[6]:25}{row[7]:25}{row[8]:12}{row[9]:<15}')
    user_input1 = input('Type User ID to select a User to Edit:--->')
    for item in items_list:
        user_input2 = input(f'Type a new {item} to edit {item} or press Enter to skip:--->')
        changed_items.append(user_input2)
    query2 = 'SELECT first_name, last_name, phone, email, password, user_type FROM Users WHERE user_id = ?;'
    existing_user = cursor.execute(query2, (user_input1,)).fetchone()
    index = 0
    for new_item in changed_items:
        if new_item == '':
            changed_items[index] = existing_user[index]
            index += 1
        else:
            index += 1
    query3 = 'UPDATE Users SET first_name = ?, last_name = ?, phone = ?, email = ?, password = ?, user_type = ? WHERE user_id = ?;'
    cursor.execute(query3, (changed_items[0],changed_items[1],changed_items[2],changed_items[3],changed_items[4],changed_items[5],user_input1))
    input('Press enter to finish adding each submission: ')
    connection.commit() 
    





def edit_a_competency():
    query1 = 'SELECT * FROM Competencies;'
    rows = cursor.execute(query1).fetchall()
    print(f'{competency_dictionary["competency_id"]:<15}{competency_dictionary["name"]:30}{competency_dictionary["date_created"]:30}{competency_dictionary["active"]:15}\n')
    for row in rows:
        print(f'{row[0]:<15}{row[1]:30}{row[2]:30}{row[3]:<15}')


def edit_an_assessment():
    pass

def edit_an_assessment_result():
    pass





def delete_an_assessment_result():
    pass



connection = sqlite3.connect('dp_My_Competency_DataBase.db')
cursor = connection.cursor()
create_schema()


while True:
    user_input1 = input('    ----- Welcome! -----\n\n    1.) Manager?\n    2.) User?\n    3.) Admin?\n    4.) Exit site\n\n    Type number here:--->')
    if user_input1 == '1':
        while True:
            user_input2 = input('''
    1.) View all users in a list
    2.) Search for users by First or Last name
    3.) View a report of all users and their competency levels for a given competency
    4.) View a competency level report for an individual user
    5.) View a list of assessments for a given user
    6.) Add Options
    7.) Edit Options
    8.) Delete Options
    9.) Logout
                        
    Type number here:--->''')
            if user_input2 == '1':
                view_all_users_in_a_list()
            elif user_input2 == '2':
                search_for_users_by_first_or_last_name()
            elif user_input2 == '3':
                view_a_report_of_all_users_and_their_competency_levels_for_a_given_competency()
            elif user_input2 == '4':
                view_a_competency_level_for_an_individual_user()
            elif user_input2 == '5':
                view_a_list_of_assessments_for_a_given_user()
            elif user_input2 == '6':
                while True:
                    user_input3 = input('''
        1.) Add a user
        2.) Add a new competency
        3.) Add a new assessment to a competency
        4.) Add an assessment result for a user for an assessment
        5.) Back to Menu
        
        Type number here:--->''')
                    if user_input3 == '1':
                        user_item_list = ['First Name:--->','Last Name:--->','Phone Number:--->','Email:--->','Password:--->','User or Manager:--->']
                        big_user_info_list = []
                        while True:
                            little_user_list = []
                            add_stop_input = input('Press enter to Add a Contact (OR) Type (Q) to Quit:--->')
                            if add_stop_input != 'q':
                                for user_item in user_item_list:
                                    user_input = input(f'{user_item}')
                                    little_user_list.append(user_input)
                                    print(little_user_list)
                                big_user_info_list.append(little_user_list)
                                print(big_user_info_list)
                            elif add_stop_input.lower() == 'q':
                                for ind in big_user_info_list:
                                    first_name = ''
                                    last_name = ''
                                    phone = ''
                                    email = ''
                                    password = ''
                                    user_type = ''
                                    variable = 0
                                    for item in ind:
                                        if variable == 0:
                                            first_name += item
                                        elif variable == 1:
                                            last_name += item
                                        elif variable == 2:
                                            phone += item
                                        elif variable == 3:
                                            email += item
                                        elif variable == 4:
                                            password += item
                                        elif variable == 5:
                                            user_type += item
                                        variable += 1

                                    add_a_user(first_name, last_name, phone, email, password, date, user_type)   
                                break
                        


                    elif user_input3 == '2':
                        comp_item_list = ['Name:--->']
                        big_comp_info_list = []
                        while True:
                            little_comp_list = []
                            input1 = input('Press enter to Add a Competency (OR) Type (Q) to Quit:--->')
                            if input1 != 'q':
                                for comp in comp_item_list:
                                    user_input = input(f'{comp}')
                                    little_comp_list.append(user_input)
                                    print(little_comp_list)
                                big_comp_info_list.append(little_comp_list)
                                print(big_comp_info_list)
                            elif input1.lower() == 'q':
                                for ind in big_comp_info_list:
                                    comp_name = ''
                                    variable = 0
                                    for item in ind:
                                        if variable == 0:
                                            comp_name += item

                                    add_a_new_competency(comp_name,date) 
                                break

  
                    elif user_input3 == '3':
                        add_a_new_assessment_to_a_competency()
                    elif user_input3 == '4':
                        add_an_assessment_result_for_a_user_for_an_assessment()
                    elif user_input3 == '5':
                        break


            elif user_input2 == '7':
                while True:
                    user_input4 = input('''
        1.) Edit a users information
        2.) Edit a competency
        3.) Edit an assessment
        4.) Edit an assessment result
        5.) Back to Menu
        
        Type number here:--->''')
                    if user_input4 == '1':
                        edit_a_users_information()
                    elif user_input4 == '2':
                        edit_a_competency()
                    elif user_input4 == '3':
                        edit_an_assessment()
                    elif user_input4 == '4':
                        edit_an_assessment_result()
                    elif user_input4 == '5':
                        break
            elif user_input2 == '8':
                while True:
                    user_input5 = input('''
        1.) Delete an assessment result
        2.) Back to Menu
        
        Type number here:--->''')
                    if user_input5 == '1':
                        delete_an_assessment_result()
                    elif user_input5 == '2':
                        break
            elif user_input2 == '9':
                break

            
    elif user_input1 == '2':
        pass
    elif user_input1 == '3':
        while True:
            admin_input = input('1.) Restore Competencies\n2.)\n3.)\nType here:--->')
            if admin_input == '1':
                create_schema_2()

    elif user_input1 == '4':
        break








