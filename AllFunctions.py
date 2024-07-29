import sqlite3

conn = sqlite3.connect('demo.db')
c = conn.cursor()
'''
c.execute("""CREATE TABLE user(
            PlayerID integer PRIMARY KEY AUTOINCREMENT,
            Fname text,
            Lname text,
            username text not null unique,
            password text not null,
            snake integer,
            asteroid integer,
            dodgeblock integer)
            """)

c.execute("INSERT INTO user VALUES (1132200001,'Ketaki','Narkhede','KetsN','1234abcd',0,0,0)")
'''
conn.commit()
conn.close()

def regUser(fname, lname, uname, pwd):
    conn = sqlite3.connect('demo.db')
    c = conn.cursor()

    c.execute("INSERT INTO user (Fname,Lname,username,password,snake,asteroid,dodgeblock) VALUES (:Fname,:Lname,:username,:password,0,0,0)",
              {
                  'Fname': fname,
                  'Lname': lname,
                  'username':uname,
                  'password':pwd
              })

    conn.commit()
    conn.close()

def fetchUser(playid):
    conn = sqlite3.connect('demo.db')
    c = conn.cursor()

    c.execute("Select PlayerID, Fname,Lname,username,password from user where PlayerID=:playerid",
              {
                  'playerid':playid
              })
    user = c.fetchall()
    conn.commit()
    conn.close()
    return user

def fetchscores(playid):
    conn = sqlite3.connect('demo.db')
    c = conn.cursor()

    c.execute("Select snake,asteroid,dodgeblock from user where PlayerID=:playerid",
              {
                  'playerid':playid
              })
    score = c.fetchall()
    conn.commit()
    conn.close()
    return score

def updatesnake(playid,score):
    conn = sqlite3.connect('demo.db')
    c = conn.cursor()

    c.execute("update user set snake=:score where PlayerID=:playerid",
              {
                  'score':score,
                  'playerid': playid
              })
    conn.commit()
    conn.close()

def updateasteroid(playid,score):
    conn = sqlite3.connect('demo.db')
    c = conn.cursor()

    c.execute("update user set asteroid=:score where PlayerID=:playerid",
              {
                  'score':score,
                  'playerid': playid
              })
    conn.commit()
    conn.close()

def updatedodge(playid,score):
    conn = sqlite3.connect('demo.db')
    c = conn.cursor()

    c.execute("update user set dodgeblock=:score where PlayerID=:playerid",
              {
                  'score':score,
                  'playerid': playid
              })
    conn.commit()
    conn.close()