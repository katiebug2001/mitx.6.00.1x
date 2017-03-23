def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """

    def base_function(x):
        raw_list = L
        print(raw_list)
        list_to_be_added = []
        length_backwards_counter = 1
        for n in raw_list :
            k = n * (x**(len(L) - length_backwards_counter))
            list_to_be_added.append(k)
            print(list_to_be_added)
            length_backwards_counter += 1
        the_number = sum(list_to_be_added)
        return the_number

    return base_function

print(general_poly([1, 2, 3, 4])(10))
print(general_poly([1, 2, 3])(2))