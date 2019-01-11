from math import *
from scipy.misc import derivative

#1
#interval1 = [-inf, inf]
filepath1 = 'data/(task1)prost_iter.txt'

#2
#interval2 = [-5.0, 5.0]
filepath21 = 'data/(task2.1)podil_navpil.txt'
filepath22 = 'data/(task2.1)metod_sichnykh.txt'

#3
coefs = [-48, -29, 724, -657, -772, 726, -25, -12]
# coefs = [1, 8, 13, -12, -9]
filepath3 = 'data/(task3)lobachevskyy.txt'

def eq1(x):
    return pi*cosh(x) * sin(pi*x) + x**2 - 5*sinh(x)*cos(x)

def eq2(x):
    return pow(x, 3) - 7 * sin(pi * x) + cos(pi * log2(5 * pi)) - 3 * x

def eq3(x, coefs=coefs):
    sum = 0
    for it in range(len(coefs)):
        sum += coefs[it] * pow(x, len(coefs) - it - 1)
    return sum

class EquationProcessor:

    def __init__(self, precision, equation, filepath):
        self.precision = precision
        self.func = equation
        self.fs = open(filepath, "w")
#TODO
    # Завдання 1: метод простих ітерацій ()
    def simple_iteration_method(self, interval):
        a = interval[0]
        b = interval[1]
        alpha = min(derivative(self.func, a, dx=1e-6), derivative(self.func, b, dx=1e-6))
        gamma = max(derivative(self.func, a, dx=1e-6), derivative(self.func, b, dx=1e-6))
        _lambda = 2/(alpha + gamma)
        q = (gamma - alpha)/(gamma + alpha)
        print("q= " + str(q))

        if q < 0.5:
            epsilon = self.precision
        else: epsilon = (1-q)*self.precision/q
        x_k = a
        self.fs.write(str(x_k) + "\n")
        x_k_next = x_k - _lambda * self.func(x_k)
        while abs(x_k_next - x_k) > epsilon and x_k_next != x_k:
            self.fs.write(str(x_k_next) + "\n")
            x_k = x_k_next
            x_k_next = x_k - _lambda*self.func(x_k)

        self.fs.write("result: " + str(x_k_next) + "\n")
        return x_k_next

    # Завдання 2.1: метод поділу навпіл ()
    def division_method(self, interval):
        x = (interval[0] + interval[1]) / 2
        self.fs.write("divided:" + str(x) + "\n")
        if abs(interval[1] - interval[0]) >= self.precision:
            interval[0], interval[1] = (interval[0], x) \
                if self.func(interval[0]) * self.func(x) < 0 \
                else (x, interval[1])
            self.fs.write("interval:" + str(interval) + "\n")
            return self.bisection_method(interval)
        else:
            self.fs.write("RESULT:" + str(x) + "\n")
            return x

    # Завдання 2.2: метод січних ()
    def secant_method(self, interval):
        x_k_prev = interval[1]
        x_k = interval[0]
        x_next = 0
        while abs(x_k_prev - x_k) >= self.precision:
            self.fs.write(str(x_k_prev) + "\n")
            x_next = x_k - (x_k - x_k_prev) * (self.func(x_k)) / (self.func(x_k) - self.func(x_k_prev))
            x_k_prev = x_k
            x_k = x_next
        self.fs.write("result" + str(x_next) + "\n")
        return x_next

#Завдання 3: метод Лобачевського
    def lobachevskyy_method(self, coefs):
        p = 0
        a = list(reversed(coefs))
        while True:
            p += 1
            b = self.iter_formula(a)
            if self.stop_criterion(b, a) < self.precision or p == 7:
                break
            a = b
        n = len(a)
        res = [0] * (n-1)
        print(p)
        for k in range(1, n):
            res[k - 1] = pow(b[n - k - 1] / b[n - k], pow(2, -p))
        # return self.find_roots(res)
        roots = []
        for value in res:
            if min(abs(self.func(value)), abs(self.func(-value))) == abs(self.func(value)):
                roots.append(value)
            else: roots.append(-value)
        for r in sorted(roots): self.fs.write(str(r) + "\n")
        return roots

    @staticmethod
    def stop_criterion(b, a):
        s = 0
        for k in range(0, len(a)):
            s += (1 - b[k] / (a[k] ** 2)) ** 2
        return pow(s, 1 / 2)

    @staticmethod
    def iter_formula(a):
        n = len(a)
        b = [0] * n
        for k in range(0, n):
            b[k] = a[k] ** 2
            for j in range(1, n-k+1):
                if k - j >= 0 and k + j < n:
                    b[k] += 2 * ((-1) ** j) * a[k - j] * a[k + j]
        return b

    def clarify_roots_by_Newton_method(self, roots):
        clarified_roots = []
        for k in sorted(roots):
            x_prev = k
            x_next = x_prev - self.func(x_prev) / derivative(self.func, x_prev, dx=1e-6)
            while abs(self.func(x_next)-self.func(x_prev)) >= self.precision:
                x_prev = x_next
                x_next = x_prev - self.func(x_prev) / derivative(self.func, x_prev, dx=1e-6)
            clarified_roots.append(x_next)
        self.fs.write("\n clarified roots \n")
        for r in clarified_roots: self.fs.write(str(r)+ "\n")
