class CheckEven:
    # @staticmethod is a static method that does not require an instance of the class to be called.
    # self keyword is not used in static methods, as they do not operate on an instance of the class.
    @staticmethod
    def is_even(num_list):
        even_numbers = [num for num in num_list if num % 2 == 0]
        print("List of numbers:", num_list)
        print("Even numbers in the list:", even_numbers)

ch1 = CheckEven()
ch1.is_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ch1.is_even([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])