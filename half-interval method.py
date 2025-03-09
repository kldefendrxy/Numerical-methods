arr = [5, 0, 1, 0, 2, 3]  # Коэффициенты многочлена
x0, x1 = -100, 100  # Начальный интервал
e = 10 ** -2  # Точность

def poly(x, coeffs):
    # Вычисляет значение многочлена в точке x
    return sum(coeffs[i] * x ** i for i in range(len(coeffs)))

def half_interval(x0, x1, arr, e=10 ** -2):
    func0 = poly(x0, arr)
    func1 = poly(x1, arr)

    if func0 * func1 > 0:
        print('Выберите другое начальное приближение')
        return None

    while abs(x1 - x0) > e:
        x2 = (x0 + x1) / 2
        func2 = poly(x2, arr)

        if func0 * func2 < 0:
            x1 = x2
        else:
            x0 = x2
            func0 = func2  # Обновляем значение f(x0)

        print(f"x0: {x0}, x1: {x1}")

    return (x0 + x1) / 2  # Возвращаем середину отрезка как приближённый корень

root = half_interval(2.5, 4, [6, -5, 1], e)
print(f"Найденный корень: {root}")