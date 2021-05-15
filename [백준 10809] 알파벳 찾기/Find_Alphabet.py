# find 함수 사용
from string import ascii_lowercase  # 파이썬 내장되어있는 string 문자열에서 ascii_lowercase(소문자) 를 import
ascii_List = list(ascii_lowercase)  # ascii_lowercase 를 ascii_List 라는 변수에 리스트 형태로 넣어주기
# ascii_List = ['a','b', ..., 'z']

S = input()  # 단어 입력
for i in range(len(ascii_List)):  # ascii_List 의 길이 만큼 i를 반복
    print(S.find(ascii_List[i]), end=" ")  # find()함수로 ascii_List[i]에 해당하는 ['a','b',..,'z']의 위치를 찾아서 end 로 개행 없이 한 줄로 출력