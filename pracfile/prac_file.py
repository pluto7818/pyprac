# ============================================================
#   Department of Operational Research, University of Delhi
#   Python Lab Programs — All 30 Practicals in One File
# ============================================================

import math
import random
import csv
import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import poisson
from pulp import *
import scipy.optimize as opt


# ─────────────────────────────────────────────
#  HELPER: Menu runner
# ─────────────────────────────────────────────
def run_menu(title, options):
    """Display a numbered menu and return the user's integer choice."""
    print(f"\n{'='*45}")
    print(f"  {title}")
    print(f"{'='*45}")
    for i, opt_text in enumerate(options, 1):
        print(f"  {i}. {opt_text}")
    print(f"{'='*45}")
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(options):
                return choice
            print(f"Please enter a number between 1 and {len(options)}.")
        except ValueError:
            print("Invalid input. Enter a number.")


# ─────────────────────────────────────────────
#  PROGRAM 1 — Hello, Name
# ─────────────────────────────────────────────
def program_01():
    """Enter name and display as 'Hello, Name'."""
    print("\n--- Program 1: Hello, Name ---")
    name = input("Enter your name: ")
    print(f'Hello, {name}')


# ─────────────────────────────────────────────
#  PROGRAM 2 — Arithmetic Operations (menu)
# ─────────────────────────────────────────────
def program_02():
    """Menu-driven arithmetic: +, -, *, /, //, %."""
    print("\n--- Program 2: Arithmetic Operations ---")
    a = float(input("Enter first number : "))
    b = float(input("Enter second number: "))
    ops = {
        1: ("+",  lambda x, y: x + y),
        2: ("-",  lambda x, y: x - y),
        3: ("*",  lambda x, y: x * y),
        4: ("/",  lambda x, y: x / y if y != 0 else "Undefined (div by 0)"),
        5: ("//", lambda x, y: x // y if y != 0 else "Undefined (div by 0)"),
        6: ("%",  lambda x, y: x % y if y != 0 else "Undefined (div by 0)"),
    }
    choice = run_menu("Arithmetic Menu", [f"a {sym} b" for sym, _ in ops.values()])
    sym, func = ops[choice]
    result = func(a, b)
    print(f"Result: {a} {sym} {b} = {result}")


# ─────────────────────────────────────────────
#  PROGRAM 3 — Roots of a Quadratic Equation
# ─────────────────────────────────────────────
def program_03():
    """Compute roots of ax² + bx + c = 0."""
    print("\n--- Program 3: Roots of a Quadratic Equation ---")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    if a == 0:
        print("Not a quadratic equation (a cannot be 0).")
        return
    disc = b ** 2 - 4 * a * c
    if disc > 0:
        r1 = (-b + math.sqrt(disc)) / (2 * a)
        r2 = (-b - math.sqrt(disc)) / (2 * a)
        print(f"Two distinct real roots: {r1:.4f} and {r2:.4f}")
    elif disc == 0:
        r = -b / (2 * a)
        print(f"One repeated real root: {r:.4f}")
    else:
        real = -b / (2 * a)
        imag = math.sqrt(-disc) / (2 * a)
        print(f"Complex roots: {real:.4f} + {imag:.4f}i  and  {real:.4f} - {imag:.4f}i")


# ─────────────────────────────────────────────
#  PROGRAM 4 — Reverse Number & Sum of Digits (menu)
# ─────────────────────────────────────────────
def program_04():
    """Menu-driven: reverse a number OR find sum of digits."""
    print("\n--- Program 4: Reverse Number / Sum of Digits ---")
    n = input("Enter a number: ").strip()
    choice = run_menu("Choose Operation", ["Reverse the number", "Sum of digits"])

    digits = [ch for ch in n if ch.isdigit()]
    if choice == 1:
        print(f"Reversed: {''.join(reversed(digits))}")
    else:
        total = sum(int(d) for d in digits)
        print(f"Sum of digits: {total}")


# ─────────────────────────────────────────────
#  PROGRAM 5 — Odd / Even / Prime (menu)
# ─────────────────────────────────────────────
def _is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def program_05():
    """Menu-driven: check odd/even OR prime."""
    print("\n--- Program 5: Odd / Even / Prime ---")
    n = int(input("Enter a number: "))
    choice = run_menu("Choose Check", ["Odd or Even", "Prime"])
    if choice == 1:
        print(f"{n} is {'Even' if n % 2 == 0 else 'Odd'}.")
    else:
        print(f"{n} is {'Prime' if _is_prime(n) else 'Not Prime'}.")


# ─────────────────────────────────────────────
#  PROGRAM 6 — Maximum of 3 Numbers
# ─────────────────────────────────────────────
def program_06():
    """Find the maximum of three entered numbers."""
    print("\n--- Program 6: Maximum of 3 Numbers ---")
    nums = [float(input(f"Enter number {i}: ")) for i in range(1, 4)]
    print(f"Maximum: {max(nums)}")


# ─────────────────────────────────────────────
#  PROGRAM 7 — ASCII Code ↔ Character
# ─────────────────────────────────────────────
def program_07():
    """Display ASCII code of a character and vice versa."""
    print("\n--- Program 7: ASCII Code ↔ Character ---")
    choice = run_menu("Choose Conversion",
                      ["Character → ASCII code",
                       "ASCII code → Character"])
    if choice == 1:
        ch = input("Enter a character: ")
        print(f"ASCII code of '{ch}': {ord(ch[0])}")
    else:
        code = int(input("Enter ASCII code: "))
        print(f"Character for {code}: '{chr(code)}'")


# ─────────────────────────────────────────────
#  PROGRAM 8 — Armstrong Number Check
# ─────────────────────────────────────────────
def program_08():
    """Check if a number is an Armstrong (narcissistic) number."""
    print("\n--- Program 8: Armstrong Number Check ---")
    n = input("Enter a number: ").strip()
    digits = [int(d) for d in n]
    power = len(digits)
    total = sum(d ** power for d in digits)
    if total == int(n):
        print(f"{n} IS an Armstrong number ({' + '.join([f'{d}^{power}' for d in digits])} = {total}).")
    else:
        print(f"{n} is NOT an Armstrong number.")


# ─────────────────────────────────────────────
#  PROGRAM 9 — Factorial using Recursion
# ─────────────────────────────────────────────
def _factorial(n):
    return 1 if n <= 1 else n * _factorial(n - 1)

def program_09():
    """Find factorial of an entered number using recursion."""
    print("\n--- Program 9: Factorial using Recursion ---")
    n = int(input("Enter a non-negative integer: "))
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"{n}! = {_factorial(n)}")


