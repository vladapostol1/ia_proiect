import math


def coeficient_binomial(n, k):
    return math.comb(n, k)


def newton_binomial(a, b, n):
    steps = []

    steps.append(f"Premisa formula generala: \n")
    steps.append(f"(a + b) ^ n = Σ(k = 0 -> n) [C(n, k) * a ^ (n - k) * b ^ k]\n")

    if n == 1:
        steps.append("Cazul de baza: n = 1, formula devine: \n")
        steps.append("(a + b) ^ 1 = a + b")
        return steps, f"{a} + {b}"

    steps.append(f"Dezvoltare pentru n = {n}. \n")
    terms = []
    for k in range(n + 1):
        coef = coeficient_binomial(n, k)
        steps.append(f"\nPasul {k + 1}: Termen pentru k = {k}")
        steps.append(f"Coeficient binomial C({n}, {k}) = {coef}")

        term = f"{coef} * a ^ {n - k} * b ^ {k}"
        steps.append(f"Termen: {term}")

        terms.append(term)

        # steps.append(f"Adaugam termenul")

    result = " + ".join(terms)
    steps.append("Termenii au fost calculati. Expansiune completa:")
    steps.append(result)
    return steps, result


def main():
    a = input("Valoare a: ")
    b = input("Valoare b: ")
    n = int(input("Valoare n: "))

    steps, result = newton_binomial(a, b, n)

    print("Demonstratie: ")
    for step in steps:
        print("\n" + step)

    print("\nRezultat final: " + result)


if __name__ == "__main__":
    main()
