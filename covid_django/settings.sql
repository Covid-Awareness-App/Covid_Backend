-- settings.sql
CREATE DATABASE covid;
CREATE USER coviduser WITH PASSWORD 'covid';
GRANT ALL PRIVILEGES ON DATABASE covid TO coviduser;