# ─────────────────────────────────────────────
#  PROGRAM 10 — Fibonacci Series
# ─────────────────────────────────────────────
def program_10():
    """Print Fibonacci series up to n terms."""
    print("\n--- Program 10: Fibonacci Series ---")
    n = int(input("Enter number of terms: "))
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    print("Fibonacci Series:", ", ".join(map(str, series)))


# ─────────────────────────────────────────────
#  PROGRAM 11 — Greatest Number using Loop
# ─────────────────────────────────────────────
def program_11():
    """Enter numbers repeatedly and print the greatest."""
    print("\n--- Program 11: Greatest Number using Loop ---")
    n = int(input("How many numbers do you want to enter? "))
    numbers = [float(input(f"  Number {i+1}: ")) for i in range(n)]
    greatest = numbers[0]
    for num in numbers[1:]:
        if num > greatest:
            greatest = num
    print(f"Greatest number: {greatest}")


# ─────────────────────────────────────────────
#  PROGRAM 12 — Palindrome Check using Loop
# ─────────────────────────────────────────────
def program_12():
    """Check if a string is a palindrome using a loop."""
    print("\n--- Program 12: Palindrome Check ---")
    s = input("Enter a string: ").strip()
    n = len(s)
    is_palindrome = True
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            is_palindrome = False
            break
    print(f'"{s}" is {"a Palindrome" if is_palindrome else "NOT a Palindrome"}.')


