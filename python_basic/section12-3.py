# Section12-3
# 파이썬 데이터베이스 연동
# 테이블 데이터 수정 및 삭제

import sqlite3

conn = sqlite3.connect('D:/코딩/Python/python_basic/resource/database.db', isolation_level=None)

c = conn.cursor()

# 데이터 수정1
# c.execute("UPDATE users SET username = ? WHERE id = ?", ('niceman', 1))

# 데이터 수정2
# c.execute("UPDATE users SET username = :name WHERE id = :id", {"name": 'niceman', 'id': 3})

# 데이터 수정3
# c.execute("UPDATE users SET username = '%s' WHERE id = '%s'" % ('badboy', 5))

# 중간 데이터 확인1
for user in c.execute('SELECT * FROM users'):
    print(user)

# Row Delete1
c.execute("DELETE FROM users WHERE id = ?", (2,))

# Row Delete2
c.execute("DELETE FROM users WHERE id = :id", {'id': 5})

# Row Delete3
c.execute("DELETE FROM users WHERE id = '%s'" % 4)

print()

# 중간 데이터 확인2
for user in c.execute('SELECT * FROM users'):
    print(user)

# 테이블 전체 데이터 삭제
print("users db deleted : ", conn.execute("delete from users").rowcount, "rows")

# 접속 해제
conn.close()

# DB 사용 권장 이유
# 데이터표준화, 데이터독립성, 보안철저, 실시간처리, 백업, 복원