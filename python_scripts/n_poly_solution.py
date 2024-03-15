# Add any imports you need here

def n_poly(
        x, *coeffs
        ):
    order = len(coeffs) - 1
    return sum([coeffs[i] * x ** (order-i) for i in range(len(coeffs))])
