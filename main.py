import sqlite3
import csv
from datetime import datetime
import bcrypt

new_date = datetime.now()
date = new_date.replace(microsecond = 0)

user_dictionary = {'user_id':'User ID','first_name':'First Name','last_name':'Last Name','phone':'Phone Number','email':'Email','password':'Password','date_created':'Date Created','hire_date':'Hire Date','user_type':'User Type','active':'Active'}
competency_dictionary = {'competency_id':'Competency ID','name':'Name','date_created':'Date Created','active':'Active'}
assessment_dictionary = {'assessment_id':'Assessment ID','competency_id':'Competency ID','name':'Name','active':'Active'}
assessment_result_dictionary = {'assessment_result_id':'Assessment Result ID','user_id':'User ID','assessment_id':'Assessment ID','score':'Score','date_taken':'Date Taken','manager':'Manager'}
def create_schema():
    with open('schema.sql','rt') as my_schema:
        queries = my_schema.read()
        cursor.executescript(queries)

def create_schema_2():
    with open('seed_data.sql','rt') as my_schema:
        queries = my_schema.read()
        cursor.executescript(queries)
        connection.commit()
        return 'Restoration Complete\n'
    
def create_schema_3():
    with open('seed_data_2.csv','rt') as my_schema:
        read_my_schema = csv.reader(my_schema)
        for row in read_my_schema: 
            hashed_password = hash_pw(row[4])    
            queries = 'INSERT INTO Users(first_name, last_name, phone, email, password, date_created, hire_date, user_type) VALUES(?,?,?,?,?,?,?,?);'
            cursor.execute(queries,(row[0],row[1],row[2],row[3],hashed_password,row[5],row[6],row[7]))
            connection.commit()
        return 'Restoration Complete\n'
    
def create_schema_4():
    with open('seed_data_3.csv','rt') as my_schema:
        read_my_schema = csv.reader(my_schema)
        for row in read_my_schema:     
            queries = 'INSERT INTO Assessments(competency_id, name) VALUES(?,?);'
            cursor.execute(queries,(row[0],row[1]))
            connection.commit()
        return 'Restoration Complete\n'
    
def create_schema_5():
    with open('seed_data_4.csv','rt') as my_schema:
        read_my_schema = csv.reader(my_schema)
        for row in read_my_schema:     
            queries = 'INSERT INTO Assessment_Results(user_id, assessment_id, score, date_taken, manager) VALUES(?,?,?,?,?);'
            cursor.execute(queries,(row[0],row[1],row[2],date,row[3]))
            connection.commit()
        return 'Restoration Complete\n'

def read_only_users():
    query = 'SELECT * FROM Users WHERE active = 1 AND user_type = "User";'
    rows = cursor.execute(query).fetchall()
    print(f'{user_dictionary["user_id"]:10}{user_dictionary["first_name"]:15}{user_dictionary["last_name"]:15}{user_dictionary["phone"]:15}{user_dictionary["email"]:35}{user_dictionary["password"]:20}{user_dictionary["date_created"]:25}{user_dictionary["hire_date"]:25}{user_dictionary["user_type"]:12}{user_dictionary["active"]:15}')
    for row in rows:
        print(f'{row[0]:<10}{row[1]:15}{row[2]:15}{row[3]:15}{row[4]:35}{row[5]:20}{row[6]:25}{row[7]:25}{row[8]:12}{row[9]:<15}')
        print()

def read_only_managers():
    query = 'SELECT * FROM Users WHERE active = 1 AND user_type = "Manager";'
    rows = cursor.execute(query).fetchall()
    print(f'{user_dictionary["user_id"]:10}{user_dictionary["first_name"]:15}{user_dictionary["last_name"]:15}{user_dictionary["phone"]:15}{user_dictionary["email"]:35}{user_dictionary["password"]:20}{user_dictionary["date_created"]:25}{user_dictionary["hire_date"]:25}{user_dictionary["user_type"]:12}{user_dictionary["active"]:15}')
    for row in rows:
        print(f'{row[0]:<10}{row[1]:15}{row[2]:15}{row[3]:15}{row[4]:35}{row[5]:20}{row[6]:25}{row[7]:25}{row[8]:12}{row[9]:<15}')
        print()

