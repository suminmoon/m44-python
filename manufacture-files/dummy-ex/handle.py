import os
#  os.chdir('폴더경로') 지정한 폴더로 이동
#  os.listdir('폴더경로') 폴더에 저장된 전체 파일 목록을 list 로 반환
#  os.rename('헌재파일명', '바꿀 파일명') 파일이름 변경
#  os.path.splitext('파일이름') 파일 경로와 확장자를 분리하여 반환
#  폴더 경로 C:\Users\msm03\PycharmProjects\m44-python2\manufacture-files\dummy-ex

# filename = os.path.splitext(r'C:\Users\msm03\PycharmProjects\m44-python2\manufacture-files\dummy-ex\dummy.py')
#  =>  ('C:\\Users\\msm03\\PycharmProjects\\m44-python2\\manufacture-files\\dummy-ex\\dummy', '.py')

os.chdir(r'C:\Users\msm03\PycharmProjects\m44-python2\manufacture-files\dummy-ex')
filenames = os.listdir('.')

for filename in filenames:
    txt = os.path.splitext(filename)[-1]
    if txt =='.txt':
        #  앞에 지원자_ 를 붙인다.
        os.rename(filename, f'지원자_{filename}')


