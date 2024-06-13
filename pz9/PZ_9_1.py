#Дана строка 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16', отражающая продажи продукции
#по дням в кг. Преобразовать информацию из строки в словари, с использованием функции найти
#максимальные продажи по каждому виду продукции, результаты вывести на экран.
sales_string = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'


words = sales_string.split()


sales_data = {}


current_product = None
for word in words:
    if word.isdigit():
        if current_product is not None:
            sales_data[current_product].append(int(word))
    else:
        current_product = word
        sales_data[current_product] = []


max_sales = {}
for product, sales in sales_data.items():
    max_sales[product] = max(sales)


for product, max_sale in max_sales.items():
    print(f'Максимальные продажи для {product}: {max_sale} кг')
