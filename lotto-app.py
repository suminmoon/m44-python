# 아래에 코드를 작성하세요.
import random

numbers = range(1,46)

lotto = random.sample(numbers, 6)

print(sorted(lotto))
