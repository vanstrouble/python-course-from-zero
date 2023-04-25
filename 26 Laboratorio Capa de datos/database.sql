# User data laboratory Database

CREATE DATABASE IF NOT EXISTS testing;
CREATE DATABASE testing;

USE testing;
CREATE EXTENSION pqcrypto; # Not working PostgreSQL 14

CREATE TABLE IF NOT EXISTS users (
    id_user SERIAL PRIMARY KEY NOT NULL,
    username varchar(15) NOT NULL,
    password VARCHAR(20) NOT NULL
);