create table Flights (
    id           integer primary key autoincrement not null,
    fdate  text ,
    source text,
    dest text,
    price text,
    airline text,
    ftimestamp date,
    json text
);