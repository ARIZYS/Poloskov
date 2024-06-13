# Задание 2. Разработать программу с применением пакета tk, взяв в качестве условия одну
# # любую задачу из ПЗ №№ 2 – 9.

#Условие из пз 3, 2 го задания
#Даны два числа. Вывести большее из них.


import tkinter as tk

def calculate_segments():

    A = int(entry_A.get())
    B = int(entry_B.get())


    if A > B:
        result_var.set(" Число А больше Б " + str(A))
    if B > A:
        result_var.set("Число Б больше А " + str(B))
    if B == A:
        result_var.set("Числа Одинаковы!")



root = tk.Tk()
root.title("Определить Наибольшее число")
root.geometry("400x120")


entry_A_label = tk.Label(root, text="Введите число A:")
entry_A_label.grid(row=0, column=0)
entry_A = tk.Entry(root)
entry_A.grid(row=0, column=1)

entry_B_label = tk.Label(root, text="Введите число B:")
entry_B_label.grid(row=1, column=0)
entry_B = tk.Entry(root)
entry_B.grid(row=1, column=1)


calculate_button = tk.Button(root, text="Определить", command=calculate_segments)
calculate_button.grid(row=2, column=0, columnspan=2)


result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.grid(row=3, column=1, columnspan=2)

root.mainloop()
