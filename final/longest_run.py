import unittest
def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """
    length_longest_run = 0
    list_longest_run = []

    up_length_this_run = 0
    up_list_this_run = []
    down_length_this_run = 0
    down_list_this_run = []
    prev_num = None

    for this_num in L:
        #print('the number is {} & the previous number is {}'.format(this_num, prev_num))

        try:
            if prev_num <= this_num:
                up_length_this_run += 1
                up_list_this_run.append(this_num)
            else:
                up_length_this_run = 1
                up_list_this_run = [this_num]

            if prev_num >= this_num:
                down_length_this_run += 1
                down_list_this_run.append(this_num)
            else:
                down_length_this_run = 1
                down_list_this_run = [this_num]

        except TypeError:
            up_length_this_run += 1
            down_length_this_run += 1
            up_list_this_run.append(this_num)
            down_list_this_run.append(this_num)
            prev_num = this_num

        finally:
            if up_length_this_run > length_longest_run:
                length_longest_run, list_longest_run = up_length_this_run, up_list_this_run
            elif down_length_this_run > length_longest_run:
                length_longest_run, list_longest_run = down_length_this_run, down_list_this_run
            prev_num = this_num
            #print('this up is {}'.format(up_list_this_run))
            #print('this down is {}'.format(down_list_this_run))
            #print('current longest is {}'.format(list_longest_run))

    return sum(list_longest_run)

# class test_longest_run(unittest.TestCase):
#     """
#     tests longest_run()
#     """
#
#     def test_this_longest_run(self):
#         """
#         tests that longest_run returns the correct value for [1, 2, 3, 2, 0] (should be 6); for [3, 2, 0, -1, 2] (should be 4) and [1] (should be 1)
#         """
#         test_sums = [6, 4, 1]
#         test_lists = [[1, 2, 3, 2, 0], [3, 2, 0, -1, 2], [1]]
#         self.assertEqual([longest_run(test_lists[0]), longest_run(test_lists[1]), longest_run(test_lists[2])], test_sums)
#
#
# if __name__ == '__main__':
#     unittest.main()
print(longest_run([1, 2, 3, 2, -1, -10]))