import psycopg2

try:
    conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="5571", port="5433")

    cur = conn.cursor()

except psycopg2.Error as e:
    print(e)

    print(cur.fetchall())

    conn.commit()

    cur.close()
    conn.close()

