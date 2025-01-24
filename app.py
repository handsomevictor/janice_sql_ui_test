from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import sys

app = Flask(__name__)


# 连接数据库
def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',  # 或者是 EC2 的 IP 地址
        user='pretty_janice',  # 数据库用户名
        password='janice',  # 数据库密码
        database='my_test_db'
    )
    return conn


# 显示所有表格的内容
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # 获取所有表格的数据
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()

    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()

    cursor.execute("SELECT * FROM order_items")
    order_items = cursor.fetchall()

    conn.close()

    return render_template('index.html', customers=customers, orders=orders, order_items=order_items)


# 执行用户输入的 SQL 语句
@app.route('/execute_sql', methods=['POST'])
def execute_sql():
    sql_query = request.form['sql_query']
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(sql_query)
        result = cursor.fetchall()
        conn.commit()
    except Exception as e:
        result = str(e)
    conn.close()
    return render_template('index.html', result=result)


# 插入数据
@app.route('/insert_data', methods=['POST'])
def insert_data():
    table = request.form['table']
    values = request.form['values']

    conn = get_db_connection()
    cursor = conn.cursor()

    if table == 'customers':
        cursor.execute("INSERT INTO customers (name, email) VALUES (%s, %s)", tuple(values.split(',')))
    elif table == 'orders':
        cursor.execute("INSERT INTO orders (customer_id, order_date) VALUES (%s, %s)", tuple(values.split(',')))
    elif table == 'order_items':
        cursor.execute("INSERT INTO order_items (order_id, product_name, quantity) VALUES (%s, %s, %s)",
                       tuple(values.split(',')))

    conn.commit()
    conn.close()

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=5787)