def read_all_assessments():
    query = 'SELECT * FROM Assessments WHERE active = 1;'
    rows = cursor.execute(query).fetchall()
    print(f'{assessment_dictionary["assessment_id"]:<15}{assessment_dictionary["competency_id"]:15}{assessment_dictionary["name"]:30}{assessment_dictionary["active"]:<15}')
    for row in rows:
        print(f'{row[0]:<15}{row[1]:<15}{row[2]:30}{row[3]:<15}')

def read_assessment_results():
    query = 'SELECT * FROM Assessment_Results;'
    rows = cursor.execute(query).fetchall()
    print(f'{assessment_result_dictionary["assessment_result_id"]:<25}{assessment_result_dictionary["user_id"]:<15}{assessment_result_dictionary["assessment_id"]:<15}{assessment_result_dictionary["score"]:<15}{assessment_result_dictionary["date_taken"]:30}{assessment_result_dictionary["manager"]:<15}')
    for row in rows:
        print(f'{row[0]:<25}{row[1]:<15}{row[2]:<15}{row[3]:<15}{row[4]:30}{row[5]:<15}')

# def record_assessment_results():
#     query = 'INSERT INTO Assessment_Results(user_id, assessment_id, score, date_taken, manager) VALUES(?,?,?,?,?);'
#     cursor.execute(query, (user_id, assessment_id, assessment_score, date, manager_id))
#     connection.commit()





def hash_pw(pt_pass):
    salt = bcrypt.gensalt()
    encoded_pass = pt_pass.encode()
    hashed_pass = bcrypt.hashpw(encoded_pass,salt)
    return hashed_pass

def check_pw(pt_pass, hashed_pw):
    encoded_pass = pt_pass.encode()
    return bcrypt.checkpw(encoded_pass, hashed_pw)















def view_all_users_in_a_list():
    query1 = 'SELECT * FROM Users WHERE active = 1;'
    rows = cursor.execute(query1).fetchall()
    print(f'{user_dictionary["user_id"]:10}{user_dictionary["first_name"]:15}{user_dictionary["last_name"]:15}{user_dictionary["phone"]:15}{user_dictionary["email"]:35}{user_dictionary["password"]:20}{user_dictionary["date_created"]:25}{user_dictionary["hire_date"]:25}{user_dictionary["user_type"]:12}{user_dictionary["active"]:15}')
    for row in rows:
        print(f'{row[0]:<10}{row[1]:15}{row[2]:15}{row[3]:15}{row[4]:35}{row[5]:20}{row[6]:25}{row[7]:25}{row[8]:12}{row[9]:<15}')
        print()

def search_for_users_by_first_or_last_name(first_name, last_name):
    query1 = 'SELECT * FROM Users WHERE first_name LIKE ? AND last_name LIKE ? AND active = 1;'
    rows = cursor.execute(query1, (first_name, last_name)).fetchall()
    print(f'{user_dictionary["user_id"]:10}{user_dictionary["first_name"]:15}{user_dictionary["last_name"]:15}{user_dictionary["phone"]:15}{user_dictionary["email"]:35}{user_dictionary["password"]:20}{user_dictionary["date_created"]:25}{user_dictionary["hire_date"]:25}{user_dictionary["user_type"]:12}{user_dictionary["active"]:15}')
    for row in rows:
        print(f'{row[0]:<10}{row[1]:15}{row[2]:15}{row[3]:15}{row[4]:35}{row[5]:20}{row[6]:25}{row[7]:25}{row[8]:12}{row[9]:<15}')
        print()

def view_a_report_of_all_users_and_their_competency_levels_for_a_given_competency(assessment_id): # for everyone


    query = """
    SELECT assessment_result_id, user_id, Assessment_Results.assessment_id, score, date_taken, manager, competency_id 
    FROM Assessment_Results, Assessments
    WHERE Assessment_Results.assessment_id = Assessments.assessment_id
    AND Assessment_Results.assessment_id = ? 
    GROUP BY user_id
    ORDER BY user_id, MAX(date_taken) DESC;
    """
