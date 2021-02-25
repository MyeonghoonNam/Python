# Section12-1
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

import sqlite3
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now : ', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)

# sqlite3
print('version : ', sqlite3.version)

# DB 생성 & Auto Commit <=> Rollback
conn = sqlite3.connect('D:/코딩/Python/python_basic/resource/database.db', isolation_level=None)

# Cursor
c = conn.cursor()
print('Cursor Type : ', type(c))

# 테이블 생성(Data Type : TEXT, NUMERIC INTEGER REAL BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")

# 데이터 삽입
# c.execute("INSERT INTO users VALUES (1 ,'Kim','Kim@naver.com', '010-0000-0000', 'Kim.com', ?)", (nowDatetime,))

# c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", (2, 'Park', 'Park@naver.com', '010-1111-1111', 'Park.com', nowDatetime))

# Many 삽입(튜플, 리스트)
userList = (
    (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', nowDatetime),
    (4, 'Cho', 'Cho@naver.com', '010-3333-3333', 'Cho.com', nowDatetime),
    (5, 'Yoo', 'Yoo@naver.com', '010-4444-4444', 'Yoo.com', nowDatetime)
)

c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", userList)

# 테이블 데이터 삭제
# conn.execute("Delete FROM users")
# print("users db deleted : ", conn.execute("Delete FROM users").rowcount, "rows") => rowcount는 지운행 반환

# 커밋 : isolation_level=None 일 경우 자동 반영(Auto Commit)
# 반영 코드를 안넣었으면 conn.commit()으로 커밋 반영

# 롤백
# conn.rollback()

# 접속 해제
conn.close()