CREATE TABLE sms (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ts TIMESTAMP,
    name VARCHAR(30) NOT NULL,
    num VARCHAR(30) NOT NULL,
    id VARCHAR(9) NOT NULL,
    message VARCHAR(250) NOT NULL
);