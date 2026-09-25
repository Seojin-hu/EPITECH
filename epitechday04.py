'''
#task1.1

print(42>12)
print(12 == 12)
print("hello" == "world")
print(218 >= 118)
print("a".upper() == "A")
print(1*2*3*4<=9)
print("z" in "azerty")

print("a" in "azerty")
print("i" in "azerty")


#task1.2

number1 = int(input("Enter a integer: "))

if number1 == 42:
    print("This is correct!")


#task1.3

number2 = int(input("Enter a integer: "))

if number2 % 2 == 0:
    print("This integer is even")
else:
    print("This integer is odd")

    
#task1.4

string1 = input("Enter a string: ")

if string1 == "open sesame":
    print("access granted")
elif string1 == "will you open, you goddamn !@&/":
    print("access fucking granted")
else:
    print("permission denied")
'''

'''
#task1.5

number = int(input("Enter a integer: "))
if number == 42:
    print("a")
elif number <= 21:
    print("b")
elif number % 2 == 0:
    print("c")
elif number / 2 < 21:
    print("d")
elif number % 2 == 1 and number >= 45:
    print("e")
else:
    print("f")
'''

'''
#task1.6
a = 42
b = 41
if a == b:
    print("A and B is the sames")
if b <= a:
    print("B is equal or lower as A")
if b != a:
    print("B is different from A")
'''

'''
#task2.1
for i in range(1, 1001):
    print(i)
'''

'''
#task2.1
i = 1
while i <= 1000:
    print(i)
    i += 1
'''

'''
#task2.2
text = input("Enter a string: ")

result = ""
for character in text:
    result += character * 2

print(result)
'''

'''
#task2.3
i = 10000
while i >= 1:
    if i % 7 == 0:
        print(i)
    i -= 1
'''

'''
#task2.4
for i in range(-30, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
'''

'''
#CHALLENGE
while True:
    n, s = input().split()
    n = int(n)

    if n == 0:
        break
    if n >= 42 or any(c in "aeiouAEIOU" for c in s):
        print(n)
    else:
        print(s)
'''

#task3.1

message = input("Message: ")
key = int(input("Key: "))

alphabet = "abcdefghijklmnopqrstuvwxyz"
result = ""

for c in message:
    if c in alphabet:
        index = alphabet.index(c) + key
        if index >= 26:
            index = index - 26
        result += alphabet[index]
    else:
        result += c

print(result)