import psycopg2

def get_connection():
    return psycopg2.connect(database="test", user="postgres", password="password", host="127.0.0.1", port="5432")

def wczytaj_klientow():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("select * from klienci")
    rows = cursor.fetchall()
    conn.close()
    return rows

def zapisz_klienta(nazwa):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("insert into klienci(nazwa) values ('{}')".format(nazwa))
    conn.commit()
    conn.close()

def wyszukaj_klienta(nazwa):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("select * from klienci where nazwa = '{}'".format(nazwa))
    rows = cursor.fetchall()
    conn.close()
    return rows
