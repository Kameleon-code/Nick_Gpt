import sqlite3

conn = sqlite3.connect("db/db_users_ai.db", check_same_thread=False)
cursor = conn.cursor()

#Добавление юзера в бд
def user_in_db (user_id: int, username: str, user_name: str, user_ling: str, user_balance_tokens: int, user_asks: int, neuronetwork: str, premium_days: int):
    cursor.execute("INSERT INTO users_ai (user_id, username, user_name, user_ling, user_balance_tokens, user_asks, neuronetwork, premium_days) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (user_id, username, user_name, user_ling, user_balance_tokens, user_asks, neuronetwork, premium_days))
    conn.commit()

#Обновление языка
def user_lingo(uid, user_ling):
    cursor.execute(f"UPDATE users_ai SET user_ling = ? WHERE user_id = ?", (f"{user_ling}", uid))
    conn.commit()

#Проверка на наличие юзера в бд
def check_user(uid):
    cursor.execute(f"SELECT * FROM users_ai WHERE user_id = {uid}")
    user = cursor.fetchone()
    if user:
        return True
    else:
        return False
    
#Подписка премиум
def premium_counter(uid):
    cursor.execute(f"UPDATE users_ai SET premium_days = {30} WHERE user_id = {uid}")
    conn.commit()

#Возвратить юзернейм юзера
def user_name(uid):
    cursor.execute(f"SELECT username FROM users_ai WHERE user_id = {uid}")
    user_name = cursor.fetchone()[0]
    return user_name

#Возравтить id юзера
def user_id(uid):
    cursor.execute(f"SELECT user_id FROM users_ai WHERE user_id = {uid}")
    user_id = cursor.fetchone()[0]
    return user_id

#Достать язык пользователя из бд
def lingo(uid):
    cursor.execute(f"SELECT user_ling FROM users_ai WHERE user_id = {uid}")
    lingo = cursor.fetchone()[0]
    return lingo

#Возрватить нейросеть, которая используется пользователем
def neuro(uid):
    cursor.execute(f"SELECT neuronetwork FROM users_ai WHERE user_id = {uid}")
    neuronet = cursor.fetchone()[0]
    return neuronet

#Количество вопросов заданных юзером
def asks(uid):
    cursor.execute(f"SELECT user_asks FROM users_ai WHERE user_id = {uid}")
    asks = cursor.fetchone()[0]
    return asks

def asks_update(uid):
    cursor.execute(f"UPDATE users_ai SET user_asks = user_asks + {1} WHERE user_id = {uid}")
    conn.commit()


#Баланс юзера в токенах
def user_tokens(uid):
    cursor.execute(f"SELECT user_balance_tokens FROM users_ai WHERE user_id = {uid}")
    token_balance = cursor.fetchone()[0]
    return token_balance

def user_tokens_update(uid, total_tokens):
    cursor.execute(f"UPDATE users_ai SET user_balance_tokens = user_balance_tokens - {total_tokens} WHERE user_id = {uid}")
    conn.commit()


def premium_tokens_update(uid, total_tokens):
    cursor.execute(f"UPDATE users_ai SET user_balance_tokens = user_balance_tokens - {total_tokens / 2} WHERE user_id = {uid}")
    conn.commit()

def tokens_plus_update(uid, tokens):
    cursor.execute(f"UPDATE users_ai SET user_balance_tokens = user_balance_tokens + {tokens} WHERE user_id = {uid}")
    conn.commit()

#Премиум дни пользователя
def premium_days(uid):
    cursor.execute(f"SELECT premium_days FROM users_ai WHERE user_id = {uid}")
    user_premium= cursor.fetchone()[0]
    return user_premium

#Обновить дни после покупки премиум
def premium_days_set(uid, premium_days):
    cursor.execute(f"UPDATE users_ai SET premium_days = ? WHERE user_id = ?", (f"{premium_days}", uid))
    conn.commit()

#Обновить Нейронку в бд
def update_ai(uid, ai):
    cursor.execute(f"UPDATE users_ai SET neuronetwork = ? WHERE user_id = ?", (f"{ai}", uid))
    conn.commit()

#Роль
def role(uid):
    cursor.execute(f"SELECT role FROM users_ai WHERE user_id = {uid}")
    role= cursor.fetchone()[0]
    return role

#Обновить роль
def set_mode(uid, num):
    cursor.execute(f"UPDATE users_ai SET role = ? WHERE user_id = ?", (f"{num}", uid))
    conn.commit()

#Внести ответ Chat_gpt в бд
def ans_gpt(uid, answer):
    cursor.execute(f"UPDATE users_ai SET answer = ? WHERE user_id = ?", (f"{answer}", uid))
    conn.commit()

def ready_answer_gpt(uid):
    cursor.execute(f"SELECT answer FROM users_ai WHERE user_id = {uid}")
    ans = cursor.fetchone()[0]
    return ans