import sqlite3 as sql

#Creating and connecting login database
login = sql.connect('password.sqlite')
login_cr = login.cursor()
login_cr.execute('CREATE TABLE IF NOT EXISTS login (Nickname, Password)')

def add_login(nickname, password):

    value = [nickname, password]
    login_cr.execute("INSERT INTO login VALUES (?,?)", value)
    login.commit()

def find_user_info():

    login_cr.execute('SELECT * FROM login')
    password = login_cr.fetchone()

    return password

def delete_login():

    login_cr.execute("DELETE FROM login")
    login.commit()



#Creating and connecting passwords database
pas = sql.connect('passwords.sqlite')
pas_cr = pas.cursor()
pas_cr.execute('CREATE TABLE IF NOT EXISTS passwords (Name, Password, Note)')


def add_pass(name, password, note):

    value = [name, password, note]
    pas_cr.execute("INSERT INTO passwords VALUES (?,?,?)", value)
    pas.commit()

def read_all_pass():

    pas_cr.execute('SELECT * FROM passwords')
    values = pas_cr.fetchall()

    return values

def delete(value):

    pas_cr.execute("DELETE FROM passwords WHERE Name = ? and Password ? and Note ?", value)
    pas.commit()

def delete_all_pass():
    
    pas_cr.execute("DELETE FROM passwords")
    pas.commit()




