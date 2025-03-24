import sympy as sp
import numpy as np
x = sp.symbols('x')

# --- Пример функции ---
f_expr = x**5 + 2*x**4 - 5*x**3 + 8*x**2 - 7*x - 3
f = sp.lambdify(x, f_expr, modules='numpy')
f_prime2 = sp.lambdify(x, sp.diff(f_expr, x, 2), modules='numpy')

# --- Метод хорд ---
def chord_method(f, f_prime2, a, b, eps=1e-5, max_iter=100):
    if f(a) * f(b) > 0:
        raise ValueError("Function must change sign on [a, b]")
    if f_prime2((a + b)/2) > 0:
        fixed = a if f(a) < 0 else b
    else:
        fixed = b if f(b) < 0 else a

    x_old = b if fixed == a else a
    for i in range(max_iter):
        x_new = x_old - f(x_old) * (fixed - x_old) / (f(fixed) - f(x_old))
        if abs(f(x_new)) < eps:
            return x_new, i + 1
        x_old = x_new
    return x_new, max_iter

# --- Теорема Декарта ---
def descartes_signs(coeffs):
    signs = np.sign(coeffs)
    changes = sum(signs[i] != 0 and signs[i] != signs[i+1]
                  for i in range(len(signs)-1))
    return changes

# --- Теорема о сопряжённости ---
def has_real_root_if_odd_degree(coeffs):
    return len(coeffs) % 2 == 1

# --- Теорема об оценке модуля корней ---
def max_modulus_bound(coeffs):
    an = coeffs[0]
    A = max(abs(c) for c in coeffs[1:])
    return 1 + A / abs(an)

# --- Теорема Лагранжа ---
def lagrange_bound(coeffs):
    an = coeffs[0]
    for k, a_k in enumerate(coeffs[1:], 1):
        if a_k < 0:
            return 1 + (abs(a_k) / an)**(1 / k)
    return None

# --- Теорема о верхних/нижних границах корней ---
def reciprocal_polynomial(coeffs):
    n = len(coeffs) - 1
    return [coeffs[n - i] for i in range(n + 1)]

def bounds_of_roots(coeffs):
    pos_upper = lagrange_bound(coeffs)
    reciprocal = reciprocal_polynomial(coeffs)
    pos_lower = 1 / lagrange_bound(reciprocal)
    return pos_lower, pos_upper

# --- Пример запуска ---
if __name__ == "__main__":
    coeffs = [1, 2, -5, 8, -7, -3]
    a, b = 1, 2
    root, iterations = chord_method(f, f_prime2, a, b)
    print(f"Метод хорд: корень ≈ {root:.6f}, итераций: {iterations}")

    print(f"Теорема Декарта: максимум положительных корней = {descartes_signs(coeffs)}")
    print(f"Сопряжённость: {'гарантирован действ. корень' if has_real_root_if_odd_degree(coeffs) else 'может быть только комплексные'}")
    print(f"Оценка |x| ≤ {max_modulus_bound(coeffs):.4f}")
    print(f"Лагранж (положит. корни): R ≤ {lagrange_bound(coeffs):.4f}")
    pos_lower, pos_upper = bounds_of_roots(coeffs)
    print(f"Положительные корни: {pos_lower:.4f} ≤ x ≤ {pos_upper:.4f}")