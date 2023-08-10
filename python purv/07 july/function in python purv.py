print("08_Purv parmar")
#1
#def hello_world():
 #print("Hello, world!")

#hello_world()

#2
#def factorial(n):
# if n == 0:
#  return 1
# else:
#  return n * factorial(n - 1)

#print(factorial(5))


#3
#def is_even(n):
# if n % 2 == 0:
#  return True
# else:
#  return False

#print(is_even(10))


#4
#import math

#def square_root(n):
# return math.sqrt(n)

#print(square_root(16))



#5
#def to_uppercase(string):
# return string.upper()

#print(to_uppercase("hello"))




#6
#def is_palindrome(string):
# reversed_string = ""
# for character in string:
#  reversed_string = character + reversed_string
# if reversed_string == string:
#  return True
# else:
#  return False

#print(is_palindrome("racecar"))


#7
#def find_longest_word(words):
# longest_word = ""
# for word in words:
#  if len(word) > len(longest_word):
#   longest_word = word
# return longest_word

#print(find_longest_word(["hello", "world", "this", "is", "a", "list"]))


#8
#def fibonacci(n):
# if n == 0:
#  return 0
# elif n == 1:
#  return 1
# else:
#  return fibonacci(n - 1) + fibonacci(n - 2)

#print(fibonacci(10))


#9
#import random

#def generate_random_number():
# return random.randint(0, 100)

#print(generate_random_number())


#10
#import time

#def print_current_time():
# print(time.strftime("%H:%M:%S"))

#print_current_time()


#11
#def read_file(filename):
# with open(filename, "r") as f:
#  contents = f.read()
# return contents

#print(read_file("my_file.txt"))


#12
def write_to_file(filename, contents):
 with open(filename, "w") as f:
  f.write(contents)

write_to_file("my_file.txt", "This is my file.")











