#  지원자_ => 합격자_

import os

os.chdir(r'C:\Users\msm03\PycharmProjects\m44-python2\manufacture-files\dummy-ex')
filenames = os.listdir('.')

for filename in filenames:
    txt = os.path.splitext(filename)[-1]
    if txt == '.txt':
        newFilename = filename.replace('지원자_지원자_', '합격자_')  # 파일명을 string 으로 가져와서 글자 바꾸는 것 까지만 됨
        os.rename(filename, newFilename)  # 여기까지 해야 파일 명이 바뀌는 것 까지 됨


