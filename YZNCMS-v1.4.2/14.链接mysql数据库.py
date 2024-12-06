import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def main():
    host = "localhost"
    user = "root"
    password = "123456"
    db = "fast"

    # 创建数据库连接
    conn = create_connection(host, user, password, db)
    if conn is not None:
        # 执行创建表的SQL语句
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INT
        );
        """
        execute_query(conn, create_table_query)
        
        # 插入数据
        insert_query = """
        INSERT INTO users (name, age) VALUES (%s, %s);
        """
        cursor = conn.cursor()
        cursor.execute(insert_query, ('Alice', 30))
        conn.commit()
        print("User inserted successfully")

        # 查询数据
        select_query = "SELECT * FROM users"
        cursor.execute(select_query)
        records = cursor.fetchall()
        print("Users:")
        for row in records:
            print(row)

        # 关闭连接
        cursor.close()
        conn.close()
    else:
        print("Unable to connect to the database")

if __name__ == '__main__':
    main()