# ─────────────────────────────────────────────
#  PROGRAM 13 — Grade Calculator (5 subjects)
# ─────────────────────────────────────────────
def program_13():
    """Enter marks for 5 subjects and print grade A/B/C/D/E."""
    print("\n--- Program 13: Grade Calculator ---")
    subjects = ["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]
    marks = []
    for sub in subjects:
        m = float(input(f"  Enter marks for {sub} (0-100): "))
        marks.append(m)
    avg = sum(marks) / len(marks)
    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    elif avg >= 45:
        grade = "D"
    else:
        grade = "E"
    print(f"Average Marks: {avg:.2f}  |  Grade: {grade}")


# ─────────────────────────────────────────────
#  PROGRAM 14 — Pattern Printing
# ─────────────────────────────────────────────
def program_14():
    """
    Display pattern:
         5
       4 5
     3 4 5
   2 3 4 5
 1 2 3 4 5
    """
    print("\n--- Program 14: Number Pattern ---")
    n = 5
    for i in range(n, 0, -1):
        # leading spaces
        print("  " * (i - 1), end="")
        # numbers from i to n
        print("  ".join(str(j) for j in range(i, n + 1)))


# ─────────────────────────────────────────────
#  PROGRAM 15 — sin(x) via Taylor Series
# ─────────────────────────────────────────────
def sin_taylor(x, n):
    """Compute sin(x) using Taylor series up to n terms."""
    result = 0
    for k in range(n):
        coeff = (-1) ** k
        numerator = x ** (2 * k + 1)
        denominator = _factorial(2 * k + 1)
        result += coeff * numerator / denominator
    return result

def program_15():
    """Calculate sin(x) using Taylor series expansion."""
    print("\n--- Program 15: sin(x) via Taylor Series ---")
    x = float(input("Enter x (in radians): "))
    n = int(input("Number of terms: "))
    approx = sin_taylor(x, n)
    exact  = math.sin(x)
    print(f"Taylor approximation ({n} terms): {approx:.8f}")
    print(f"math.sin value (exact)          : {exact:.8f}")
    print(f"Absolute error                  : {abs(approx - exact):.2e}")


# ─────────────────────────────────────────────
#  PROGRAM 16 — EOQ (Inventory Models)
# ─────────────────────────────────────────────
def program_16():
    """Determine EOQ using basic and production-run inventory models."""
    print("\n--- Program 16: EOQ Inventory Models ---")
    choice = run_menu("EOQ Model",
                      ["Basic EOQ (Wilson Formula)",
                       "Production Run Model (EPQ)"])
    if choice == 1:
        D = float(input("Annual demand (D): "))
        S = float(input("Ordering cost per order (S): "))
        H = float(input("Holding cost per unit per year (H): "))
        eoq = math.sqrt((2 * D * S) / H)
        orders_year = D / eoq
        cycle_time  = eoq / D * 365
        tc = (D / eoq) * S + (eoq / 2) * H
        print(f"\nEOQ              = {eoq:.2f} units")
        print(f"Orders per year  = {orders_year:.2f}")
        print(f"Cycle time       = {cycle_time:.2f} days")
        print(f"Total annual cost= {tc:.2f}")
    else:
        D = float(input("Annual demand rate (D): "))
        P = float(input("Production rate (P, must be > D): "))
        S = float(input("Setup cost per run (S): "))
        H = float(input("Holding cost per unit per year (H): "))
        if P <= D:
            print("Production rate must be greater than demand rate.")
            return
        epq = math.sqrt((2 * D * S) / (H * (1 - D / P)))
        tc  = (D / epq) * S + (epq / 2) * (1 - D / P) * H
        print(f"\nEPQ (Production lot size) = {epq:.2f} units")
        print(f"Total annual cost         = {tc:.2f}")


# ─────────────────────────────────────────────
#  PROGRAM 17 — Queuing Models
# ─────────────────────────────────────────────
def program_17():
    """Compute characteristics of M/M/1 and M/M/c queuing models."""
    print("\n--- Program 17: Queuing Models ---")
    choice = run_menu("Queuing Model",
                      ["M/M/1 Queue", "M/M/c Queue"])

    lam = float(input("Arrival rate λ (customers/unit time): "))
    mu  = float(input("Service rate  μ (customers/unit time): "))

    if choice == 1:
        rho = lam / mu
        if rho >= 1:
            print("System is unstable (ρ ≥ 1).")
            return
        Lq = rho ** 2 / (1 - rho)
        L  = rho / (1 - rho)
        Wq = Lq / lam
        W  = L  / lam
        print(f"\nM/M/1 Characteristics")
        print(f"  Traffic intensity ρ = {rho:.4f}")
        print(f"  Avg customers in system  L  = {L:.4f}")
        print(f"  Avg customers in queue   Lq = {Lq:.4f}")
        print(f"  Avg time in system       W  = {W:.4f}")
        print(f"  Avg time in queue        Wq = {Wq:.4f}")
    else:
        c = int(input("Number of servers (c): "))
        rho = lam / (c * mu)
        if rho >= 1:
            print("System is unstable (ρ ≥ 1).")
            return
        # P0 computation
        r = lam / mu
        sum_terms = sum((r ** n) / math.factorial(n) for n in range(c))
        last_term  = (r ** c) / (math.factorial(c) * (1 - rho))
        P0 = 1 / (sum_terms + last_term)
        Lq = (P0 * (r ** c) * rho) / (math.factorial(c) * (1 - rho) ** 2)
        Wq = Lq / lam
        W  = Wq + 1 / mu
        L  = lam * W
        print(f"\nM/M/{c} Characteristics")
        print(f"  P0 (prob system empty) = {P0:.4f}")
        print(f"  Traffic intensity ρ    = {rho:.4f}")
        print(f"  Avg customers in system  L  = {L:.4f}")
        print(f"  Avg customers in queue   Lq = {Lq:.4f}")
        print(f"  Avg time in system       W  = {W:.4f}")
        print(f"  Avg time in queue        Wq = {Wq:.4f}")


# ─────────────────────────────────────────────
#  PROGRAM 18 — Inheritance: Manager & Clerk from Employee
# ─────────────────────────────────────────────
def program_18():
    """Implement Inheritance — Employee → Manager and Clerk."""
    print("\n--- Program 18: Inheritance (Employee, Manager, Clerk) ---")

    class Employee:
        def __init__(self, name, emp_id, salary):
            self.name    = name
            self.emp_id  = emp_id
            self.salary  = salary

        def display(self):
            print(f"  Name      : {self.name}")
            print(f"  Emp ID    : {self.emp_id}")
            print(f"  Salary    : {self.salary}")

    class Manager(Employee):
        def __init__(self, name, emp_id, salary, department):
            super().__init__(name, emp_id, salary)
            self.department = department

        def display(self):
            print("\n[Manager Details]")
            super().display()
            print(f"  Department: {self.department}")

    class Clerk(Employee):
        def __init__(self, name, emp_id, salary, section):
            super().__init__(name, emp_id, salary)
            self.section = section

        def display(self):
            print("\n[Clerk Details]")
            super().display()
            print(f"  Section   : {self.section}")

    m = Manager("Alice", "M001", 75000, "Operations Research")
    c = Clerk  ("Bob",   "C042", 35000, "Data Entry")
    m.display()
    c.display()


# ─────────────────────────────────────────────
#  PROGRAM 19 — Fit Poisson Distribution
# ─────────────────────────────────────────────
def program_19():
    """Fit a Poisson distribution to given data."""
    print("\n--- Program 19: Fit Poisson Distribution ---")
    print("Enter space-separated observed frequency data (non-negative integers):")
    raw = input("Data: ").strip().split()
    data = [int(x) for x in raw]
    mu_hat = np.mean(data)
    max_val = max(data)
    x = np.arange(0, max_val + 1)
    pmf_values = poisson.pmf(x, mu_hat)
    print(f"\nEstimated λ (mean) = {mu_hat:.4f}")
    print(f"{'k':>5}  {'P(X=k)':>12}")
    print("-" * 20)
    for k, p in zip(x, pmf_values):
        print(f"{k:>5}  {p:>12.6f}")
    # Quick bar chart
    plt.figure(figsize=(7, 4))
    plt.bar(x, pmf_values, color="steelblue", edgecolor="white")
    plt.title(f"Fitted Poisson Distribution (λ={mu_hat:.2f})")
    plt.xlabel("k"); plt.ylabel("P(X=k)")
    plt.tight_layout(); plt.show()


# ─────────────────────────────────────────────
#  PROGRAM 20 — Linear Regression
# ─────────────────────────────────────────────
def program_20():
    """Implement linear regression using Python (numpy + matplotlib)."""
    print("\n--- Program 20: Linear Regression ---")
    print("Enter X values (space-separated): ")
    X = list(map(float, input().split()))
    print("Enter Y values (space-separated, same count): ")
    Y = list(map(float, input().split()))
    if len(X) != len(Y):
        print("Error: X and Y must have equal number of values.")
        return
    X_arr = np.array(X)
    Y_arr = np.array(Y)
    slope, intercept, r, p, se = stats.linregress(X_arr, Y_arr)
    Y_pred = slope * X_arr + intercept
    print(f"\nRegression Equation: Y = {slope:.4f}X + {intercept:.4f}")
    print(f"R² (coefficient of determination) = {r**2:.4f}")
    plt.figure(figsize=(7, 4))
    plt.scatter(X_arr, Y_arr, color="coral",    label="Observed",  zorder=3)
    plt.plot   (X_arr, Y_pred, color="steelblue", label="Fitted line")
    plt.title("Linear Regression"); plt.xlabel("X"); plt.ylabel("Y")
    plt.legend(); plt.tight_layout(); plt.show()


# ─────────────────────────────────────────────
#  PROGRAM 21 — Read & Write CSV File
# ─────────────────────────────────────────────
def program_21():
    """Perform read and write operations with a CSV file."""
    print("\n--- Program 21: CSV Read & Write ---")
    filename = "sample_data.csv"

    # Write
    rows = [
        ["Name",  "Age", "City"],
        ["Alice",  28,   "Delhi"],
        ["Bob",    35,   "Mumbai"],
        ["Carol",  22,   "Bangalore"],
    ]
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"Written to '{filename}'.")

    # Read back
    print(f"\nReading '{filename}':")
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print("  ", row)

    os.remove(filename)    # cleanup