# 
    # query = 'SELECT * FROM Assessment_Results WHERE assessment_id = ? ORDER BY user_id, date_taken DESC;'
    rows = cursor.execute(query, (assessment_id,))
    scores_list = []
    # score_dict = {}
    user_id = '0'


    #print(f'{assessment_result_dictionary["assessment_result_id"]:<25}{assessment_result_dictionary["user_id"]:<15}{assessment_result_dictionary["assessment_id"]:<15}{assessment_result_dictionary["score"]:<15}{assessment_result_dictionary["date_taken"]:30}{assessment_result_dictionary["manager"]:<15}')
    for row in rows:
        #print(f'{row[0]:<25}{row[1]:<15}{row[2]:<15}{row[3]:<15}{row[4]:30}{row[5]:<15}')
        #if user_id != row[1]:
            # my_list.append(row[1])
            # my_dictionary[row[1]] = row[3]
        scores_list.append({"user_id":row[1], "comp_id": row[6], "score": row[3]})
        #user_id = row[1]

    with open('competencies.csv','wt') as my_csv:
        wrt = csv.writer(my_csv)
        wrt.writerow(['user_id','comp_id','score'])
        for score_dict in scores_list:
            #print(score_dict)
            if int(score_dict["score"]) <= 20:
                comp_level = 0

            elif int(score_dict["score"]) <= 40:
                comp_level = 1

            elif int(score_dict["score"]) <= 60:
                comp_level = 2

            elif int(score_dict["score"]) <= 80:
                comp_level = 3

            elif int(score_dict["score"]) <= 100:
                comp_level = 4
              
            wrt.writerow([score_dict["user_id"],score_dict["comp_id"], comp_level])
    list1 = []
    with open('competencies.csv','r') as my_csv:
        headers = ['User ID', 'Competency ID', 'Competency Level']
        csvreader = csv.reader(my_csv)
        fields = next(csvreader)
        for row in csvreader:
            list1.append(row)
        print(f'{headers[0]:25}{headers[1]:25}{headers[2]:25}')
        for list in list1:
            print(f'{list[0]:<25}{list[1]:<25}{list[2]:<25}')

def view_a_competency_level_for_an_individual_user(user_id, assessment_id): #for a specific person
    query = """
    SELECT assessment_result_id, user_id, Assessment_Results.assessment_id, score, date_taken, manager, competency_id 
    FROM Assessment_Results, Assessments
    WHERE Assessment_Results.assessment_id = Assessments.assessment_id
    AND Assessment_Results.assessment_id = ? AND user_id = ?
    GROUP BY user_id
    ORDER BY user_id, MAX(date_taken) DESC;
    """

    rows = cursor.execute(query, (assessment_id, user_id))
    scores_list = []
    for row in rows:
        scores_list.append({"user_id":row[1], "comp_id": row[6], "score": row[3]})

    with open('competencies.csv','wt') as my_csv:
        wrt = csv.writer(my_csv)
        wrt.writerow(['user_id','comp_id','score'])
        for score_dict in scores_list:
            #print(score_dict)
            if int(score_dict["score"]) <= 20:
                comp_level = 0

            elif int(score_dict["score"]) <= 40:
                comp_level = 1

            elif int(score_dict["score"]) <= 60:
                comp_level = 2

            elif int(score_dict["score"]) <= 80:
                comp_level = 3

            elif int(score_dict["score"]) <= 100:
                comp_level = 4
              
            wrt.writerow([score_dict["user_id"],score_dict["comp_id"], comp_level])
    list1 = []
    with open('competencies.csv','r') as my_csv:
        headers = ['User ID', 'Competency ID', 'Competency Level']
        csvreader = csv.reader(my_csv)
        fields = next(csvreader)
        for row in csvreader:
            list1.append(row)
        print(f'{headers[0]:25}{headers[1]:25}{headers[2]:25}')
        for list in list1:
            print(f'{list[0]:<25}{list[1]:<25}{list[2]:<25}')


def view_a_list_of_assessments_for_a_given_user(user_id): # tests taken by a specific person
    query = 'SELECT * FROM Assessment_Results WHERE user_id = ?;'
    rows = cursor.execute(query, (user_id,)).fetchall()
    print(f'{assessment_result_dictionary["assessment_result_id"]:<25}{assessment_result_dictionary["user_id"]:<15}{assessment_result_dictionary["assessment_id"]:<15}{assessment_result_dictionary["score"]:<15}{assessment_result_dictionary["date_taken"]:30}{assessment_result_dictionary["manager"]:<15}')
    for row in rows:
        print(f'{row[0]:<25}{row[1]:<15}{row[2]:<15}{row[3]:<15}{row[4]:30}{row[5]:<15}')





