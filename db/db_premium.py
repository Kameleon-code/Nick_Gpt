import sqlite3
from datetime import time

conn = sqlite3.connect("db/db_premium.db", check_same_thread=False)
cursor = conn.cursor()

#Доавбавление юзера в бд
def user_in_prem (user_id: int, days: int):
    cursor.execute("INSERT INTO users_premium (user_id, days) VALUES (?, ?)", (user_id, days))
    conn.commit()

#Проверка на наличие юзера в бд
def check_user_prem(uid):
    cursor.execute(f"SELECT * FROM users_premium WHERE user_id = {uid}")
    user = cursor.fetchone()
    if user:
        return True
    else:
        return False
    
#Удалить пользователя из бд
def delete_user(uid):
    cursor.execute(f"DELETE FROM users_premium WHERE user_id = {uid}")
    conn.commit()
    
#Вытащить user_id

def user_id_prem(uid):
    cursor.execute(f"SELECT user_id FROM users_premium WHERE user_id = {uid}")
    user_id = cursor.fetchone()[0]
    return user_id

#Вытащить user_time

def user_time(uid):
    cursor.execute(f"SELECT user_time FROM users_premium WHERE user_id = {uid}")
    user_time = cursor.fetchone()[0]
    return user_time

#Вытащить days

def days(uid):
    cursor.execute(f"SELECT days FROM users_premium WHERE user_id = {uid}")
    days = cursor.fetchone()[0]
    return days

#Обновоить колличетсво дней
def days_update(uid):
    cursor.execute(f"UPDATE users_premium SET days = days - {1} WHERE user_id = {uid}")
    conn.commit()

#Вытщить инфо о пользователе
def u_in():
    cursor.execute(f"SELECT user_id FROM users_premium")
    user_ids = cursor.fetchall()
    return user_ids