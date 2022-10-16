# HW Excercise 1

class SetCalculator:
    @staticmethod
    def addition(set_of_integers):
        if isinstance(set_of_integers, set):
            sum_of_elements = 0
            for i in set_of_integers:
                if isinstance(i, int):
                    sum_of_elements += i
                else:
                    return "Error: wrong input."
            return sum_of_elements
        return 'Error: input is not a set.'

    @staticmethod
    def average(set_of_integers):
        if isinstance(set_of_integers, set):
            set_count = 0
            sum_of_elements = 0
            for i in set_of_integers:
                if isinstance(i, int):
                    set_count += 1
                    sum_of_elements += i
                else:
                    return "Error: wrong input."
            set_average = sum_of_elements / set_count
            return set_average
        return 'Error: input is not a set.'

    @staticmethod
    def set_maximum(set_of_integers):
        if isinstance(set_of_integers, set):
            set_max = 0
            for i in set_of_integers:
                if isinstance(i, int):
                    if i > set_max:
                        set_max = i
                else:
                    return "Error: wrong input."
            return set_max
        return 'Error: input is not a set.'

    @staticmethod
    def set_minimum(set_of_integers):
        if isinstance(set_of_integers, set):
            set_min = 0
            for i in set_of_integers:
                if isinstance(i, int):
                    if i < set_min:
                        set_min = i
                else:
                    return "Error: wrong input."
            return set_min
        return 'Error: input is not a set.'


# create set (no duplicates)
proper_test_set = {-1, 0, 2, 99}
wrong_test_set = {1, 2, 'q'}
wrong_input = [1, 2, 3]

print(type(proper_test_set))
print(proper_test_set)

# create object
a = SetCalculator()

# adding
print('\nAdding:')
print(a.addition(proper_test_set))
print(a.addition(wrong_test_set))
print(a.addition(wrong_input))

# average
print('\nAverage:')
print(a.average(proper_test_set))
print(a.average(wrong_test_set))
print(a.average(wrong_input))

# maximum
print('\nMaximum:')
print(a.set_maximum(proper_test_set))
print(a.set_maximum(wrong_test_set))
print(a.set_maximum(wrong_input))

# minimum
print('\nMinimum:')
print(a.set_minimum(proper_test_set))
print(a.set_minimum(wrong_test_set))
print(a.set_minimum(wrong_input))