import pymysql as mdb
from bottle import FormsDict
from hashlib import sha256
import os

# connection to database project2
def connect():
    """makes a connection to MySQL database.
    @return a mysqldb connection
    """

    #TODO: 1 of 6 fill out MySQL connection parameters. 
    # Use the netid and given password of the repo you are committing your solution to.
    # See the file we gave you called dbrw.secret in your repo.
    # Do not change this value - we use it when grading. 

    return mdb.connect(host="localhost",
                       user="lukasa3",
                       passwd="9345ac89127ba9aafe81c15ef8b6aceb9fe5d40a39c8ba8eadd06ff2ecbffee2",
                       db="project2");

def createUser(username, password):
    """ creates a row in table named users
    @param username: username of user
    @param password: password of user
    """

    salt = os.urandom(32)
    salted = salt + str.encode(password)

    m = sha256()
    m.update(salted)
    passwordhash = hex(int.from_bytes(m.digest(), byteorder="big"))[2:]
    salt = hex(int.from_bytes(salt, byteorder="big"))[2:]

    db_rw = connect()
    cur = db_rw.cursor()
    cur.execute("INSERT INTO users (username, salt, passwordhash) VALUES ('" + str(username) + "','" + str(salt) + "','" + str(passwordhash) + "');")
    #TODO 2 of 6. Use cur.execute() to insert a new row into the users table containing the username, salt, and passwordhash
    db_rw.commit()

def validateUser(username, password):
    """ validates if username,password pair provided by user is correct or not
    @param username: username of user
    @param password: password of user
    @return True if validation was successful, False otherwise.
    """

    db_rw = connect()
    cur = db_rw.cursor()
    #TODO 3 of 6. Use cur.execute() to select the appropriate user record (if it exists)
    cur.execute("SELECT salt, passwordhash FROM users WHERE username = '" + username + "';")
    if cur.rowcount < 1:
        return False
    user_record = cur.fetchone()
    print(user_record) # Delete this later
    salt_hex = user_record[0]
    while len(salt_hex) < 64:
        salt_hex = "0" + salt_hex
    salt = bytes.fromhex(salt_hex)
    passwordhash_authoritative = user_record[1]
    salted = salt + str.encode(password)

    m = sha256()
    m.update(salted)
    passwordhash = hex(int.from_bytes(m.digest(), byteorder="big"))[2:]

    if passwordhash_authoritative == passwordhash:
        return True
    else:
        return False

def fetchUser(username):
    """ checks if there exists given username in table users or not
    if user exists return (id, username) pair
    if user does not exist return None
    @param username: the username of a user
    @return The row which has username is equal to provided input
    """

    db_rw = connect()
    cur = db_rw.cursor(mdb.cursors.DictCursor)
    #TODO 4 of 6. Use cur.execute() to fetch the row with this username from the users table, if it exists
    cur.execute("SELECT id, username FROM users WHERE username = '" + username + "';")
    if cur.rowcount < 1:
        return None    
    return FormsDict(cur.fetchone())

def addHistory(user_id, query):
    """ adds a query from user with id=user_id into table named history
    @param user_id: integer id of user
    @param query: the query user has given as input
    """

    db_rw = connect()
    cur = db_rw.cursor()
    #TODO 5 of 6. Use cur.execute() to add a row to the history table containing the correct user_id and query
    cur.execute("INSERT INTO history (query, user_id) VALUES ('"+ str(query) + "','" + str(user_id) + "');")
    db_rw.commit()

def getHistory(user_id):
    """ grabs last 15 queries made by user with id=user_id from
    table named history in descending order of when the searches were made
    @param user_id: integer id of user
    @return a first column of a row which MUST be query
    """

    db_rw = connect()
    cur = db_rw.cursor()
    #TODO 6 of 6. Use cur.execute() to fetch the most recent 15 queries from this user (including duplicates). 
    # Note: Make sure the query text is at index 0 in the returned rows. 
    # Otherwise you will get an error when the templating engine tries to use this object to build the HTML reply.
    cur.execute("SELECT query, user_id FROM history WHERE user_id = '" + str(user_id) + "' ORDER BY id DESC LIMIT 15;")
    rows = cur.fetchall();
    return [row[0] for row in rows]