# ─────────────────────────────────────────────
#  PROGRAM 22 — DataFrames and pandas
# ─────────────────────────────────────────────
def program_22():
    """Enter multi-column data in a DataFrame and display it."""
    print("\n--- Program 22: DataFrames with pandas ---")
    data = {
        "StudentID": [101, 102, 103, 104, 105],
        "Name"     : ["Amit", "Priya", "Raj", "Sneha", "Vikram"],
        "Maths"    : [88, 72, 95, 60, 83],
        "Science"  : [76, 85, 91, 70, 79],
        "English"  : [82, 90, 68, 74, 88],
    }
    df = pd.DataFrame(data)
    df["Total"]   = df[["Maths", "Science", "English"]].sum(axis=1)
    df["Average"] = df["Total"] / 3
    print(df.to_string(index=False))


# ─────────────────────────────────────────────
#  PROGRAM 23 — Statistical Measures with pandas
# ─────────────────────────────────────────────
def program_23():
    """Perform various statistical measures using pandas."""
    print("\n--- Program 23: Statistical Measures with pandas ---")
    print("Enter data values separated by spaces:")
    vals  = list(map(float, input().split()))
    series = pd.Series(vals)
    print(f"\n  Count    : {series.count()}")
    print(f"  Mean     : {series.mean():.4f}")
    print(f"  Median   : {series.median():.4f}")
    try:
        print(f"  Mode     : {series.mode()[0]:.4f}")
    except Exception:
        print("  Mode     : N/A")
    print(f"  Std Dev  : {series.std():.4f}")
    print(f"  Variance : {series.var():.4f}")
    print(f"  Min      : {series.min():.4f}")
    print(f"  Max      : {series.max():.4f}")
    print(f"  Range    : {series.max() - series.min():.4f}")
    print(f"  Skewness : {series.skew():.4f}")
    print(f"  Kurtosis : {series.kurt():.4f}")


