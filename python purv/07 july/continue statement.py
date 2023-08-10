no=int(input("Enter a number:"))
number =[23,7,15,12,30]

for i in number:
    if i == no:
        print("Number Found in list",i)
        continue
else:
    print("Number Not Found in list")
