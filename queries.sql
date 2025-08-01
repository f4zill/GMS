create database gym;

use gym;

CREATE TABLE members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(100)
);

CREATE TABLE trainers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    specialty VARCHAR(100)
);

CREATE TABLE equipment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    type VARCHAR(100)
);

CREATE TABLE workout_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT,
    date DATE,
    description TEXT
);

CREATE TABLE payments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT,
    amount DECIMAL(8,2),
    date DATE
);

CREATE TABLE sessions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT,
    trainer_id INT,
    session_date DATE,
    notes TEXT
);

delete from trainers where id='1';