# ─────────────────────────────────────────────
#  PROGRAM 24 — Bar Chart (School Results, 5 Years)
# ─────────────────────────────────────────────
def program_24():
    """Plot a bar chart displaying school results for 5 consecutive years."""
    print("\n--- Program 24: Bar Chart — School Results ---")
    years  = [2020, 2021, 2022, 2023, 2024]
    passed = [85,   90,   78,   92,   88]
    failed = [15,   10,   22,    8,   12]
    x = np.arange(len(years))
    width = 0.35
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(x - width/2, passed, width, label="Passed", color="steelblue")
    ax.bar(x + width/2, failed, width, label="Failed",  color="coral")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Students")
    ax.set_title("School Results for 5 Consecutive Years")
    ax.set_xticks(x); ax.set_xticklabels(years)
    ax.legend(); ax.grid(axis="y", alpha=0.3)
    plt.tight_layout(); plt.show()


# ─────────────────────────────────────────────
#  PROGRAM 25 — Plot y = x²
# ─────────────────────────────────────────────
def program_25():
    """Plot the graph of y = x²."""
    print("\n--- Program 25: Plot y = x² ---")
    x = np.linspace(-10, 10, 400)
    y = x ** 2
    plt.figure(figsize=(7, 5))
    plt.plot(x, y, color="darkorange", linewidth=2)
    plt.title("Graph of y = x²")
    plt.xlabel("x"); plt.ylabel("y = x²")
    plt.axhline(0, color="black", linewidth=0.8)
    plt.axvline(0, color="black", linewidth=0.8)
    plt.grid(alpha=0.3); plt.tight_layout(); plt.show()


