import sqlite3

conn = sqlite3.connect("db/db_pag.db", check_same_thread=False)
cursor = conn.cursor()

def pages(num):
    cursor.execute(f"SELECT page FROM pagination WHERE page = {num}")
    page_ = cursor.fetchone()[0]
    return page_

def title(num):
    cursor.execute(f"SELECT title FROM pagination WHERE page = {num}")
    title_ = cursor.fetchone()[0]
    return title_

def stat(num):
    cursor.execute(f"SELECT spend FROM pagination WHERE page = {num}")
    stat_ = cursor.fetchone()[0]
    return stat_

def stat_eng(num):
    cursor.execute(f"SELECT spend_eng FROM pagination WHERE page = {num}")
    stat_ = cursor.fetchone()[0]
    return stat_

def stat_es(num):
    cursor.execute(f"SELECT spend_es FROM pagination WHERE page = {num}")
    stat_ = cursor.fetchone()[0]
    return stat_

def stat_cn(num):
    cursor.execute(f"SELECT spend_cn FROM pagination WHERE page = {num}")
    stat_ = cursor.fetchone()[0]
    return stat_

def pages_count():
    cursor.execute("SELECT COUNT(*) FROM pagination")
    pages = cursor.fetchone()[0]
    return pages