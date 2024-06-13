#Из заданной строки отобразить только символы пунктуации. Использовать
#библиотеку string.
#cтрока: --msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"
import string

строка = '--msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}'

simbol_p = ''.join(filter(lambda char: char in string.punctuation, строка))

print('Символы пунктуац ии:', simbol_p)