'''
Write a function called general_poly, that meets the specifications below.
For example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234 because 1∗10^3+2∗10^2+3∗10^1+4∗10^0.

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE
'''


def general_poly(L):
    """
    Return polynomial sum function (with specified coefficient) that will apply to a given base
    :param L: value of polynomial coefficients from highest to lowest powers
    :return: function that would take given coefficients and apply it to a given base
    """
    coefficients = L
    powers = reversed(range(len(L)))

    def poly_raise(base=0):
        """
        Raise input base with the existing coefficients and powers from the enclosing general_poly function
        :param base: base value of the polynomial
        :return: polynomial sums of all terms raised from the base with the existing coefficients and powers
        """
        poly_sum = 0
        for coefficient, power in zip(coefficients, powers):
            poly_sum += coefficient * (base**power)
        return poly_sum

    return poly_raise


if __name__ == '__main__':
    print(general_poly([6, 3, 9, 7])(0))

