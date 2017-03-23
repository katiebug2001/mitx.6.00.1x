import unittest

trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    if int(us_num) <= 10: #know us_num is more than or equal to 0 b/c of function specs
        return trans[us_num]
    elif int(us_num) <= 19: #know us_num is more than 10 (i.e., at least 11) because of previous conditional.
        digit = us_num[1]
        return 'shi {}'.format(trans[digit])
    else: #know us_num is more than 19 b/c of previous conditional and is less than 100 b/c of function specs
        ten = us_num[0]
        digit = us_num[1]
        if digit == '0':
            return '{} shi'.format(trans[ten])
        else:
            return '{} shi {}'.format(trans[ten], trans[digit])


#print(convert_to_mandarin('0'))
#print(convert_to_mandarin('10'))
#print(convert_to_mandarin('11'))
#print(convert_to_mandarin('20'))
#print(convert_to_mandarin('55'))
#print(convert_to_mandarin('67'))


class test_convert_to_mandarin(unittest.TestCase):
    """
    tests convert_to_mandarin()
    """

    def test_mandarin_numbers(self):
        """
        tests 2 numbers from each: 0-10, 11-19, 20-99
        """
        test_us = ['0', '10', '11', '17', '23', '80']
        test_mandarin = []
        for n in test_us:
            test_mandarin.append(convert_to_mandarin(n))
        self.assertEqual(['ling', 'shi', 'shi yi', 'shi qi', 'er shi san', 'ba shi'], test_mandarin)


if __name__ == '__main__':
    unittest.main()