def add_a_user(first_name, last_name, phone, email, password, date, user_type):
    hashed_password = hash_pw(password)
    query1 = 'INSERT INTO Users(first_name, last_name, phone, email, password, date_created, hire_date, user_type) VALUES(?,?,?,?,?,?,?,?);'
    cursor.execute(query1, (first_name, last_name, phone, email, hashed_password, date, date, user_type))
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


def add_a_new_assessment_to_a_competency(comp_id, name):
    query = 'INSERT INTO Assessments(competency_id, name) VALUES(?,?);'
    cursor.execute(query, (comp_id, name))
    connection.commit() 

    

def add_an_assessment_result_for_a_user_for_an_assessment(user_id, assessment_id, assessment_score, date, manager_id):
    query = 'INSERT INTO Assessment_Results(user_id, assessment_id, score, date_taken, manager) VALUES(?,?,?,?,?);'
    cursor.execute(query, (user_id, assessment_id, assessment_score, date, manager_id))
    connection.commit()





def edit_a_users_information(changed_items,user_input1):
    hashed_password = hash_pw(changed_items[4])
    query3 = 'UPDATE Users SET first_name = ?, last_name = ?, phone = ?, email = ?, password = ?, user_type = ? WHERE user_id = ? AND active = 1;'
    cursor.execute(query3, (changed_items[0],changed_items[1],changed_items[2],changed_items[3],hashed_password,changed_items[5],user_input1))
    #input('Press enter to finish adding submission: ')
    connection.commit() 
    
def edit_a_competency(changed_comp_items,comp_id_input):
    query = 'UPDATE Competencies SET name = ? WHERE competency_id = ? AND active = 1;'
    cursor.execute(query,(changed_comp_items[0],comp_id_input))
    #input('Press enter to finish adding submission: ')
    connection.commit()

def edit_an_assessment(assessment_id, name):
    query = 'UPDATE Assessments SET competency_id = ?, name = ? WHERE assessment_id = ? AND active = 1;'
    cursor.execute(query, (assessment_id, name))
    connection.commit()

def edit_an_assessment_result(user_id, assessment_id, assessment_score, manager_id, assessment_result_id):
    query = 'UPDATE Assessment_Results SET user_id = ?, assessment_id = ?, score = ?, manager = ? WHERE assessment_result_id = ?;'
    cursor.execute(query, (user_id, assessment_id, assessment_score, manager_id, assessment_result_id))
    connection.commit()




def deactivate_an_assessment_result():
    pass

def deactivate_a_user(user_id):
    query = 'UPDATE Users SET active = 0 WHERE user_id = ?;'
    cursor.execute(query, (user_id,))
    #input('Press enter to confirm you want to Delete: ')
    connection.commit()

def deactivate_a_competency(comp_id):
    query = 'UPDATE Competencies SET active = 0 WHERE competency_id = ?;'
    cursor.execute(query, (comp_id,))
    #input('Press enter to confirm you want to Delete: ')
    connection.commit()

def deactivate_an_assessment(assessment_id):
    query = 'UPDATE Assessments SET active = 0 WHERE assessment_id = ?;'
    cursor.execute(query, (assessment_id,))
    connection.commit()

def activate_an_assessment_result():
    pass

def activate_a_user(user_id):
    query = 'UPDATE Users SET active = 1 WHERE user_id = ?;'
    cursor.execute(query, (user_id,))
    #input('Press enter to confirm you want to UnDelete: ')
    connection.commit()

def activate_a_competency(comp_id):
    query = 'UPDATE Competencies SET active = 1 WHERE competency_id = ?;'
    cursor.execute(query, (comp_id,))
    #input('Press enter to confirm you want to UnDelete: ')
    connection.commit()

def activate_an_assessment(assessment_id):
    query = 'UPDATE Assessments SET active = 1 WHERE assessment_id = ?;'
    cursor.execute(query, (assessment_id,))
    connection.commit()




