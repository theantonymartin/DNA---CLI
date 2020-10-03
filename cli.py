import subprocess as sp
import pymysql
import pymysql.cursors


def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

# CLI Loop
while(1):
    tmp = sp.call('clear', shell=True)

    try:
        con = pymysql.connect(host='sql12.freemysqlhosting.net',
                              user="sql12368514",
                              password="larZ24F2qN",
                              db='sql12368514',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected to the Database.")
        else:
            print("Failed to connect.)

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                # Here taking example of Employee Mini-world
                print("1. Option 1")  # Hire an Employee
                print("2. Option 2")  # Fire an Employee
                print("3. Option 3")  # Promote Employee
                print("4. Option 4")  # Employee Statistics
                print("5. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 5:
                    break
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except:
        tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
