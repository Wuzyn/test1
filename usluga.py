import psycopg2

class Usluga:
    def __init__(self, id, nazwa, opis, cena_netto, termin_waznosci, klient_id):
        self.id = id
        self.nazwa = nazwa
        self.opis = opis
        self.cena_netto = cena_netto
        self.termin_waznosci = termin_waznosci
        self.klient_id = klient_id

def get_connection():
    return psycopg2.connect(database="test", user="postgres", password="password", host="127.0.0.1", port="5432")

def wczytaj_uslugi(id_klienta):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("select * from uslugi where klient_id = {}".format(id_klienta))
    rows = cursor.fetchall()
    conn.close()
    return rows

def zapisz_usluge(usluga):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("insert into uslugi(nazwa, opis, cena_netto, termin_waznosci, klient_id) "
                   "values ('{}', '{}', {}, {}, {})"
                   .format((usluga.nazwa, usluga.opis, usluga.cena_netto, usluga.termin_waznosci, usluga.klient_id)))
    conn.commit()
    conn.close()

def wyszukaj_usluge(nazwa_uslugi, klient_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("select * from uslugi where klient_id = {} and nazwa = '{}'".format(klient_id, nazwa_uslugi))
    rows = cursor.fetchall()
    conn.close()
    return rows