import psycopg2 
try:
    conn = psycopg2.connect(database = "GITHUB",
                            user = "postgres",
                            password = "123",
                            host = "78.141.227.124")
    print("db connected successfully")
    cur = conn.cursor()
    cur.execute("SELECT COUNT(students) FROM students where age > 15")
    students = cur.fetchall()
    conn.commit()
    print(students)
except Exception as err:
    print("not connected", err)

