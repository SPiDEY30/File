#1
#for i in range(1,11):
#    print(i)


#2
#sum_of_numbers = 0
#for i in range(1,11):
#    sum_of_numbers += i
#print(sum_of_numbers)


#3
#for i in range(2,21,2):
#    print(i)



#4
#factorial = 1
#for i in range(1,6):
#    factorial *= i
#print(factorial)


#5
#fibonacci_numbers = [0, 1]
#for i in range(2, 11):
 #   fibonacci_numbers.append(fibonacci_numbers[i - 1] +
#fibonacci_numbers[i - 2])
#print(fibonacci_numbers)



#6
#prime_numbers=[]
#for i in range(2, 101):
#    is_prime = True
#    for j in range(2, int(i ** 0.5) + 1):
 #       if i % j == 0:
 #           is_prime = False
#            break
#    if is_prime:
#        prime_numbers.append(i)
#print(prime_numbers)



#7
#for i in range(32, 127):
#    print(chr(i), end="")


#8
#string = "hello world"
#reversed_string = ""
#for i in range(len(string) - 1, -1, -1):
#    reversed_string += string[i]
#print(reversed_string)



#9
#def is_palindrome(number):
#    string = str(number)
#    reversed_string = ""
#    for i in range(len(string) - 1, -1, -1):
#        reversed_string += string[i]
#    return string == reversed_string

#number = 121
#print(is_palindrome(number))



#10
#letters = ("abcdefghijklmnopqrstuvwxyz")
#for i in letters:
#    for j in letters:
 #       print(i, j)



#11
#fibonacci_numbers = [0, 1]
#for i in range(2, 11):
 #   fibonacci_numbers.append(fibonacci_numbers[i - 1] +
#fibonacci_numbers[i - 2])
#    if (fibonacci_numbers[i] % 2 == 0):
 #       print(fibonacci_numbers[i])




#12
#prime_numbers = []
#for i in range(101, 201):
#    is_prime = True
#    for j in range(2, int(i ** 0.5) + 1):
 #       if i % j == 0:
#            is_prime = False
 #           break
 #   if is_prime:
#        prime_numbers.append(i)
#print(prime_numbers[:10])


#13
fibonacci_numbers = [0, 1]
for i in range(2, 10):
    fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
    print(fibonacci_numbers)

 
 

