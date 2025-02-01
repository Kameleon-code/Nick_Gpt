import sqlite3

conn = sqlite3.connect("db\luma_udio.db", check_same_thread=False)
cur = conn.cursor()

#Чек юзера в бд
def check_user_in_luma(user_id):
    cur.execute(f"SELECT * FROM luma_udio WHERE user_id = {user_id}")
    user = cur.fetchone()
    if user:
        return True
    else: 
        return False

#Добавлене юезра в бд
def add_user_in_luma(user_id: str, days: int, times: int, mode: str, seconds: str):
    cur.execute(f"INSERT INTO luma_udio (user_id, days, times, mode, seconds) VALUES (?, ?, ?, ?, ?)", (user_id, days, times, mode, seconds))
    conn.commit()

#Удалить юзера из бд
def delete_user_from_luma(user_id):
    cur.execute(f"DELETE FROM luma_udio WHERE user_id = {user_id}")
    conn.commit()

#Вытащить дни пользователя
def take_days_from_luma(user_id):
    cur.execute(f"SELECT days FROM luma_udio WHERE user_id = {user_id}")
    days = cur.fetchone()[0]
    return days

#Вытащить user_id
def take_user_id_from_lume(user_id):
    cur.execute(f"SELECT days FROM luma_udio WHERE user_id = {user_id}")
    user_id = cur.fetchone()[0]
    return user_id

#Вытащить версию нейронки
def take_mode_kling(user_id):
    cur.execute(f"SELECT mode FROM luma_udio WHERE user_id = {user_id}")
    mode = cur.fetchone()[0]
    return mode

#Вытщить секунды
def take_seconds(user_id):
    cur.execute(f"SELECT seconds FROM luma_udio WHERE user_id = {user_id}")
    sec = cur.fetchone()[0]
    return sec

#Сократитель дней
def short_days(user_id):
    cur.execute(f"UPDATE luma_udio SET days = days - {1} WHERE user_id = {user_id}")
    conn.commit()

#Сократитель дней
def times_killer(user_id):
    cur.execute(f"UPDATE luma_udio SET times = times - {1} WHERE user_id = {user_id}")
    conn.commit()

#Достать всех юзеров из бд
def take_all_luma_users():
    cur.execute(f"SELECT user_id FROM luma_udio")
    users = cur.fetchall()
    fin_list = []
    for i in users:
        fin_list.append(i[0])
    return fin_list