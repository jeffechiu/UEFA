DROP DATABASE IF EXISTS Rankings;
CREATE DATABASE Rankings;
\c rankings;

\i create.sql

\copy countries from 'countries.csv' csv header;

\copy firstCL1415 from 'firstCL1415.csv' csv header;