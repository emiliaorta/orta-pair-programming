def offset_mean(array, target_mean):
    """
    Shift the values in an array so that the mean matches target_mean

    Parameters:
    array : list of numbers (Input values)
    target_mean : float (The mean you want the output array to have)

    Returns:
    list of float (A new list with all values shifted by the same amount.)
    """
    current_mean = sum(array) / len(array)
    offset = target_mean - current_mean

    new_array = []
    for value in array:
        new_array.append(value + offset)

    return new_array

'''
Feedback: 
- I like how it is a function so it can easily be called with a lot of different inputs. 
- A small improvement could be having the output be a numpy array instead of a Python list because if it was in numpy functions like .mean() or .diff() could be used for tests.
'''
