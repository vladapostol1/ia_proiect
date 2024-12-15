import math

def binomial_coefficient(n, k):
    return math.comb(n, k)

def newton_binomial(a, b, n):
    steps = []

    steps.append(f"Premisa: Formula generală pentru Binomul lui Newton este:")
    steps.append(f"(a + b)^n = ∑(k=0 până la n) [C(n, k) * a^(n-k) * b^k]\n")

    if n == 1:
        steps.append("Caz de bază: Pentru n=1, formula devine direct:")
        steps.append("(a + b)^1 = a + b")
        return steps, f"{a} + {b}"

    steps.append(f"Calculăm dezvoltarea pentru n={n}. Vom determina fiecare termen al sumei pas cu pas:")
    terms = []
    for k in range(n + 1):
        coef = binomial_coefficient(n, k)
        steps.append(f"Pasul {k + 1}: Calculăm termenul pentru k={k}.")
        steps.append(f"Coeficientul binomial C({n}, {k}) = {coef}")

        term = f"{coef} * a^{n - k} * b^{k}"
        steps.append(f"Termenul este: {term}")

        terms.append(term)
        steps.append(f"Adăugăm termenul în expansiune.\n")

    result = " + ".join(terms)
    steps.append("Toți termenii au fost calculați. Expansiunea completă este:")
    steps.append(result)
    return steps, result


def main():
    print("Demonstrație: Binomul lui Newton prin raționament înainte\n")
    a = input("Introduceți valoarea lui a: ")
    b = input("Introduceți valoarea lui b: ")
    n = int(input("Introduceți valoarea lui n: "))

    steps, result = newton_binomial(a, b, n)

    print("\nPașii demonstrației:")
    for step in steps:
        print("- " + step)

    print("\nRezultatul final:")
    print(result)


if __name__ == "__main__":
    main()
