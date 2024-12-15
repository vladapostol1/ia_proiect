import math

def binomial_coefficient(n, k):
    return math.comb(n, k)

def newton_binomial(a, b, n):
    steps = []

    steps.append(f"Premisa: Formula generală pentru Binomul lui Newton este:")
    steps.append(f"(a + b)^n = ∑(k=0 până la n) [C(n, k) * a^(n-k) * b^k]\n")

    if n == 1:
        steps.append("Caz de bază: Pentru n=1, formula devine:")
        steps.append("(a + b)^1 = a + b")
        expanded_result = f"{a} + {b}"
        numeric_result = float(a) + float(b)
        return steps, expanded_result, numeric_result

    steps.append(f"Calculăm dezvoltarea pentru n={n}. Vom determina fiecare termen al sumei pas cu pas:")
    expanded_terms = []
    numeric_terms = []

    for k in range(n + 1):
        coef = binomial_coefficient(n, k)
        steps.append(f"Pasul {k + 1}: Calculăm termenul pentru k={k}.")
        steps.append(f"Coeficientul binomial C({n}, {k}) = {coef}")

        expanded_term = f"{coef} * {a}^{n - k} * {b}^{k}"
        expanded_terms.append(expanded_term)
        steps.append(f"Termenul expandat este: {expanded_term}")

        numeric_term = coef * (float(a) ** (n - k)) * (float(b) ** k)
        numeric_terms.append(numeric_term)
        steps.append(f"Valoarea numerică este: {numeric_term}")


        steps.append(f"Adăugăm termenul în expansiune.\n")

    expanded_result = " + ".join(expanded_terms)
    numeric_result = sum(numeric_terms)
    steps.append("Toți termenii au fost calculați. Expansiunea este:")
    steps.append(f"{expanded_result}")
    steps.append(f"\nIar valoarea numerică este: {numeric_result}")

    return steps, expanded_result, numeric_result



def main():
    print("Demonstrație: Binomul lui Newton prin raționament înainte\n")
    a = float(input("Introduceți valoarea lui a: "))
    b = float(input("Introduceți valoarea lui b: "))
    n = int(input("Introduceți valoarea lui n: "))

    if(n < 0):
        raise Exception("valoarea lui n trebuie sa fie mai mare sau egala cu 0.")

    steps, expanded_result, numeric_result = newton_binomial(a, b, n)

    print("\nPașii demonstrației:")
    for step in steps:
        print(step)

if __name__ == "__main__":
    main()