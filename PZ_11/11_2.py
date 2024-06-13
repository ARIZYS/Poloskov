#2. Из предложенного текстового файла (text18-22.txt) вывести на экран его содержимое,
#количество букв в верхнем регистре. Сформировать новый файл, в который поместить текст
#в стихотворной форме предварительно заменив символы третей строки их числовыми
#кодами

with open('text18-22.txt', 'r', encoding='utf-16') as file:
    text = file.read()


print("Содержимое файла:")
print(text)


uppercase_count = sum(1 for char in text if char.isupper())
print("\nКоличество букв в верхнем регистре:", uppercase_count)


lines = text.splitlines()


modified_third_line = ''.join(str(ord(char)) for char in lines[2])
lines[2] = modified_third_line


poem = '\n'.join(lines)


with open('poem.txt', 'w', encoding='utf-8') as new_file:
    new_file.write(poem)

print("\nТекст в стихотворной форме с измененной третьей строкой успешно записан в файл 'poem.txt'")


