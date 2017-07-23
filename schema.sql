create table klienci (
    klient_id smallserial primary key,
    nazwa varchar(255) unique
);

create table zadania (
    zadanie_id smallserial primary key,
    nazwa varchar(255),
    termin_realizacji date,
    waznosc smallint check(waznosc > 0 and waznosc <= 3),
    status varchar(20) check (status = 'aktywne' or status = 'wykonane'),
    klient_id smallint references klienci(klient_id)
);

create table uslugi (
    usluga_id smallserial primary key,
    nazwa varchar(255),
    opis text,
    cena_netto money,
    termin_waznosci date,
    klient_id smallint references klienci(klient_id)
);

