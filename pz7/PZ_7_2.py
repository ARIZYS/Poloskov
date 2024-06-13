#2. Дана строка, состоящая из русских слов, разделенных пробелами
# (одним или несколькими). Найти длину самого длинного слова.
def length(input_string):
    words = input_string.split()

    if words:
        max_length = max(len(word) for word in words)
        return max_length
    else:
        print("В строке нет слов.")
        return None


input_str = input("Введите строку из русских слов, разделенных пробелами: ")

result = length(input_str)
print("Длина самого длинного слова:", result)