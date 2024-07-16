#연습문제 14.8 

#14.1 현재 디렉터리의 파일을 리스트로 출력하라.
import os
dir_list = os.listdir()
print(dir_list)

#14.2 상위(부모) 디렉터리의 파일을 리스트로 출력하라.
os.chdir('../')
os.listdir()

#14.3 ‘This is a test of the emergency text system’ 문자열을 test1 변수에 할당하라. 그리고 test1 변수를 test.txt 파일에 작성하라.
test1 = "This is a test of the emergency text system"
len(test1)

# open(), wirte(), close() 함수를 사용하여 파일을 작성
outfile = open('test.txt', 'wt')
outfile.write(test1)

outfile.close()
# with 문 사용
with open('test.txt', 'wt') as outfile:
     outfile.write(test1)

#14.4 test.txt 파일을 열어서 내용을 읽고, test2 문자열에 저장하라. test1과 test2의 값이 같은가?
test2 = open('test.txt', 'rt')
test1 == test2.read()

test2.close()
