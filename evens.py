def even_number_of_evens(numbers):
    """
        Return an error if the type of numbers is not a list
        If no numbers return False
        If even number of evens return True
        If odd number of evens return False
        If no even numbers return False
    """
    if type(numbers) is list:
        num_evens = len([1 for n in numbers if n % 2 == 0])
        return num_evens % 2 == 0 and num_evens != 0

    else:
        raise TypeError("A list was not passed into the function")


if __name__ == "__main__":
    print(even_number_of_evens([2, 1, 4]))
