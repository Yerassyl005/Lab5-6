import re
#  Напишите программу Python, которая соответствует строке, которая имеет 'a', за которой следует ноль или более 'b'.

first = re.compile(r"ab*")

# Напишите программу Python, которая соответствует строке, которая имеет 'a', за которой следуют от двух до трех 'b'.

second = re.compile(r"ab{2,3}")

# Напишите программу Python, чтобы найти последовательности строчных букв, соединенных с подчеркиванием.

third = re.compile(r"[a-z]+\_")

#Напишите программу Python, чтобы найти последовательности одной заглавной буквы, за которой следуют строчные буквы.

fourth = re.compile(r"[A-Z]{1}[a-z]+")

# Напишите программу на Python, которая соответствует строке, в которой есть 'a', за которой следует что-либо, заканчивающееся на 'b'.

fifth = re.compile(r"a.+b\Z")

# Напишите программу Python, чтобы заменить все вхождения пробела, запятой или точки двоеточием.

sixth = re.compile(r"[ ,.]")


# Напишите программу python для преобразования строки регистра змеи в строку регистра верблюда.

def snakeToCamel(text):
    camelCase=""
    pattern = re.compile(r"[_]")
    words=pattern.split(text)
    for i, word in enumerate(words):
        if i != 0:
            camelCase+=word.capitalize()
        else: 
            camelCase += word
    return camelCase



# Напишите программу Python, чтобы разделить строку на прописные буквы.
def modify(text):
    res = ""
    pattern = re.compile(r"[A-Z][a-z]+")
    words = pattern.findall(text)
    for i, word in enumerate(words):
        if i != 0:  
            res += " " + word
        else:
            res += word
    return res


#Напишите программу на Python, чтобы вставить пробелы между словами, начинающиеся с заглавных букв.
def spaces(text):
    res = ""
    pattern = re.compile(r"[A-Z][a-z]+")
    words = pattern.findall(text)
    for i, word in enumerate(words):
        if i != 0:
            res += " " + word
        else:
            res += word
    return res

#  Напишите программу Python для преобразования данной строки верблюжьего регистра в змеиный регистр.
def camel_to_snake(text):
    res = ""
    pattern = re.compile(r"[A-Z][a-z]+")
    words = pattern.findall(text)
    for i, word in enumerate(words):
        if i == 0:
            res += word.casefold()
        else:
            res += "_" + word.casefold()
    return res


def main():
    print("1 пример")
    print(first.search("fdskfldkflddsdsab"))
    print(" ")

    print("2 пример")
    print(second.search("gjdfkabbbbfkkliu"))
    print(" ")

    print("3 пример")
    print(third.findall("fdsfd_ fdjskfjdsk_ fdsf4ds_"))
    print(" ")

    print("4 пример")
    print(fourth.findall("Ffdsf GGfgrhr ImknkJtr"))
    print(" ")

    print("5 пример")
    print(fifth.search("kktngtag423b"))
    print(fifth.search("fjdjgfdb"))
    print(fifth.search("fdifafgnjgr3"))
    print(" ")

    print("6 пример")
    text = "gfdjf,fhdsjh..fdskjf fjhgerj,. fds"
    print(sixth.sub(":", text))
    print(" ")

    print("7 пример")

    print(snakeToCamel("hello_world_wordle"))
    print(" ")

    print("8 пример")
    print(modify("OneTwoThree"))
    print(" ")
    
    print("9 пример")
    print(spaces("HelloWordlOneMoreTime"))
    print(" ")

    print("10 пример")
    print(camel_to_snake("SnakeCaseVar"))





if __name__ == "__main__":
    main()