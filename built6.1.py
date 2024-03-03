from time import sleep
import math
a = int(input("Vvedite nomer zadaniya:  "))
if a==1:
    list = []
    x = input("Vvedite elementy massiva:   ").split()
    n = len(x)
    for i in range(n):
        list.append(int(x[i]))
    result = 1
    for num in list:
        result *= num
    print("list: " + str(list))
    print("umnozhenie: ", result)
if a==2:
    word = input("Vvedite slovo:  ")
    upper = 0
    lower = 0
    for i in word:
        if i.isupper():
            upper +=1
        elif i.islower(): 
            lower +=1
    print("Lowercase:  " + str(lower))
    print("Uppercase:  "+ str(upper))
if a==3:
    word = input("Vvedite slovo:  ")
    n = len(word)
    for i in range(n-1):
        if word[i] == word[n-1-i]:
            ans = "Palindrome"
        else:
            ans = "Not Palindrome"
    print(ans)
if a==4:
    n = int(input("Vvedite chislo:  "))
    t = int(input("Vvedite vremya ozhidaniya:   "))
    sleep(t/1000)
    s = math.sqrt(n)
    print("Square root of ", n, " after ", t, " miliseconds is ", s)
if a==5:
    list = []
    t = "True"
    x = input("Vvedite elementy massiva:   ").split()
    n = len(x)
    for i in range(n):
        list.append(x[i])
    for i in list:
        if i == "True":
            continue
        else:
            t = 'False'
    print(t)