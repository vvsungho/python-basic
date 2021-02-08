

# hello.py


print ("Hello Word")


naver = 601000

print(naver)

myString = "Hello World"

# 이상, 미만
print(len(myString))

print(myString[6:11])

print(myString[6:])
print(myString[:5]) # 처음부터 [5] 번쨔 전까지 (미만)

print(myString[6: -2])  # [6]번째 부터 끝에서 2자리 빼고 출력


str = "hello world"

arr = str.split(" ")

print(arr)

print(type(70000))

# 연습문제 2-1, 2-2
daum = 89000
naver = 751000
sum = (daum * 100 * 0.95 + naver * 20 * 0.9)
print(sum)

# 연습문제 2-3
f = 50
c = (f-32) / 1.8
print(c)

# 연습문제 2-4
print("pizza \n" * 10)

# 연습문제 2-5
print(1000000 * 0.70 * 0.7 * 0.7)

# 연습문제 2-7
s = "Daum KaKao"
s = s[5:] + ' ' + s[:4]
print(s)

# 연습문제 2-8
a = "hello world"
a = 'hi ' + a[6:]
print(a)

# 연습문제 2-9
x = "abcdef"
x = x[1:5] + x[5:] + x[:1]
print(x)




