# 아래에 코드를 작성하세요.
import random

numbers = range(1,46)

lotto = random.sample(numbers, 6)

print(f'오늘의 행운의 숫자는 {sorted(lotto)} 입니다.')
