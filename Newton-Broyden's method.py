import numpy as np

# Функция для вычисления многочлена
def func_init(x, coeffs):
    return sum(float(coeffs[i]) * x ** i for i in range(len(coeffs)))

# Метод Ньютона-Бройдена (одномерный случай)
def broyden_method(x0, coeffs, e=1e-6, max_iter=100):
    x_n = float(x0)  # Начальное приближение
    f_n = func_init(x_n, coeffs)

    # Начальное приближение производной (численное вычисление)
    delta = 1e-5
    df_n = (func_init(x_n + delta, coeffs) - f_n) / delta
    if abs(df_n) < 1e-10:
        print("Производная слишком мала, метод не работает.")
        return None

    B_n = 1 / df_n  # начальное приближение обратной производной

    for i in range(max_iter):
        # Вычисляем следующее приближение
        x_next = x_n - B_n * f_n
        f_next = func_init(x_next, coeffs)

        # Критерий останова
        stopping_criteria = abs(x_next - x_n) / max(1, abs(x_next))

        print(f"Итерация {i + 1}: x_n = {x_n:.6f}, x_next = {x_next:.6f}, f(x_n) = {f_n:.6f}, B_n = {B_n:.6f}")

        if stopping_criteria < e:
            return x_next

        # Обновляем B_n по формуле Бройдена
        y_n = f_next - f_n
        s_n = x_next - x_n

        if abs(s_n) < 1e-12:
            print("s_n слишком мал, метод может не сходиться.")
            return None

        # Одномерная формула Бройдена для обновления обратной производной
        B_n = B_n + ((s_n - B_n * y_n) * s_n) / (s_n * B_n * y_n)

        # Подготавливаемся к следующей итерации
        x_n, f_n = x_next, f_next

    print("Метод не сошелся за", max_iter, "итераций")
    return None

# Тестируем метод Ньютона-Бройдена на уравнении x**2 - 5*x + 6 = 0 (корни 2 и 3)
root = broyden_method(4, [6, -5, 1], e=1e-6)
print(f"Найденный корень: {root:.6f}")