# ─────────────────────────────────────────────
#  PROGRAM 26 — List, Tuple, Dictionary Operations
# ─────────────────────────────────────────────
def program_26():
    """Create and modify List, Tuple, and Dictionary."""
    print("\n--- Program 26: List, Tuple & Dictionary ---")

    # --- List ---
    print("\n[LIST]")
    lst = [10, 20, 30, 40, 50]
    print(f"  Original : {lst}")
    lst.append(60)
    print(f"  After append(60)      : {lst}")
    lst.insert(2, 25)
    print(f"  After insert(2, 25)   : {lst}")
    lst.remove(40)
    print(f"  After remove(40)      : {lst}")
    lst.sort(reverse=True)
    print(f"  After sort(reverse)   : {lst}")

    # --- Tuple ---
    print("\n[TUPLE]")
    tup = (5, 3, 8, 1, 9, 2)
    print(f"  Tuple        : {tup}")
    print(f"  Min          : {min(tup)}")
    print(f"  Max          : {max(tup)}")
    print(f"  Count of 3   : {tup.count(3)}")
    print(f"  Index of 8   : {tup.index(8)}")
    # Tuples are immutable; demonstrate conversion
    lst2 = list(tup)
    lst2.append(100)
    tup2 = tuple(lst2)
    print(f"  After adding 100 (new tuple): {tup2}")

    # --- Dictionary ---
    print("\n[DICTIONARY]")
    d = {"name": "Alice", "age": 25, "city": "Delhi"}
    print(f"  Original : {d}")
    d["email"] = "alice@example.com"
    print(f"  After adding email  : {d}")
    d["age"] = 26
    print(f"  After updating age  : {d}")
    del d["city"]
    print(f"  After deleting city : {d}")
    print(f"  Keys   : {list(d.keys())}")
    print(f"  Values : {list(d.values())}")


# ─────────────────────────────────────────────
#  PROGRAM 27 — Correlation
# ─────────────────────────────────────────────
def program_27():
    """Find correlation between dependent and independent variables."""
    print("\n--- Program 27: Correlation ---")
    print("Enter X values (independent variable, space-separated):")
    X = list(map(float, input().split()))
    print("Enter Y values (dependent variable, same count):")
    Y = list(map(float, input().split()))
    if len(X) != len(Y):
        print("Error: X and Y must have the same length.")
        return
    X_arr = np.array(X)
    Y_arr = np.array(Y)
    r, p_val = stats.pearsonr(X_arr, Y_arr)
    print(f"\nPearson Correlation Coefficient (r) = {r:.4f}")
    print(f"P-value                             = {p_val:.4f}")
    if abs(r) >= 0.8:
        strength = "Strong"
    elif abs(r) >= 0.5:
        strength = "Moderate"
    else:
        strength = "Weak"
    direction = "Positive" if r > 0 else "Negative"
    print(f"Interpretation: {strength} {direction} Correlation")

    # Scatter plot with regression line
    slope, intercept = np.polyfit(X_arr, Y_arr, 1)
    plt.figure(figsize=(7, 4))
    plt.scatter(X_arr, Y_arr, color="coral", zorder=3, label="Data Points")
    plt.plot(X_arr, slope * X_arr + intercept, color="steelblue", label="Regression Line")
    plt.title(f"Correlation Plot  (r = {r:.4f})")
    plt.xlabel("X (Independent)"); plt.ylabel("Y (Dependent)")
    plt.legend(); plt.tight_layout(); plt.show()


