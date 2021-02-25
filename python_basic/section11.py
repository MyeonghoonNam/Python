# Section11
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME = text/csv

import csv

# 예제 1
with open('D:/코딩/Python/python_basic/resource/sample1.csv', 'r') as f:
  reader = csv.reader(f)
  next(reader) # Header 스킵(하나의 행 스킵)
  print(reader)

  for c in reader:
    print(c)

print("-----------------------------------------")
print("-----------------------------------------")

# 예제 2
with open('D:/코딩/Python/python_basic/resource/sample2.csv', 'r') as f:
  reader = csv.reader(f, delimiter='|') # 기본값 : ,
  next(reader)

  for c in reader:
    print(c)

print("-----------------------------------------")
print("-----------------------------------------")

# 예제 3
with open('D:/코딩/Python/python_basic/resource/sample1.csv', 'r') as f:
  reader = csv.DictReader(f)

  for c in reader :
    for k, v in c.items():
      print(k, v)
    print('-----------')

print("-----------------------------------------")
print("-----------------------------------------")

# 예제 4
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]

with open('D:/코딩/Python/python_basic/resource/sample3.csv', 'w', newline='') as f:  # newline='' 테스트
    wt = csv.writer(f)
    # dir 확인
    print(dir(wt))
    print(type(wt))
    for v in w:
        wt.writerow(v) # 줄바꿈 적용

# 예제 5
with open('D:/코딩/Python/python_basic/resource/sample4.csv', 'w', newline='') as f:
  wt = csv.writer(f)
  wt.writerow(w)

# XSL, XLSX
# openpyxl, xlxxwriter, xlrd, xlwt, xlutils
# pandas를 주로 사용(openpyxl, xlrd를 내부적으로 사용)

# pip install xlrd   설치 필요
# pip install openpyxl 설치 필요
# pip install pandas 설치 필요

import pandas as pd

# sheetname='시트명' 또는 숫자(첫 번째 시트가 1), header=3, skiprow=1 실습
xlsx = pd.read_excel('D:/코딩/Python/python_basic/resource/sample.xlsx')

# 상위 데이터 확인(5개)
print(xlsx.head())
print()

# 하위 데이터 확인(5개)
print(xlsx.tail())

# 행, 열 반환
print(xlsx.shape)

# 엑셀 or CSV 다시 쓰기
xlsx.to_excel('D:/코딩/Python/python_basic/resource/result.xlsx', index=False) # index = 행 번호 붙이는 옵션
xlsx.to_csv('D:/코딩/Python/python_basic/resource/result.csv', index=False)