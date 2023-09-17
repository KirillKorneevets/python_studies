from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)
app.debug = True
conn = psycopg2.connect(dbname='lessflask', user='postgres', password='Asdcvbjkl763', host='localhost')


@app.get('/users/<int:user_id>') 
def get_users(user_id):
    cursor = conn.cursor()
    sql_query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(sql_query, (user_id,))
    user = cursor.fetchone()
    return jsonify(user)

@app.post('/users')
def create_user():
    cursor = conn.cursor()
    name = request.form.get('name')
    age = request.form.get('age')
    sql_create_database = f"INSERT INTO users (username, age) values ('{name}', {age})"
    cursor.execute(sql_create_database)
    conn.commit()

    return 'User created'

@app.put('/users/<int:_id>')
def update_user(_id):
    cursor = conn.cursor()
    name = request.form.get('name')
    age = request.form.get('age')
    sql_create_database = f"update users set age = {age}, username = '{name}' where id = {_id}"
    cursor.execute(sql_create_database)
    conn.commit()

    return 'User update'

@app.delete('/users/<int:_id>')
def delete_user(_id):
    cursor = conn.cursor()
    sql_create_database = f"delete from users where id = {_id}"
    cursor.execute(sql_create_database)
    conn.commit()

    return 'User delete'


if __name__ == '__main__':
    app.run()
