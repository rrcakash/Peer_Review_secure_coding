import os
import pymysql
from urllib.request import urlopen

db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')

}

def get_user_input():
    user_input = input('Enter your name: ')
    return re.sub(r'[^a-zA-Z0-9 ]', '', user_input)

def send_email(to, subject, body):
    subprocess.run(['mail', '-s', subject, to], input=body, text=True)

def get_data():
    url = 'http://insecure-api.com/get-data'
    data = urlopen(url).read().decode()
    return data

def save_to_db(data):
    query = f"INSERT INTO mytable (column1, column2) VALUES (%s, %s)"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query, (data, 'Another Value'))
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
