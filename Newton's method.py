import sympy as sp


# Функция для вычисления многочлена
def func_init(x, coeffs):
    return sum(float(coeffs[i]) * x ** i for i in range(len(coeffs)))


# Функция для вычисления производной многочлена
def deriv(x_n, coeffs):
    x = sp.Symbol('x')
    df_dx = sp.diff(sum(coeffs[i] * x ** i for i in range(len(coeffs))), x)  # Символьная производная
    return float(df_dx.subs(x, x_n))  # Преобразуем в float, чтобы избежать проблем с дробями


# Метод Ньютона
def newtons_method(x0, arr, e=1e-6, max_iter=100):
    x_n = float(x0)  # Начальное приближение (делаем float, чтобы избежать дробей SymPy)

    for i in range(max_iter):
        func = func_init(x_n, arr)  # Значение функции
        dfunc = deriv(x_n, arr)  # Значение производной

        if abs(dfunc) < 1e-10:  # Проверка на деление на 0
            print("Производная слишком мала, метод не работает.")
            return None

        x_next = x_n - func / dfunc  # Формула метода Ньютона

        # Критерий останова: относительное изменение x_n
        stopping_criteria = abs(x_next - x_n) / max(1, abs(x_next))

        print(f"Итерация {i + 1}: x_n = {x_n:.6f}, x_next = {x_next:.6f}, f(x_n) = {func:.6f}, f'(x_n) = {dfunc:.6f}")

        if stopping_criteria < e:  # Проверка выхода
            return x_next  # Возвращаем найденный корень

        x_n = x_next  # Обновляем текущее приближение

    print("Метод не сошелся за", max_iter, "итераций")
    return None


# Тестируем метод Ньютона на уравнении x**2 - 5*x + 6 = 0 (корни 2 и 3)
root = newtons_method(4, [6, -5, 1], e=1e-6)
print(f"Найденный корень: {root:.6f}")