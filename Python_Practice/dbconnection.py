
import cx_Oracle

# Connect as user "hr" with password "welcome" to the "oraclepdb" service running on this computer.
connection = cx_Oracle.connect("hr", "hr", "127.0.0.1")

cursor = connection.cursor()
cursor.execute("""SELECT first_name,last_name  FROM employees""")
for fname, lname in cursor:
    print ("first name -->",fname,"last_name -->",lname)