# ─────────────────────────────────────────────
#  PROGRAM 28 — Data Visualisation
# ─────────────────────────────────────────────
def program_28():
    """Charts using plot(), Pie Chart, Scatter Plot, Histogram, Bar Chart."""
    print("\n--- Program 28: Data Visualisation ---")
    np.random.seed(42)
    data   = np.random.randn(200) * 10 + 50
    cats   = ["A", "B", "C", "D", "E"]
    values = [23, 45, 17, 35, 29]
    x_sc   = np.random.rand(50) * 100
    y_sc   = 0.6 * x_sc + np.random.randn(50) * 10

    fig, axes = plt.subplots(2, 3, figsize=(15, 8))
    fig.suptitle("Data Visualisation — Program 28", fontsize=14)

    # 1. Line plot
    axes[0, 0].plot(np.linspace(0, 4 * np.pi, 300), np.sin(np.linspace(0, 4 * np.pi, 300)),
                    color="steelblue")
    axes[0, 0].set_title("Line Plot (sin wave)")

    # 2. Bar chart
    axes[0, 1].bar(cats, values, color="coral", edgecolor="white")
    axes[0, 1].set_title("Bar Chart")

    # 3. Pie chart
    axes[0, 2].pie(values, labels=cats, autopct="%1.1f%%", startangle=140)
    axes[0, 2].set_title("Pie Chart")

    # 4. Scatter plot
    axes[1, 0].scatter(x_sc, y_sc, color="mediumpurple", alpha=0.7)
    axes[1, 0].set_title("Scatter Plot")

    # 5. Histogram
    axes[1, 1].hist(data, bins=15, color="mediumseagreen", edgecolor="white")
    axes[1, 1].set_title("Histogram")

    # 6. Horizontal bar chart
    axes[1, 2].barh(cats, values, color="goldenrod")
    axes[1, 2].set_title("Horizontal Bar Chart")

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()


# ─────────────────────────────────────────────
#  PROGRAM 29 — PuLP Library
# ─────────────────────────────────────────────
def program_29():
    """Solve a Linear Programming problem using PuLP."""
    print("\n--- Program 29: PuLP — Linear Programming ---")
    print("Maximise  Z = 5x + 4y")
    print("Subject to:")
    print("  6x + 4y ≤ 24")
    print("  x + 2y  ≤  6")
    print("  x, y   ≥  0")

    prob = LpProblem("LP_Example", LpMaximize)
    x = LpVariable("x", lowBound=0)
    y = LpVariable("y", lowBound=0)

    prob += 5 * x + 4 * y           # Objective
    prob += 6 * x + 4 * y <= 24     # Constraint 1
    prob +=     x + 2 * y <= 6      # Constraint 2

    prob.solve(PULP_CBC_CMD(msg=0))
    print(f"\nStatus   : {LpStatus[prob.status]}")
    print(f"x        = {value(x):.4f}")
    print(f"y        = {value(y):.4f}")
    print(f"Max Z    = {value(prob.objective):.4f}")


