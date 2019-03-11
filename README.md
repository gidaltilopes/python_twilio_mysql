# Twilio
Sending sms through python's twilio module and logging into a mysql database for parsing.

## Python
***Template:***  *provide simpler string substitutions.* <br />
***Twilio Library:***  *interaction between the Twilio API and the Python application.* <br />
***Mysql:*** *standardized database driver for Python platforms and development.* <br />
## Docker
***Dockerfile:*** *build an docker image that starts the project.*
## Ansible
***Playbook:*** *manage the containers with `docker_container` module.*
## Mysql
*Records all SMS sent.*
<br />
<br />
<br />
### How to use
1. Build a docker image <br />
```docker build -t <container_name> .```
<br />
<br />
2. Create a MySQL database with the following syntax
```CREATE TABLE smstable (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ts TIMESTAMP,
    name VARCHAR(30) NOT NULL,
    num VARCHAR(30) NOT NULL,
    id VARCHAR(9) NOT NULL,
    message VARCHAR(250) NOT NULL
);```

3. Run Ansible playbook. <br />
```ansible-paybook /<path>/ansible/playbook.yml```
