import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        database="iot_data",
        user="iot_user",
        password="iot_password",
        port="5432"
    )

    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"Database connection successful! PostgreSQL version: {db_version}")

except Exception as e:
    print(f"Database connection failed: {e}")

finally:
    if 'connection' in locals() and connection:
        cursor.close()
        connection.close()
