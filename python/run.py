from string import Template
from twilio.rest import Client
import mysql.connector

def mysqltwilio(name, num, id, message, status):
    mydb = mysql.connector.connect(host="<db_server>", database="<database>", user="root", passwd="<password>", auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    mycursor.execute("insert into <table>(ts, name, num, id, message, status) values (NOW(), %s, %s, %s, %s, %s)", (str(name), str(num), ''.join(id), str(message), str(status)))
    mydb.commit()

def erro_twiliosend(name, num, id):
    f= open("/<path>/documents/contact_list_INVALID_NUMBERS.csv","a+")
    f.write("%s;%s;%s\r\n" % (name, num, id))
    f.close()

def twiliosend(message_to_send, dest):
    account_sid = <"twilio_account_sid">
    auth_token = <"twilio_auth_token">
    client = Client(account_sid, auth_token)
    messagefull = client.messages.create(
        to=dest,
        from_=<"twilio_number">,
        body=message_to_send)

def get_users(file_name):
    names = []
    numbers = []
    ids = []
    with open(file_name, mode='r', encoding='utf-8') as user_file:
        for user_info in user_file:
            ids.append(user_info.split(';')[0])
            names.append(user_info.split(';')[1])
            numbers.append("+"+"<country_code>"+user_info.split(';')[2])
            numbers = [item.replace('\n','') for item in numbers]
    return names, numbers, ids

def template(file_name):
    with open(file_name, 'r', encoding='utf-8') as msg_template:
        msg_template_content = msg_template.read()
    return Template(msg_template_content)

def main():
    names, numbers, ids = get_users('/<path>/documents/contact_list.csv')
    for name, num, id in zip(names, numbers, ids):
        message_template = template('/<path>/documents/message.txt')
        message = message_template.substitute(USER_NAME=name)
        try:
            twiliosend(message, num)
            status = "SEND"
        except Exception:
            erro_twiliosend(name, num, id)
            status = "INVALID NUMBER"
        mysqltwilio(name, num, id, message, status)

if __name__ == '__main__':
    main()