def view_my_info(user_id):
    query = 'SELECT * FROM Users WHERE user_id = ?;'
    rows = cursor.execute(query, (user_id)).fetchall()
    print(f'{user_dictionary["user_id"]:10}{user_dictionary["first_name"]:15}{user_dictionary["last_name"]:15}{user_dictionary["phone"]:15}{user_dictionary["email"]:35}{user_dictionary["password"]:20}{user_dictionary["date_created"]:25}{user_dictionary["hire_date"]:25}{user_dictionary["user_type"]:12}{user_dictionary["active"]:15}')
    for row in rows:
        print(f'{row[0]:<10}{row[1]:15}{row[2]:15}{row[3]:15}{row[4]:35}{row[5]:20}{row[6]:25}{row[7]:25}{row[8]:12}{row[9]:<15}')

def edit_user_name(user_id, first_name, last_name):
    query = 'UPDATE Users SET first_name = ?, last_name = ? WHERE user_id = ?;' 
    cursor.execute(query, (first_name, last_name, user_id))
    connection.commit() 

def edit_user_password(user_id, new_password):
    hashed_password = hash_pw(new_password)
    query = 'UPDATE Users SET password = ? WHERE user_id = ?;'
    cursor.execute(query, (hashed_password, user_id))
    connection.commit()

def view_competencies():
    query = 'SELECT * FROM Competencies WHERE active = 1;'
    rows = cursor.execute(query).fetchall()
    print(f'{competency_dictionary["competency_id"]:<15}{competency_dictionary["name"]:30}{competency_dictionary["date_created"]:30}{competency_dictionary["active"]:15}\n')
    for row in rows:
        print(f'{row[0]:<15}{row[1]:30}{row[2]:30}{row[3]:<15}')


connection = sqlite3.connect('dp_My_Competency_DataBase.db')
cursor = connection.cursor()
create_schema()


