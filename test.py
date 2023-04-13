import sqlite3
import bcrypt

connection = sqlite3.connect('dp_My_Competency_DataBase.db')
cursor = connection.cursor()

def hash_pw(pt_pass):
    salt = bcrypt.gensalt()
    encoded_pass = pt_pass.encode()
    hashed_pass = bcrypt.hashpw(encoded_pass,salt)
    return hashed_pass

def check_pw(pt_pass, hashed_pw):
    encoded_pass = pt_pass.encode()
    return bcrypt.checkpw(encoded_pass, hashed_pw)


# query = "UPDATE Users SET password = ? WHERE user_id = ?"

# new_password = input("New Password: ")

# hashed_pw = hash_pw(new_password)

# cursor.execute(query,(hashed_pw, user_id))
# connection.commit()

query = "SELECT password FROM Users WHERE user_id = ?"
user_id = input('Which user ID to check password for? ')

result = cursor.execute(query, (user_id,)).fetchone()

password = input("Password: ")

print(check_pw(password, result[0]))
