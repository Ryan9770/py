### 변수
# 변수 선언
# 변수는 = 연산자를 이용하여 할당
# 파이썬은 기본적으로 변수 선언 시의 자료형의 인식이 자동으로 이루어짐

x = 4
y = 'Ryan'
x = "Lee" # 위에서 X에 할당된 4의 값은 Lee로 덮어씌워짐
print(x) # "Lee"


### 캐스팅
# 변수에 값을 할당할때, 변수의 자료형을 지정해 줄 수 있긴함
x = str(3) 
print(x) # '3'

y = int(3) 
print(y) # 3

z = float(3)
print(z) # 3.0


### 자료형 확인
# type() 함수를 활용하여 변수의 자료형 확인 가능
x = 5 
y= 'Ryan'

print(type(x)) # <class 'int'>
print(type(y)) # <class 'str'>


### 따옴표, 쌍따옴표
# 파이썬에서 따옴표와 쌍따옴표는 String 자료형을 할당할때 사용됨
# 개행이 포함된 문단을 그대로 표현하려면 쌍따옴표 3개(""")를 이용하여 감싸면 문단의 형태의 변경없이 String 자료형으로 변환됨
x = 'Lee'
y = "Lee"
z = """
    Dear Ryan Lee
    
    Hello world!

    Learn to Python is Exciting!

    By myself
    """


### Case-Sensitive
# 변수를 선언할때, 파이썬은 대소문자 구분이됨
# A와 a 변수는 서로 다른 변수임


### 변수명
# 파이썬 변수명은 자유롭게 설정가능하나 권장사항과 필수사항이 존재하며 아래와 같음
# 1. 변수명은 문자나 밑줄로 시작
# 2. 변수명은 숫자로 시작할 수 없음
# 3. 변수명에는 영문, 숫자, 밑줄만 포함될 수 있음
# 4. 변수명은 영문 대소문자를 구분함
# 5. 변수명은 파이썬의 키워드를 사용할 수 없음

# 또한 변수명은, 카멜,파스칼, 스네이크 케이스 중 선택하여 사용함
myVariableType = 'Camel'
MyVariableType = 'Pascal'
my_variable_type = 'Snake'



### 변수 할당
# 한줄에서 여러개의 변수에 할당할 수 있음
x, y, z = 1, 2, 3

x = y = z = 4

numbers = [1, 2, 3]
x, y, z = numbers


### 변수 출력
# print() 함수를 사용하여 변수를 출력할 수 있음
x = '파이썬 재밌당'
print(x) # "파이썬 재밌당"

x = '파이썬'
y = '재밌당'
print(x,y) # 쉼표를 기준으로 나뉘어서 출력됨 "파이썬 재밌당"

# print()에서는 연산도 가능함
x = 5
y = 5
print(x+y) # 10

# 하지만 자바스크립트와는 다르게 print()안에 변수의 자료형이 다른 경우 에러가 발생함
y= 'Ryan'
#print(x+y) # TypeError: unsupported operand type(s) for +: 'int' and 'str'


### 전역 변수
# 함수나 코드블럭 밖에서 선언된 변수를 전역 변수라고 지칭함
# 전역변수는 어디에서나 사용 가능

SECRET_KEY = "base64:encoded python_1234"

def what_is_secret_key():
    print('secret key is ' + SECRET_KEY)

what_is_secret_key()

# 만약 함수내에 같은 변수에 다른 값을 재할당하게 된다면 함수내에 있는 값을 사용하게 됨

def wut_is_secret_key():
    SECRET_KEY = 'JAVA and Spring Boot'
    print('secret key is ' + SECRET_KEY)

wut_is_secret_key()


### 글로벌 키워드
# 만약 함수내에 변수를 생성했고, 해당 함수내의 변수를 전역변수로 사용하고 싶다면 global 키워드를 사용하면됨

def myFunc():
    global g_var
    g_var = "This variables is Global variable"

myFunc()

print(g_var)

# 만약 글로벌 키워드를 사용하여 이미 존재하는 전역변수를 재할당하게 되면 해당 전역 변수의 값도 변경됨
print(SECRET_KEY)
def change_global_variable():
    global SECRET_KEY
    SECRET_KEY = "PYTHON"

change_global_variable()
print(SECRET_KEY)