# ─────────────────────────────────────────────
#  PROGRAM 30 — SciPy Library
# ─────────────────────────────────────────────
def program_30():
    """Demonstrate SciPy: optimization, integration, root-finding, stats."""
    print("\n--- Program 30: SciPy Demonstrations ---")

    # 1. Minimise f(x) = (x - 3)² + 2
    print("\n1. Optimisation — minimise f(x) = (x-3)² + 2")
    f = lambda x: (x - 3) ** 2 + 2
    result = opt.minimize_scalar(f)
    print(f"   Minimum at x = {result.x:.4f},  f(x) = {result.fun:.4f}")

    # 2. Find root of x³ - x - 2 = 0
    print("\n2. Root finding — x³ - x - 2 = 0")
    g = lambda x: x ** 3 - x - 2
    root = opt.brentq(g, 1, 2)
    print(f"   Root ≈ {root:.6f}")

    # 3. Numerical integration of sin(x) from 0 to π
    print("\n3. Numerical integration of sin(x) from 0 to π")
    area, error = opt.quad(math.sin, 0, math.pi) if False else \
                  __import__("scipy.integrate", fromlist=["quad"]).quad(math.sin, 0, math.pi)
    print(f"   ∫₀^π sin(x) dx ≈ {area:.6f}  (exact = 2.0)")

    # 4. Descriptive statistics
    print("\n4. Descriptive statistics on a sample dataset")
    sample = [12, 15, 14, 10, 18, 21, 11, 16, 13, 19]
    desc = stats.describe(sample)
    print(f"   n        = {desc.nobs}")
    print(f"   Mean     = {desc.mean:.4f}")
    print(f"   Variance = {desc.variance:.4f}")
    print(f"   Skewness = {desc.skewness:.4f}")
    print(f"   Kurtosis = {desc.kurtosis:.4f}")

    # 5. One-sample t-test
    print("\n5. One-sample t-test (H₀: mean = 15)")
    t_stat, p_val = stats.ttest_1samp(sample, 15)
    print(f"   t-statistic = {t_stat:.4f},  p-value = {p_val:.4f}")
    print(f"   {'Reject' if p_val < 0.05 else 'Fail to reject'} H₀ at α = 0.05")


# ============================================================
#   MAIN MENU
# ============================================================
PROGRAMS = {
    1 : ("Hello, Name",                          program_01),
    2 : ("Arithmetic Operations (menu-driven)",  program_02),
    3 : ("Roots of a Quadratic Equation",        program_03),
    4 : ("Reverse Number & Sum of Digits",       program_04),
    5 : ("Odd / Even / Prime",                   program_05),
    6 : ("Maximum of 3 Numbers",                 program_06),
    7 : ("ASCII Code ↔ Character",               program_07),
    8 : ("Armstrong Number Check",               program_08),
    9 : ("Factorial using Recursion",            program_09),
    10: ("Fibonacci Series",                     program_10),
    11: ("Greatest Number using Loop",           program_11),
    12: ("Palindrome Check",                     program_12),
    13: ("Grade Calculator (5 subjects)",        program_13),
    14: ("Number Pattern",                       program_14),
    15: ("sin(x) via Taylor Series",             program_15),
    16: ("EOQ Inventory Models",                 program_16),
    17: ("Queuing Models (M/M/1, M/M/c)",        program_17),
    18: ("Inheritance — Employee/Manager/Clerk", program_18),
    19: ("Fit Poisson Distribution",             program_19),
    20: ("Linear Regression",                    program_20),
    21: ("CSV Read & Write",                     program_21),
    22: ("DataFrames with pandas",               program_22),
    23: ("Statistical Measures with pandas",     program_23),
    24: ("Bar Chart — School Results",           program_24),
    25: ("Plot y = x²",                          program_25),
    26: ("List, Tuple & Dictionary",             program_26),
    27: ("Correlation",                          program_27),
    28: ("Data Visualisation",                   program_28),
    29: ("PuLP — Linear Programming",            program_29),
    30: ("SciPy Demonstrations",                 program_30),
}

def main():
    while True:
        print("\n" + "=" * 55)
        print("   Dept. of Operational Research, University of Delhi")
        print("              Python Lab — All 30 Programs")
        print("=" * 55)
        for num, (title, _) in PROGRAMS.items():
            print(f"  {num:>2}. {title}")
        print("   0. Exit")
        print("=" * 55)
        try:
            choice = int(input("Select program (0 to exit): "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if choice == 0:
            print("Goodbye!")
            break
        if choice in PROGRAMS:
            try:
                PROGRAMS[choice][1]()
            except Exception as e:
                print(f"[Error in program {choice}]: {e}")
        else:
            print(f"Invalid choice. Enter 0–{len(PROGRAMS)}.")

if __name__ == "__main__":
    main()