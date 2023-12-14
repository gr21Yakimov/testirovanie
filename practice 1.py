import tkinter as tk
from tkinter import messagebox

def check_triangle_type(a, b, c):
    if a == b == c:
        return "Равносторонний"
    elif a == b or b == c or c == a:
        return "Равнобедренный"
    else:
        return "Разносторонний"

def check_triangle_existence(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False

def check_right_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()
    return sides[0]**2 + sides[1]**2 == sides[2]**2

def check_acute_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()
    return sides[0]**2 + sides[1]**2 > sides[2]**2

def check_obtuse_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()
    return sides[0]**2 + sides[1]**2 < sides[2]**2

def check_sum_of_sides(a, b, c):
    sorted_sides = sorted([a, b, c])
    return sorted_sides[0] + sorted_sides[1] > sorted_sides[2]

def calculate_triangle_type():
    try:
        side1 = float(entry_side1.get())
        side2 = float(entry_side2.get())
        side3 = float(entry_side3.get())

        if side1 == side2 == side3 == 1:
            messagebox.showerror("Ошибка", "Треугольник с такими сторонами не существует.")
            return

        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            messagebox.showerror("Ошибка", "Все стороны треугольника должны быть положительными числами.")
            return

        if not check_triangle_existence(side1, side2, side3):
            messagebox.showerror("Ошибка", "Треугольник с такими сторонами не существует.")
            return

        if not check_sum_of_sides(side1, side2, side3):
            messagebox.showerror("Ошибка", "Сумма двух меньших сторон короче большей стороны. Такой треугольник не существует.")
            return

        triangle_type = check_triangle_type(side1, side2, side3)

        if check_right_triangle(side1, side2, side3):
            triangle_type += " и прямоугольный"
        elif check_acute_triangle(side1, side2, side3):
            triangle_type += " и остроугольный"
        elif check_obtuse_triangle(side1, side2, side3):
            triangle_type += " и тупоугольный"

        messagebox.showinfo("Результат", f"Тип треугольника: {triangle_type}")

    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите числовые значения для сторон треугольника.")

def clear_entries():
    entry_side1.delete(0, tk.END)
    entry_side2.delete(0, tk.END)
    entry_side3.delete(0, tk.END)

# GUI
root = tk.Tk()
root.title("Определение типа треугольника")

label_side1 = tk.Label(root, text="Сторона 1:")
label_side1.grid(row=0, column=0)
entry_side1 = tk.Entry(root)
entry_side1.grid(row=0, column=1)

label_side2 = tk.Label(root, text="Сторона 2:")
label_side2.grid(row=1, column=0)
entry_side2 = tk.Entry(root)
entry_side2.grid(row=1, column=1)

label_side3 = tk.Label(root, text="Сторона 3:")
label_side3.grid(row=2, column=0)
entry_side3 = tk.Entry(root)
entry_side3.grid(row=2, column=1)

calculate_button = tk.Button(root, text="Определить тип треугольника", command=calculate_triangle_type)
calculate_button.grid(row=3, column=0, columnspan=2)

clear_button = tk.Button(root, text="Очистить", command=clear_entries)
clear_button.grid(row=4, column=0, columnspan=2)

root.mainloop()
