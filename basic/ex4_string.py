###  문자열
# 파이썬에서 'hello' 와 "hello" 는 동일함
x = 'hello'
y = "hello"
print(x==y) # True

# 문자열을 사용할때, ""를 사용했다면 안에 ''를 사용할 수 있고  반대의 경우도 가능하다. 또는 같은 걸로 사용하고 싶을땐 \를 사용하면 된다.
print("hi! my name is 'Ryan'")
print('hi! my name is "Ryan"')
print("hi! my name is \"Ryan\"")

# 이전 변수 정리할때 적었던 것처럼 """나 '''를 사용하여 여러줄의 개행과 띄어쓰기가 포함된 문자열을 묶을 수 있다
a = """
    Last day, I ate Samgyupsal and specipic part of pork.
    That was Amazing and very delicious.
    Maybe I'll visit again later
    """
b = '''
    Last day, I'm not went my exercise.
    i feel fat
    danm! i'm going to do hard today.
    maybe...?
    '''
print(a)
print(b)


# 파이썬은 문자열을 배열처럼 이용이 가능하다
str1 = "banana"
print(str1[1]) # a

# 그래서 for문을 이용하는것도 가능함
for x in str1:
    print(x);

# 문자열의 길이를 재는것도 비교적 간단하다. len()
print(len(str1)) # 6

# 문자열 상에 어떤것이 포함되어 있는지 찾는 것도 가능. in
txt = "Developer want high technology device for programing"
print("Developer" in txt) # True

if "Developer" in txt:
    print("but, no one buy good stuff for slave!")

# 없는지도 확인 가능. not in 

if "Owner" not in txt:
    print("Owner is Devil. Someday.. We will lose our lives because of excessive workload.")



### Slicing
# 파이썬에서 문자열을 나누는건 자주쓰이는듯함
# 만약 슬라이싱을 잘 못하겠으면 배열로 넣고 생각해보자
# 변수 = "바나나는 맛있다."
# ["바","나","나","는"," ","맛","있","다","."]
a = "dobi is free" # 인덱스는 0 부터 시작함
print(a[2:5]) # bi 

print(a[:5]) # 처음부터 5번째 인덱스 전까지 출력

print(a[2:]) # 2번 인덱스인 b부터 끝까지 출력

print(a[-5:-2]) # 뒤의 free앞의 공백부터 -2 인덱스에 존재하는 e전까지 출력

print(a[-8:-2]) # is앞의 공백부터 free의 e전까지 출력


### 문자열 변환

a = "Wow, amazing!"

print(a.upper()) # 모든 문자 대문자로 변경
print(a.lower()) # 모든 문자 소문자로 변경
print(a.strip()) # 양 옆의 공백 제거
print(a.replace('amazing','awesome')) # 특정 문자 변경
print(a.split(',')) # 특정 문자로 문자열을 나눠 배열 변환

### 문자열 형식
age = 31
# txt = "My name is John, I am " + age  # String 과 Int형은 +연산자로 합칠 수 없음
txt = f"My name is Ryan, I am {age}" # 쓰려면 이런 식으로 변수를 사용하겠다는 명시를 해줘야함
print(txt)
txt = f"My name is Ryan, I am {age:.2f}" # 뒤에 추가적인 설정을 통해 어떠한 형식으로 나타낼지 설정할 수 있음
print(txt)
txt = f"My name is Ryan, I am {age+1}" # 또는 연산을 할 수 있
print(txt)



### 문자열 함수
# capitalize()	    Converts the first character to upper case
# casefold()	    Converts string into lower case
# center()	        Returns a centered string
# count()	        Returns the number of times a specified value occurs in a string
# encode()	        Returns an encoded version of the string
# endswith()	    Returns true if the string ends with the specified value
# expandtabs()	    Sets the tab size of the string
# find()	        Searches the string for a specified value and returns the position of where it was found
# format()	        Formats specified values in a string
# format_map()	    Formats specified values in a string
# index()	        Searches the string for a specified value and returns the position of where it was found
# isalnum()	        Returns True if all characters in the string are alphanumeric
# isalpha()	        Returns True if all characters in the string are in the alphabet
# isascii()	        Returns True if all characters in the string are ascii characters
# isdecimal()	    Returns True if all characters in the string are decimals
# isdigit()	        Returns True if all characters in the string are digits
# isidentifier()    Returns True if the string is an identifier
# islower()	        Returns True if all characters in the string are lower case
# isnumeric()	    Returns True if all characters in the string are numeric
# isprintable()	    Returns True if all characters in the string are printable
# isspace()	        Returns True if all characters in the string are whitespaces
# istitle()	        Returns True if the string follows the rules of a title
# isupper()	        Returns True if all characters in the string are upper case
# join()	        Joins the elements of an iterable to the end of the string
# ljust()	        Returns a left justified version of the string
# lower()	        Converts a string into lower case
# lstrip()	        Returns a left trim version of the string
# maketrans()	    Returns a translation table to be used in translations
# partition()	    Returns a tuple where the string is parted into three parts
# replace()	        Returns a string where a specified value is replaced with a specified value
# rfind()	        Searches the string for a specified value and returns the last position of where it was found
# rindex()	        Searches the string for a specified value and returns the last position of where it was found
# rjust()	        Returns a right justified version of the string
# rpartition()	    Returns a tuple where the string is parted into three parts
# rsplit()	        Splits the string at the specified separator, and returns a list
# rstrip()	        Returns a right trim version of the string
# split()	        Splits the string at the specified separator, and returns a list
# splitlines()	    Splits the string at line breaks and returns a list
# startswith()	    Returns true if the string starts with the specified value
# strip()	        Returns a trimmed version of the string
# swapcase()	    Swaps cases, lower case becomes upper case and vice versa
# title()	        Converts the first character of each word to upper case
# translate()	    Returns a translated string
# upper()	        Converts a string into upper case
# zfill()	        Fills the string with a specified number of 0 values at the beginning