-- settings.sql
CREATE DATABASE covidapp;
CREATE USER covidappuser WITH PASSWORD 'covidapp';
GRANT ALL PRIVILEGES ON DATABASE covidapp TO covidappuser;