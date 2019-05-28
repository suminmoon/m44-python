print("안녕하세요")
print('저는 수민입니다.')
print('만나서 반갑습니다.')

# ''' -> 3개를 이어서 쓰면 줄바꿈 가능
print('''

안녕하세요
저는 문입니다.
오늘은 비 오는 날
''')

# Range
# 숫자의 범위를 가지고 있다.
print(range(5))  # => range(0, 5)

# List 형변환
a = list(range(5))
print(a)  # [0, 1, 2, 3, 4]

# Range를 이용한 반복문
for i in range(3):
    print(i)

# List
# 배열이다. 여러 개의 멤버 변수를 가질 수 있으며 index 를 통한 접근이 가능하다. Array
numbers = [0,1,2,3]
print(numbers[-1])
print('=============')
numbers = [3,1,2]
# sorted 함수는 배열을 정렬해주지만 원본을 바꾸지 않는다.
print(sorted(numbers))  # [1, 2, 3]
print(numbers)  # [3, 1, 2]

print(numbers.sort())  # None
print(numbers) # [1, 2, 3]

# Dictionary
# key 와 value 로 이루어진 자료구조
# 다른 언어에서는 map, object 라고도 불린다.
phonebook = {
    '중국집': '123-123',
    '초밥집': '533-345',
    '김밥집' : '555-123'
}
print(phonebook['중국집'])  # 123-123
