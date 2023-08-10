print("08_Purv Parmar")
#1
#for i in range(1, 21):
#    if i % 2 == 0:
#        print(i)
#        break

#2
#i = 1
#while i <= 10:
#    if i % 5 != 0:
#        i += 1
#        continue
#    print(i)
#    i += 1

#3
#for i in range(1, 11):
#    if i % 2 == 0:
#        pass
#    else:
#        print(i)

#4
#str = "Python"
#for i in str:
#    if i == "h":
#        break
#    print(i)


#5
#str = "Python"
#for i in str:
#    if i == "h":
#        continue
#    print(i)


#6
#i = 1
#while i <= 10:
#    if i % 2 == 0:
#        print(i)
#    i += 1
#    if i % 5 == 0:
#        continue



#7
#str = "Python"
#for i in str:
#    if i == "h":
#        break
#    elif i == "o":
#        continue
#    else:
#        print(i)

#8
#i = 1
#while i <= 10:
#    j = 1
#    while j <= 2:
#        if i % 2 == 0:
#            print(i)
#            break
#        j += 1
#    i += 1

#9
#i = 1
#while i <= 10:
#    j = 1
#    while j <= 2:
#        if i % 5 != 0:
#            j += 1
#            continue
#        print(i)
#        j += 1
#    i += 1


#10
#i = 1
#while i <= 10:
#    j = 1
#    while j <= 2:
#        if i % 2 == 0:
#            j += 1
#            pass
#        else:
#            print(i)
#            j += 1
#    i += 1


#11
#str = "Python"
#i = 0
#while i < len(str):
#    j = 0
#    while j < 2:
#        if str[i] == "h":
#            break
#        elif str[i] == "o":
#            continue
#        else:
#            print(str[i])
#            j += 1
#    i += 1

#12
str = "Python"
i = 0
while i < len(str):
    j = 0
    while j < 2:
        if str[i] == "h":
            j += 1
            continue
        elif str[i] == "o":
            break
        else:
            print(str[i])
            j += 1
    i += 1



