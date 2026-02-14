from database import engine

try:
    conn = engine.connect()
    print("DB connected successfully")
    conn.close()
except Exception as e:
    print("Error:", e)
