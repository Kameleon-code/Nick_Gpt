import sqlite3

conn = sqlite3.connect("db/udio.db", check_same_thread=False)
cur = conn.cursor()

#Чек пользователя в бд
def check_user_in_udio(user_id):
    cur.execute(f"SELECT * FROM udio WHERE user_id = {user_id}")
    user = cur.fetchone()[0]
    if user:
        return True
    else:
        return False
    
#Добавить юзера в бд
def add_user_in_udio(user_id: str, days: int, times: int):
    cur.execute(f"INSERT INTO udio (user_id, days, times) VALUES (?, ?, ?)", (user_id, days, times))
    conn.commit()

#Вытащить дни пользователя
def take_days_udio(user_id):
    cur.execute(f"SELECT days FROM udio WHERE user_id = {user_id}")
    days = cur.fetchone()[0]
    return days

#Вытащить дни пользователя
def take_times_udio(user_id):
    cur.execute(f"SELECT times FROM udio WHERE user_id = {user_id}")
    times = cur.fetchone()[0]
    return times

#Убиватель дней
def days_udio_killer(user_id):
    cur.execute(f"UPDATE udio SET days = days - {1} WHERE user_id = {user_id}")
    conn.commit()

#Убиватель генераций
def times_udio_killer(user_id):
    cur.execute(f"UPDATE udio SET times = times - {1} WHERE user_id = {user_id}")
    conn.commit()

#Достать всех пользователей бд
def take_all_udio_users():
    cur.execute(f"SELECT user_id FROM luma_udio")
    users = cur.fetchall()
    fin_list = []
    for i in users:
        fin_list.append(i[0])
    return fin_list

#Удалить пользователя из бд
def delete_from_udio(user_id):
    cur.execute(f"DELETE FROM udio WHERE user_id = {user_id}")
    conn.commit()