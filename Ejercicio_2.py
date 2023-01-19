def simplify(polynomial: str) -> str:
    from collections import Counter
    from itertools import groupby
    from operator import itemgetter

    # Dividir el polinomio en monomios
    monomials = polynomial.split("+")

    # Agrupar los monomios por su grado
    monomials.sort(key=lambda x: len(x), reverse=True)
    monomials_by_degree = groupby(monomials, key=lambda x: len(x))

    # Ordenar monomios dentro de cada grupo de grado por orden lexicográfico
    monomials_by_degree = {degree: sorted(list(monomials)) for degree, monomials in monomials_by_degree}

    # Agrupar monomios por sus variables
    monomials_by_variables = {}
    for degree, monomials in monomials_by_degree.items():
        for monomial in monomials:
            variables = "".join(sorted(list(set(monomial))))
            if variables not in monomials_by_variables:
                monomials_by_variables[variables] = []
            monomials_by_variables[variables].append(monomial)

    # Simplificar monomios combinando términos semejantes
    simplified_monomials = []
    for variables, monomials in monomials_by_variables.items():
        monomials_coefficients = Counter([m.replace("-", "") for m in monomials])
        for monomial, coefficient in monomials_coefficients.items():
            if coefficient > 0:
                simplified_monomials.append(f"{coefficient}{variables}")
            elif coefficient < 0:
                simplified_monomials.append(f"{coefficient}{variables}")

    # Ordenar monomios por orden lexicográfico
    simplified_monomials.sort()

    # Crea la cadena polinomial simplificada
    simplified_polynomial = "+".join(simplified_monomials)
    if simplified_polynomial[0] == "+":
        simplified_polynomial = simplified_polynomial[1:]
    return simplified_polynomial

if __name__ == "__main__":
    # Casos de prueba
    test_cases = [
        "3x-zx+2xy-x",
        "cb+cba",
        "2xy-yx",
        "-a+5ab+3a-c-2a",
        "-abc+3a+2ac",
        "xyz-xz",
        "a+ca-ab",
        "xzy+zby",
        "-y+x",
        "y-x"
    ]
    for polynomial in test_cases:
        simplified_polynomial = simplify(polynomial)
        print(f"{polynomial} -> {simplified_polynomial}")