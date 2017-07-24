import psycopg2

class Klient:
    def __init__(self, id, nazwa):
        self.id = id
        self.nazwa = nazwa

def get_connection():
    return psycopg2.connect(database="test", user="postgres", password="password", host="127.0.0.1", port="5432")

def wczytaj_klientow():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("select * from klienci")
    rows = cursor.fetchall()
    conn.close()
    klienci = []
    for row in rows:
    	klienci.append(Klient(row[0], row[1]))
    return klienci

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