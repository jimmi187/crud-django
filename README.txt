CREATE DATABASE testDB;
CREATE USER jimi WITH PASSWORD '123';
GRANT ALL PRIVILEGES ON DATABASE testDB TO jimi;


//to speed it up
 ALTER ROLE jimi SET client_encodint TO 'uft8';
 ALTER ROLE jimi SET default_transaction_isolation TO 'read commited';
 ALTER ROLE jimi SET timezone TO 'UTC';
 