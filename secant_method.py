import sympy as sp

# Функция для вычисления значения многочлена
def func_init(x, coeffs):
    return sum(float(coeffs[i]) * x ** i for i in range(len(coeffs)))

# Метод секущих
def secant_method(x0, x1, arr, e=1e-6, max_iter=100):
    x_n_0 = float(x0)  # Первое начальное приближение
    x_n = float(x1)  # Второе начальное приближение

    for i in range(max_iter):
        func_x_n = func_init(x_n, arr)  # f(x_n)
        func_x_n_0 = func_init(x_n_0, arr)  # f(x_n_0)

        if func_x_n - func_x_n_0 == 0:  # Проверка деления на ноль
            print("Ошибка: деление на ноль. Метод не сходится.")
            return None

        # Формула метода секущих
        x_next = x_n - (func_x_n * (x_n - x_n_0)) / (func_x_n - func_x_n_0)

        # Критерий остановки: относительное изменение
        stopping_criteria = abs(x_next - x_n) / max(1, abs(x_next))

        print(f"Итерация {i + 1}: x_n = {x_n:.6f}, x_next = {x_next:.6f}, f(x_n) = {func_x_n:.6f}")

        if stopping_criteria < e:  # Проверка точности
            return x_next  # Возвращаем найденный корень

        x_n_0, x_n = x_n, x_next  # Обновляем приближения

    print("Метод не сошелся за", max_iter, "итераций")
    return None

# Тестируем метод секущих на уравнении x**2 - 5*x + 6 = 0 (корни 2 и 3)
root = secant_method(5, 4, [6, -5, 1], e=1e-6)
print(f"Найденный корень: {root:.6f}")