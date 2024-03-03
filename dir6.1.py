import os
a = int(input("Vvedite nomer zadaniya:  "))
if a==1:
    path = input("Vvedite put:  ")
    print("Only directories:  ")
    print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
    print("Only files:  ")
    print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
    print("All directories and files:  ")
    print([ name for name in os.listdir(path)])
if a==2:
    path = input("Vvedite put':  ")
    print('Exist:', os.access(path, os.F_OK))
    print('Readable:', os.access(path, os.R_OK))
    print('Writable:', os.access(path, os.W_OK))
    print('Executable:', os.access(path, os.X_OK))
if a==3:
    path = input("Vvedite put':  ")
    print('Exist:', os.access(path, os.F_OK))
    if os.access(path, os.F_OK):
        print("All directories and files:  ")
        print([ name for name in os.listdir(path)]) 
    else:
        print("[]")
if a==4:
    path = input("Vvedite put':  ")
    file = open(path, 'r')
    content = file.read()
    lines = content.split('\n')
    print (str(len(lines))+" lines")
if a==5:
    path = input("Vvedite put:  ")
    list = input("Vvedite list:  ").split()
    with open(path, 'w') as file:
        for i in list:
            file.write("%s\n" % i)
if a==6:
    for i in range(65, 91): #From ASCII table(A-Z)
        filename=chr(i) + ".txt"
        open(filename, 'w')
    print("Done! ")
if a==7:
    path1 = input("Vvedite put1:  ")
    path2 = input("Vvedite put2:  ")
    with open(path1,'r') as first, open(path2,'a') as second:
            for i in first:
                second.write(i)
if a==8:
    path = input("Vvedite put':  ")
    if os.access(path, os.F_OK):
        os.remove(path)
        print("Done! ")
    else: print("File does not exist!")