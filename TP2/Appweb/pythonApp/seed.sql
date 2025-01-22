CREATE DATABASE soupa_db;

USE soupa_db;

CREATE TABLE users (
    id int,
    name varchar(255)
);

INSERT INTO users (id, name)
VALUES
("1", "bob"),
("2", "martin"),
("3", "pikachu"),
("4", "shibboleth");

CREATE USER 'meow'@'%' IDENTIFIED BY 'meow';
GRANT ALL PRIVILEGES ON *.* TO 'meow'@'%';