while True:
    user_input1 = input('    ----- Welcome! -----\n\n    1.) Manager?\n    2.) User?\n    3.) Exit site\n\n    Type number here:--->')
    if user_input1 == '1':
        email = input('Your Email:--->')
        password = input('Your Password:--->')
        user_query = 'SELECT password, user_type, user_id FROM Users WHERE email = ?;'
        row = cursor.execute(user_query, (email,)).fetchone()
        # for row in rows:
        #     query = "SELECT password FROM Users WHERE user_id = ?"
        user_id = str(row[2])
        # result = cursor.execute(query, (user_id,)).fetchone()
        check_password = check_pw(password, row[0])
        if row[1] == 'Manager' and check_password == True:
            while True:
                user_input2 = input('''
    1.) View all users in a list
    2.) Search for users by First or Last name
    3.) View a report of all users and their competency levels for a given competency
    4.) View a competency level report for an individual user
    5.) View a list of assessments for a given user
    6.) Add Options
    7.) Edit Options
    8.) Activate or Deactivate Options
    9.) Dumby Data
    10.) Logout
                        
    Type number here:--->''')
                if user_input2 == '1':
                    view_all_users_in_a_list()

                elif user_input2 == '2':
                    first_name = input("Type Person's First Name:---> ")
                    last_name = input("Type Person's Last Name:---> ")
                    search_for_users_by_first_or_last_name(first_name, last_name)

                elif user_input2 == '3':
                    read_all_assessments()
                    assessment_id = input('Type the Assessment ID to choose Assessment:--->')
                    view_a_report_of_all_users_and_their_competency_levels_for_a_given_competency(assessment_id)

                elif user_input2 == '4':
                    read_only_users()
                    user_id = input('Type User ID to choose User:--->')
                    read_all_assessments()
                    assessment_id = input('Type the Assessment ID to choose Assessment:--->')
                    view_a_competency_level_for_an_individual_user(user_id, assessment_id)

                elif user_input2 == '5':
                    read_only_users()
                    user_id = input('Type User ID to choose User:--->')
                    view_a_list_of_assessments_for_a_given_user(user_id)

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
                            user_item_list = ['First Name:--->','Last Name:--->','Phone Number:--->','Email:--->','Password:--->']
                            big_user_info_list = []
                            while True:
                                little_user_list = []
                                add_stop_input = input('Press enter to Add a User (OR) Type (Q) to Quit:--->')
                                if add_stop_input != 'q':
                                    for user_item in user_item_list:
                                        user_input = input(f'{user_item}')
                                        little_user_list.append(user_input)
                                        print(little_user_list)
                                    select_user_type = input('''
    1.) Manager
    2.) User
    
    Type Here:--->''')
                                    if select_user_type == '1': 
                                        little_user_list.append('Manager')
                                    elif select_user_type == '2':
                                        little_user_list.append('User')
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
                                        print(ind)
                                        
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
                                        #print(little_comp_list)
                                    big_comp_info_list.append(little_comp_list)
                                    #print(big_comp_info_list)
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
                            name1 = 'Formative Assessment'
                            name2 = 'Summative Assessment'
                            name3 = 'Diagnostic Assessment'
                            query = 'SELECT * FROM Competencies WHERE active = 1;'
                            rows = cursor.execute(query1).fetchall()
                            print(f'{competency_dictionary["competency_id"]:<15}{competency_dictionary["name"]:30}{competency_dictionary["date_created"]:30}{competency_dictionary["active"]:15}\n')
                            for row in rows:
                                print(f'{row[0]:<15}{row[1]:30}{row[2]:30}{row[3]:<15}')
                            comp_id = input('Type a Competency ID to select Competency for the Assessment:--->')
                            assessment_type = input('''
    1.) Formative Assessment
    2.) Summative Assessment
    3.) Diagnostic Assessment
    4.) Other
    
    Type Here:--->''')
                            if assessment_type == '1':
                                add_a_new_assessment_to_a_competency(comp_id, name1)
                            elif assessment_type == '2':
                                add_a_new_assessment_to_a_competency(comp_id, name2)
                            elif assessment_type == '3':
                                add_a_new_assessment_to_a_competency(comp_id, name3)
                            elif assessment_type == '4':
                                name4 = input('Type your Assessment Type here:---> ')
                                add_a_new_assessment_to_a_competency(comp_id, name4)


                        elif user_input3 == '4':
                            read_only_users()
                            user_id = input('Type User ID to choose User:--->')
                            read_only_managers()
                            manager_id = input('Type User ID to choose Manager:--->')
                            read_all_assessments()
                            assessment_id = input('Type Assessment ID to choose Assessment:--->')
                            assessment_score = input('Type User\'s Assessment Score Here:--->')


                            add_an_assessment_result_for_a_user_for_an_assessment(user_id, assessment_id, assessment_score, date, manager_id)
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
                            changed_items = []
                            items_list = ['First Name','Last Name','Phone Number','Email','Password','User Type (User) or (Manager)']
                            view_all_users_in_a_list()
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
                            edit_a_users_information(changed_items,user_input1)

                        elif user_input4 == '2':
                            query1 = 'SELECT * FROM Competencies WHERE active = 1;'
                            rows = cursor.execute(query1).fetchall()
                            print(f'{competency_dictionary["competency_id"]:<15}{competency_dictionary["name"]:30}{competency_dictionary["date_created"]:30}{competency_dictionary["active"]:15}\n')
                            for row in rows:
                                print(f'{row[0]:<15}{row[1]:30}{row[2]:30}{row[3]:<15}')
                            comp_item_list = ['Name Competency:--->']
                            comp_id_input = input('Type the Competency ID here to choose Competency:--->')
                            changed_comp_items = []
                            for comp_item in comp_item_list:
                                new_comp_input = input(f'{comp_item}')
                                changed_comp_items.append(new_comp_input)
                            query2 = 'SELECT * FROM Competencies WHERE competency_id = ? AND active = 1;'
                            existing_comp = cursor.execute(query2, (comp_id_input,)).fetchone()
                            index = 0
                            for new_comp_item in changed_comp_items:
                                if new_comp_item == '':
                                    changed_comp_items[index] = existing_comp[index]
                                    index += 1
                                else:
                                    index += 1
                            edit_a_competency(changed_comp_items,comp_id_input)

                        elif user_input4 == '3':
                            name1 = 'Formative Assessment'
                            name2 = 'Summative Assessment'
                            name3 = 'Diagnostic Assessment'
                            query = 'SELECT * FROM Assessments WHERE active = 1;'
                            assessment_type = input('''
    1.) Formative Assessment
    2.) Summative Assessment
    3.) Diagnostic Assessment
    4.) Other
    
    Type Here:--->''')
                            if assessment_type == '1':
                                comp_id = input('Type a Competency ID to change Competency for the Assessment:--->')
                                edit_an_assessment(comp_id, name1)
                            elif assessment_type == '2':
                                comp_id = input('Type a Competency ID to change Competency for the Assessment:--->')
                                edit_an_assessment(comp_id, name2)
                            elif assessment_type == '3':
                                comp_id = input('Type a Competency ID to change Competency for the Assessment:--->')
                                edit_an_assessment(comp_id, name3)
                            elif assessment_type == '4':
                                comp_id = input('Type a Competency ID to change Competency for the Assessment:--->')
                                name4 = input('Type your Assessment Type here:---> ')
                                edit_an_assessment(comp_id, name4)

                        elif user_input4 == '4':
                            read_assessment_results()
                            assessment_result_id = input('Type Assessment Result ID to choose Assessment Result to change:--->')
                            read_only_users()
                            user_id = input('Type User ID to choose User:--->')
                            read_only_managers()
                            manager_id = input('Type User ID to choose Manager:--->')
                            read_all_assessments()
                            assessment_id = input('Type Assessment ID to choose Assessment:--->')
                            assessment_score = input('Type User\'s Assessment Score Here:--->')

                            edit_an_assessment_result(user_id, assessment_id, assessment_score, manager_id, assessment_result_id)
                        elif user_input4 == '5':
                            break
                elif user_input2 == '8':
                    while True:
                        user_input5 = input('''
    1.) Deactivate an Assessment result
    2.) Activate an Assessment result
    3.) Deactivate a User
    4.) Activate a User
    5.) Deactivate a Competency
    6.) Activate a Competency
    7.) Deactivate an Assessment
    8.) Activate an Assessment
    9.) Back to Menu
    
    Type number here:--->''')
                        if user_input5 == '1':
                            deactivate_an_assessment_result()
                        elif user_input5 == '2':
                            activate_an_assessment_result()

                        elif user_input5 == '3':
                            view_all_users_in_a_list()
                            user_id = input('Type User ID to select Person to Deactivate:--->')
                            deactivate_a_user(user_id)
                        elif user_input5 == '4':
                            query1 = 'SELECT * FROM Users WHERE active = 0;'
                            rows = cursor.execute(query1).fetchall()
                            print(f'{user_dictionary["user_id"]:10}{user_dictionary["first_name"]:15}{user_dictionary["last_name"]:15}{user_dictionary["phone"]:15}{user_dictionary["email"]:35}{user_dictionary["password"]:20}{user_dictionary["date_created"]:25}{user_dictionary["hire_date"]:25}{user_dictionary["user_type"]:12}{user_dictionary["active"]:15}')
                            for row in rows:
                                print(f'{row[0]:<10}{row[1]:15}{row[2]:15}{row[3]:15}{row[4]:35}{row[5]:20}{row[6]:25}{row[7]:25}{row[8]:12}{row[9]:<15}')
                                print()
                            user_id = input('Type User ID to select Person to Activate:--->')
                            activate_a_user(user_id)

                        elif user_input5 == '5':
                            query1 = 'SELECT * FROM Competencies WHERE active = 1;'
                            rows = cursor.execute(query1).fetchall()
                            print(f'{competency_dictionary["competency_id"]:<15}{competency_dictionary["name"]:30}{competency_dictionary["date_created"]:30}{competency_dictionary["active"]:15}\n')
                            for row in rows:
                                print(f'{row[0]:<15}{row[1]:30}{row[2]:30}{row[3]:<15}')
                            comp_id = input('Type Copmetency ID to select Competency to Deactivate:--->')
                            deactivate_a_competency(comp_id)
                        elif user_input5 == '6':
                            query1 = 'SELECT * FROM Competencies WHERE active = 0;'
                            rows = cursor.execute(query1).fetchall()
                            print(f'{competency_dictionary["competency_id"]:<15}{competency_dictionary["name"]:30}{competency_dictionary["date_created"]:30}{competency_dictionary["active"]:15}\n')
                            for row in rows:
                                print(f'{row[0]:<15}{row[1]:30}{row[2]:30}{row[3]:<15}')
                            comp_id = input('Type Copmetency ID to select Competency to Activate:--->')
                            activate_a_competency(comp_id)

                        elif user_input5 == '7':
                            query = 'SELECT * FROM Assessments WHERE active = 1;'
                            rows = cursor.execute(query).fetchall()
                            print(f'{assessment_dictionary["assessment_id"]:<15}{assessment_dictionary["competency_id"]:15}{assessment_dictionary["name"]:30}{assessment_dictionary["active"]:<15}')
                            for row in rows:
                                print(f'{row[0]:<15}{row[1]:<15}{row[2]:30}{row[3]:<15}')
                            assessment_id = input('Type an Assessment ID to select Assessment to Deactivate:--->')
                            deactivate_an_assessment(assessment_id)

                        elif user_input5 == '8':
                            query = 'SELECT * FROM Assessments WHERE active = 0;'
                            rows = cursor.execute(query).fetchall()
                            print(f'{assessment_dictionary["assessment_id"]:<15}{assessment_dictionary["competency_id"]:15}{assessment_dictionary["name"]:30}{assessment_dictionary["active"]:<15}')
                            for row in rows:
                                print(f'{row[0]:<15}{row[1]:<15}{row[2]:30}{row[3]:<15}')
                            assessment_id = input('Type an Assessment ID to select Assessment to Deactivate:--->')
                            activate_an_assessment(assessment_id)
                            
                        elif user_input5 == '9':
                            break
                elif user_input2 == '9':
                    while True:
                        admin_input = input('1.) Restore Competencies\n2.) Restore Users\n3.) Restore Assessments\n4.) Restore Assessment Results\n5.) Return to Main Menu\nType here:--->')
                        if admin_input == '1':
                            print(create_schema_2())
                        elif admin_input == '2':
                            print(create_schema_3())
                        elif admin_input == '3':
                            print(create_schema_4())
                        elif admin_input == '4':
                            print(create_schema_5())
                        elif admin_input == '5':
                            break
                elif user_input2 == '10':
                    break

            
    elif user_input1 == '2':
        email = input('Your Email:--->')
        password = input('Your Password:--->')
        user_query = 'SELECT password, user_type, user_id FROM Users WHERE email = ?;'
        row = cursor.execute(user_query, (email,)).fetchone()
        # for row in rows:
        #     query = "SELECT password FROM Users WHERE user_id = ?"
        user_id = str(row[2])
        # result = cursor.execute(query, (user_id,)).fetchone()
        check_password = check_pw(password, row[0])
        if row[1] == 'User' and check_password == True:
            while True:
                user_menu = input('''
    1.) View Options
    2.) Edit Options
    3.) Back to Main Menu
    
    Type Here:--->''')
                if user_menu == '1':
                    while True:
                        view_options = input('''
    1.) Assessments
    2.) Competencies
    3.) Competency Level
    4.) My Info
    5.) Back to last Menu

    Type Here:--->''')
                        if view_options == '1':
                            read_all_assessments()
                        elif view_options == '2':
                            view_competencies()
                        elif view_options == '3':
                            read_all_assessments()
                            assessment_id = input('Type the Assessment ID to choose Assessment:--->')
                            view_a_competency_level_for_an_individual_user(user_id, assessment_id)
                        elif view_options == '4':
                            view_my_info(user_id)
                        elif view_options == '5':
                            break
                elif user_menu == '2':
                
                    edit_options = input('''
    1.) Change Name
    2.) Change Password
    3.) Go Back

    Type Here:--->''')
                    if edit_options == '1':
                        first_name = input('Type First Name or Press Enter to skip:--->')
                        last_name = input('Type Last Name or Press Enter to skip:--->')
                        query = 'SELECT * FROM Users WHERE user_id = ?;'
                        rows = cursor.execute(query, (user_id)).fetchall()
                        for row in rows:
                            if first_name == '':
                                first_name = row[1]
                            if last_name == '':
                                last_name = row[2]
                        edit_user_name(user_id, first_name, last_name)

                    elif edit_options == '2':
                        new_password = input('Type new Password Here:--->')
                        edit_user_password(user_id, new_password)

                    elif edit_options == '3':
                        print()

                elif user_menu == '3':
                    break
        else:
            print('Invalid Input! Try again')

    elif user_input1 == '3':
        break








